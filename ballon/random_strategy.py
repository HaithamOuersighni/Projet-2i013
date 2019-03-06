# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu, math
from soccersimulator import settings 
from .tools import *
from .settings import *


class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        return SoccerAction(Vector2D.create_random(),Vector2D.create_random())

class joueur_fonceur(Strategy):
    def __init__(self):
        Strategy.__init__(self,"neymar")
    
    def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        i=s.goal.x
        if s.milieu:
                return SoccerAction(Vector2D(),Vector2D(i,GAME_HEIGHT/2)-s.player)
        if s.cannot:
            return SoccerAction((s.ball+2*s.vball-s.player),Vector2D())
        else:
            if id_team==1:
                if state.player_state(2,0).position.x>s.player.x:
                    if s.player.y>45:
                        return SoccerAction((s.ball+2*s.vball-s.player),Vector2D(s.player.x+5, s.player.y+5).normalize()*3)
                    else:
                        return SoccerAction((s.ball+2*s.vball-s.player),Vector2D(s.player.x+5, s.player.y-5).normalize()*3)
                else:
                    return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize())
            else:
                if state.player_state(1,0).position.x>s.player.x:
                    if s.player.y<45:
                        return SoccerAction((s.ball+2*s.vball-s.player),Vector2D(0,GAME_HEIGHT))
                    else:
                        return SoccerAction((s.ball+2*s.vball-s.player),Vector2D(0,0))
                else:
                    return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize())
  
class joueur_fonceur2(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Fonceur2")
        
    def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        i=s.goal.x
        if s.cannot:
            return SoccerAction((s.ball-s.player),Vector2D())
        return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2)-s.player)*4)
    
class alfonseur(Strategy):
    def __init__(self):
        Strategy.__init__(self,"alfonseur")
        
    def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        i=s.goal.x
        
        #pos depart
        if s.milieu:
            if id_team==1:
                return SoccerAction(Vector2D(GAME_WIDTH/6,GAME_HEIGHT/2)-s.player,Vector2D())
            else:
                return SoccerAction(Vector2D(5*GAME_WIDTH/6,GAME_HEIGHT/2)-s.player,Vector2D())
        
        if(id_team==1):
            
            if s.ball.x<GAME_WIDTH/4:
                if s.ball.y>30 and s.ball.y<60 and s.pos_eproche.y>30 and s.pos_eproche.y<60 and s.pos_eproche.x>s.player.x and (s.pos_eproche.y-s.player.y<10):
                    if s.cannot:
                        return SoccerAction((s.ball+2*s.vball-s.player),Vector2D())
                    elif s.ball.y>(GAME_HEIGHT/2):
                        return SoccerAction((s.ball-s.player),(Vector2D(0,GAME_HEIGHT)-s.player).normalize()*3)
                    else:
                        return SoccerAction((s.ball-s.player),(Vector2D(0,0)-s.player).normalize()*3)
                    
                elif s.ball.y<30 and s.ball.x<GAME_WIDTH/4 and s.pos_eproche.y<30 and s.pos_eproche.x>s.player.x or s.enorme<s.norme:
                    return SoccerAction((Vector2D(s.aligne_def_y,30)-s.player),Vector2D())
                
                elif s.ball.y>60 and s.ball.x<GAME_WIDTH/4 and s.pos_eproche.y>60 and s.pos_eproche.x>s.player.x or s.enorme<s.norme:
                    return SoccerAction((Vector2D(s.aligne_def_y,60)-s.player),Vector2D())
                
                elif (s.ball.y>30 and s.pos_eproche.y<30 and s.ball.x<GAME_WIDTH/4 and s.pos_eproche.x<GAME_WIDTH/4 and s.norme<s.enorme) or (s.ball.y< 60 and s.pos_eproche.y>60 and s.ball.x<GAME_WIDTH/4 and s.pos_eproche.x<GAME_WIDTH/4 and s.norme<s.enorme):
                    if s.cannot:
                        return SoccerAction((s.ball+2*s.vball-s.player),Vector2D())
                    else:
                        return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2).normalize()*6))
            if s.cannot:
                return SoccerAction((s.ball+2*s.vball-s.player),Vector2D())
            else:
                return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize())
        else:
            if s.ball.x>3*GAME_WIDTH/4:
                if s.ball.y>30 and s.ball.y<60 and s.pos_eproche.y>30 and s.pos_eproche.y<60 and s.pos_eproche.x<s.player.x and (s.pos_eproche.y-s.player.y<10):
                    if s.cannot:
                        return SoccerAction((s.ball+2*s.vball-s.player),Vector2D())
                    elif s.ball.y>(GAME_HEIGHT/2):
                        return SoccerAction((s.ball-s.player),(Vector2D(GAME_WIDTH,GAME_HEIGHT)-s.player).normalize()*3)
                    else:
                        return SoccerAction((s.ball-s.player),(Vector2D(GAME_WIDTH,0)-s.player).normalize()*3)
                    
                elif s.ball.y<30 and s.ball.x>3*GAME_WIDTH/4 and s.pos_eproche.y<30 and s.pos_eproche.x<s.player.x or s.enorme<s.norme:
                    return SoccerAction((Vector2D(s.aligne_def_y,30)-s.player),Vector2D())
                
                elif s.ball.y>60 and s.ball.x>3*GAME_WIDTH/4 and s.pos_eproche.y>60 and s.pos_eproche.x<s.player.x or s.enorme<s.norme:
                    return SoccerAction((Vector2D(s.aligne_def_y,60)-s.player),Vector2D())
                
                elif (s.ball.y>30 and s.pos_eproche.y<30 and s.ball.x>3*GAME_WIDTH/4 and s.pos_eproche.x>3*GAME_WIDTH/4 and s.norme<s.enorme) or (s.ball.y< 60 and s.pos_eproche.y>60 and s.ball.x>3*GAME_WIDTH/4 and s.pos_eproche.x>3*GAME_WIDTH/4 and s.norme<s.enorme):
                    if s.cannot:
                        return SoccerAction((s.ball+2*s.vball-s.player),Vector2D())
                    else:
                        return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize()*6)
            if s.cannot:
                return SoccerAction((s.ball+2*s.vball-s.player),Vector2D())
            else:
                return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize())
            
            
            
            
                
