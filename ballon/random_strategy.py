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
        if s.ball.x==GAME_WIDTH/2 and s.ball.y==GAME_HEIGHT/2:
                return SoccerAction(Vector2D(),Vector2D(i,GAME_HEIGHT/2)-s.player)
        if s.norme>PLAYER_RADIUS+BALL_RADIUS:
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
        if s.norme>PLAYER_RADIUS+BALL_RADIUS:
            return SoccerAction((s.ball-s.player),Vector2D())
        return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2)-s.player)*4)
    
class alfonseur(Strategy):
    def __init__(self):
        Strategy.__init__(self,"alfonseur")
        
    def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        i=s.goal.x
        if id_team==1:
            if s.ball.x==GAME_WIDTH/2 and s.ball.y==GAME_HEIGHT/2:
                return SoccerAction(Vector2D(GAME_WIDTH/10-s.player.x,GAME_HEIGHT/2-s.player.y),Vector2D())
            elif s.ball.x<=4*GAME_WIDTH/5 :
                if s.norme<=PLAYER_RADIUS+BALL_RADIUS:
                    return SoccerAction(Vector2D(),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize())
            else:
                if s.norme<=PLAYER_RADIUS+BALL_RADIUS:
                    return SoccerAction(Vector2D(),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize()*6)
            return SoccerAction((s.ball+1*s.vball-s.player),Vector2D())
        else:
            if s.ball.x==GAME_WIDTH/2 and s.ball.y==GAME_HEIGHT/2:
                return SoccerAction(Vector2D(GAME_WIDTH-s.player.x,GAME_HEIGHT/2-s.player.y),Vector2D())
            elif s.ball.x>=GAME_WIDTH/9 :
                if s.norme<=PLAYER_RADIUS+BALL_RADIUS:
                    if state.player_state(1,0).position.x<s.player.x:
                        return SoccerAction(Vector2D(),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize()*6)
                    return SoccerAction(Vector2D(),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize())
            else:
                if s.norme<=PLAYER_RADIUS+BALL_RADIUS:
                    return SoccerAction(Vector2D(),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize()*6)
            return SoccerAction((s.ball+1*s.vball-s.player),Vector2D())
    
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
        if s.norme>PLAYER_RADIUS+BALL_RADIUS:
            return SoccerAction((s.ball+4*s.vball-s.player),Vector2D())
        if (s.player.x<6*GAME_WIDTH/7 and s.id_team==1)or(s.player.x>GAME_WIDTH/7 and s.id_team==2)or (s.cnorme>s.gnorme):
            return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize())
        else:
            return SoccerAction((s.ball-s.player),Vector2D(i,GAME_HEIGHT/2)-s.player)
        
        
class joueur_unedeux(Strategy):
     def __init__(self):
        Strategy.__init__(self, "Attaquant")
        
     def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        i=s.goal.x
        if id_team==2: 
           if  s.ball.x>GAME_WIDTH/100*70:  
                return SoccerAction((Vector2D(GAME_WIDTH/100*65,s.ball.y)-s.player),Vector2D())
        if id_team==1:
            if s.ball.x<GAME_WIDTH/100*30:
                return SoccerAction((Vector2D(GAME_WIDTH/100*35,s.ball.y)-s.player),Vector2D())
        if s.norme>SHORT_RANGE:
            return SoccerAction((s.ball+4*s.vball-s.player),Vector2D())
        if s.norme>PLAYER_RADIUS+BALL_RADIUS:
            return SoccerAction((s.ball+4*s.vball-s.player),Vector2D())
        if (s.player.x<5*GAME_WIDTH/6 and s.id_team==1)or(s.player.x>GAME_WIDTH/6 and s.id_team==2):
            return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize())
        else:
            return SoccerAction((s.ball-s.player),Vector2D(i,GAME_HEIGHT/2)-s.player)
    


class joueur_defenseur(Strategy):
     def __init__(self):
        Strategy.__init__(self, "Defenseur")
        
     def compute_strategy(self, state, id_team, id_player):
        #foncer sur la balle
        s=SuperState(state,id_team,id_player)
        if (s.ball.x==GAME_WIDTH/2 and s.ball.y==GAME_HEIGHT/2):
            if id_team==1:
                return SoccerAction((Vector2D(GAME_WIDTH/5,GAME_HEIGHT/2)-s.player),Vector2D())
            else:
                return SoccerAction((Vector2D(4*GAME_WIDTH/5,GAME_HEIGHT/2)-s.player),Vector2D())

        if id_team==1:
            #prend sa position de base
            if  s.ball.x>2*GAME_WIDTH/5:# s.fnorme<s.enorme:  
                return SoccerAction((Vector2D(GAME_WIDTH/7,s.aligne_def)-s.player),Vector2D())
            #eloigne l'adversaire en tirant dans les coins
            elif s.ball.x<GAME_WIDTH/5 and s.ball.y<55 and s.ball.y>35 and s.pos_eproche.x<GAME_WIDTH/5 and s.pos_eproche.y>35 and s.pos_eproche.y<55:
                if s.norme>PLAYER_RADIUS+BALL_RADIUS:
                    return SoccerAction((s.ball+2*s.vball-s.player),Vector2D())
                if s.pos_eproche.y<(GAME_HEIGHT/2):
                    return SoccerAction((s.ball+4*s.vball-s.player),(Vector2D(0,GAME_HEIGHT)).normalize()*3)
                else:
                    return SoccerAction((s.ball+4*s.vball-s.player),(Vector2D(0,0).normalize()*3))
            #mode gardien en attendant la balle
            elif s.ball.x<GAME_WIDTH/5 and s.ball.y<35:
                return SoccerAction((Vector2D(s.aligne_def_y,35)-s.player),Vector2D())
            elif s.ball.x<GAME_WIDTH/5 and s.ball.y>55:
                return SoccerAction((Vector2D(s.aligne_def_y,55)-s.player),Vector2D())
            #contre attaque
            elif elif s.ball.x<GAME_WIDTH/5 and s.ball.y<55 and s.ball.y>35 and s.pos_eproche.x<GAME_WIDTH/5 and (s.pos_eproche.y<35 or s.pos_eproche.y>55):
                
        if id_team==2:
            if s.ball.x<3*GAME_WIDTH/5:# s.fnorme<s.enorme:
                return SoccerAction((Vector2D(6*GAME_WIDTH/7,s.aligne_def)-s.player),Vector2D())
            
        if s.norme>PLAYER_RADIUS+BALL_RADIUS:
            return SoccerAction((s.ball+2*s.vball-s.player),Vector2D())
        return SoccerAction((s.ball+4*s.vball-s.player),(s.fproche).normalize()*4)
    
    
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