class joueur_attaquant(Strategy):
     def __init__(self):
        Strategy.__init__(self, "Attaquant")
        
     def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        i=s.goal.x
        if id_team==2: 
           if  s.ball.x>GAME_WIDTH/100*70:
               if s.ball.y>GAME_HEIGHT/2:
                   return SoccerAction((Vector2D(GAME_WIDTH/100*65,s.ball.y+10)-s.player),Vector2D())
               return SoccerAction((Vector2D(GAME_WIDTH/100*65,s.ball.y-10)-s.player),Vector2D())
        if id_team==1:
            if s.ball.x<GAME_WIDTH/100*30:
                if s.ball.y<GAME_HEIGHT/2:
                    return SoccerAction((Vector2D(GAME_WIDTH/100*35,s.ball.y+10)-s.player),Vector2D())
                return SoccerAction((Vector2D(GAME_WIDTH/100*35,s.ball.y-10)-s.player),Vector2D())
        if s.cannot:
            return SoccerAction((s.ball+4*s.vball-s.player),Vector2D())
        if (s.player.x<6*GAME_WIDTH/7 and s.id_team==1)or(s.player.x>GAME_WIDTH/7 and s.id_team==2) or (s.cnorme>s.gnorme):
            return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize())
        else:
            return SoccerAction((s.ball-s.player),Vector2D(i,GAME_HEIGHT/2)-s.player)
        
        
class joueur_unedeux(Strategy):
     def __init__(self):
        Strategy.__init__(self, "unedeux")
        
     def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        i=s.goal.x
        if (id_team==1):
            p=10
        else:
            p=-10
        if s.ide==0:
            if s.milieu:
                return SoccerAction((s.ball-s.player),Vector2D(s.unedeux.x-s.player.x+p,s.unedeux.y-s.player.y).normalize()*1.5)
            if  s.ball.y>GAME_HEIGHT/2:
                if(s.ball.x<(5*GAME_WIDTH/6)-15 and s.id_team==1) or (s.ball.x>(GAME_WIDTH/6)+15 and s.id_team==2 ):
                    return SoccerAction((Vector2D(s.ball.x,35)-s.player),Vector2D())
                else:
                    return SoccerAction((Vector2D(i-p,45)-s.player),Vector2D())
            else:
                if (s.eproche>20):
                    return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize())
                elif s.cannot:
                    return SoccerAction((s.ball+4*s.vball-s.player),Vector2D())
                elif (s.player.x<5*GAME_WIDTH/6 and s.id_team==1 and s.ball.y<GAME_HEIGHT/2)or(s.player.x>GAME_WIDTH/6 and s.id_team==2 and s.ball.y<GAME_HEIGHT/2):
                   return SoccerAction((s.ball-s.player),Vector2D(s.unedeux.x-s.player.x+p,s.unedeux.y-s.player.y).normalize()*3)
                else:
                    return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize())
                
        if s.ide==1:
            if s.milieu:
                  return SoccerAction((Vector2D(s.ball.x,55)-s.player),Vector2D())
            if s.ball.y<GAME_HEIGHT/2:
               return SoccerAction((Vector2D(s.ball.x,50)-s.player),Vector2D())
            else:
               if (s.eproche>20):
                   return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize())
               if s.cannot:
                   return SoccerAction((s.ball+4*s.vball-s.player),Vector2D())
               else:
                   return SoccerAction((s.ball-s.player),Vector2D(s.unedeux.x-s.player.x+p,s.unedeux.y-s.player.y).normalize()*3)
        return SoccerAction((s.ball-s.player),Vector2D(i,GAME_HEIGHT/2)-s.player)
    


class joueur_defenseur(Strategy):
     def __init__(self):
        Strategy.__init__(self, "Defenseur")
        
     def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        #status engagemment
        if (s.milieu):
            if id_team==1:
                return SoccerAction((Vector2D(GAME_WIDTH/5,GAME_HEIGHT/2)-s.player),Vector2D())
            else:
                return SoccerAction((Vector2D(4*GAME_WIDTH/5,GAME_HEIGHT/2)-s.player),Vector2D())

        if id_team==1:
            #prend sa position de base
            if  s.ball.x>2*GAME_WIDTH/5: 
                return SoccerAction((Vector2D(GAME_WIDTH/7,s.aligne_def)-s.player),Vector2D())
            #eloigne l'adversaire en tirant dans les coins
            elif s.ball.x<GAME_WIDTH/5 and s.ball.y<60 and s.ball.y>30 and s.pos_eproche.x<GAME_WIDTH/5 and s.pos_eproche.y>30 and s.pos_eproche.y<60:
                if s.cannot:
                    return SoccerAction((s.ball+(s.norme/10)*s.vball-s.player),Vector2D())
                elif s.pos_eproche.y<(GAME_HEIGHT/2):
                    return SoccerAction((s.ball-s.player),(Vector2D(0,GAME_HEIGHT)).normalize()*3)
                else:
                    return SoccerAction((s.ball-s.player),(Vector2D(0,0).normalize()*3))
            #mode gardien en attendant la balle
            elif s.ball.x<GAME_WIDTH/5 and s.ball.y<30:
                return SoccerAction((Vector2D(s.aligne_def_y,30)-s.player),Vector2D())
            elif s.ball.x<GAME_WIDTH/5 and s.ball.y>60:
                return SoccerAction((Vector2D(s.aligne_def_y,60)-s.player),Vector2D())
            #contre attaque
            else:
                if s.cannot:
                    return SoccerAction((s.ball+(s.norme/10)*s.vball-s.player),Vector2D())
                else:
                    return SoccerAction((s.ball+(s.norme/10)*s.vball-s.player),(sfproche).normalize()*5)
        if id_team==2:
            #prend sa position de base
            if  s.ball.x<3*GAME_WIDTH/5: 
                return SoccerAction((Vector2D(6*GAME_WIDTH/7,s.aligne_def)-s.player),Vector2D())
            #eloigne l'adversaire en tirant dans les coins
            elif s.ball.x>4*GAME_WIDTH/5 and s.ball.y<60 and s.ball.y>30 and s.pos_eproche.x>4*GAME_WIDTH/5 and s.pos_eproche.y>30 and s.pos_eproche.y<60:
                if s.cannot:
                    return SoccerAction((s.ball+(s.norme/10)*s.vball-s.player),Vector2D())
                elif s.pos_eproche.y<(GAME_HEIGHT/2):
                    return SoccerAction((s.ball-s.player),(Vector2D(GAME_WIDTH,GAME_HEIGHT)).normalize()*3)
                else:
                    return SoccerAction((s.ball-s.player),(Vector2D(GAME_WIDTH,0).normalize()*3))
            #mode gardien en attendant la balle
            elif s.ball.x>4*GAME_WIDTH/5 and s.ball.y<30:
                return SoccerAction((Vector2D(s.aligne_def_y,30)-s.player),Vector2D())
            elif s.ball.x>4*GAME_WIDTH/5 and s.ball.y>60:
                return SoccerAction((Vector2D(s.aligne_def_y,60)-s.player),Vector2D())
            #contre attaque
            else:
                if s.norme>PLAYER_RADIUS+BALL_RADIUS:
                    return SoccerAction((s.ball+(s.norme/10)*s.vball-s.player),Vector2D())
                else:
                    return SoccerAction((s.ball+(s.norme/10)*s.vball-s.player),(s.fproche).normalize()*5)
                
                
    
class joueur_defenseur2(Strategy):
     def __init__(self):
        Strategy.__init__(self, "Defenseur2")
        
     def compute_strategy(self, state, id_team, id_player):
        #foncer sur la balle
        s=SuperState(state,id_team,id_player)
        if id_team==1:
            if  s.ball.x>GAME_WIDTH/2-1:  
                return SoccerAction((Vector2D(GAME_WIDTH/3,GAME_HEIGHT/2)-s.player),Vector2D())
            elif(s.ball.x>GAME_WIDTH/2+1 and s.norme<s.fnorme):
                return SoccerAction((s.ball+4*s.vball-s.player),s.fproche)
            else:
                return SoccerAction((Vector2D(5,GAME_HEIGHT/2)-s.player),Vector2D())
        if id_team==2:
            if s.ball.x<GAME_WIDTH/2+1:
                return SoccerAction((Vector2D(2*GAME_WIDTH/3,GAME_HEIGHT/2)-s.player),Vector2D())
            elif (s.ball.x>GAME_WIDTH/2-1 and s.norme<s.fnorme):
                return SoccerAction((s.ball+4*s.vball-s.player),s.fproche)
            else:
                return SoccerAction((Vector2D(GAME_WIDTH-5,GAME_HEIGHT/2)-s.player),Vector2D())
    
    
    
class GoTestStrategy(Strategy):
    def __init__(self,strength = None ):
        Strategy. __init__ ( self , " Go - getter " )
        self.strength = strength
    
    def compute_strategy( self , state , id_team , id_player ):
        s = SuperState ( state , id_team , id_player )
        move = Move(s)
        shoot = Shoot(s)
        return move.to_ball() + shoot.to_goal( self.strength )    
    
    
"""class joueur_goal(Strategy):
     def __init__(self):
        Strategy.__init__(self, "goal")
        
     def compute_strategy(self, state, id_team, id_player):
        #foncer sur la balle
        s=SuperState(state,id_team,id_player)
        
        if id_team==1:
            if  s.ball.x>GAME_WIDTH/2-1:  
                return SoccerAction((Vector2D(8,GAME_HEIGHT/2)-s.player),Vector2D())
        if id_team==2:
            if s.ball.x<GAME_WIDTH/2+1:
                return SoccerAction((Vector2D(GAME_WIDTH-8,GAME_HEIGHT/2)-s.player),Vector2D())
        
        if s.norme<GAME_WIDTH/2:
            if s.norme<BALL_RADIUS: 
                return SoccerAction(Vector2D(s.ball-s.player),Vector2D(s.goal.x,GAME_HEIGHT/2)-s.player)
            else:
                return SoccerAction(s.pgoal,Vector2D())"""