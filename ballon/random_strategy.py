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

#fonceur de base
class joueur_fonceur(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Fonceur2")
        
    def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        i=s.goal.x
        if s.cannot:
            return SoccerAction((s.ball-s.player),Vector2D())
        return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2)-s.player)*4)

# alfonse joueur 1vs1
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
            
#attaquant 2v2 ameliorer qui met des crocher           
class joueur_attaquant(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaquant")
        
    def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        i=s.goal.x
        if id_team==2: 
            if  s.ball.x>3*GAME_WIDTH/4:
                if s.possede2v2 and s.abnorme2v2:
                    if s.cannot:
                        return SoccerAction((s.ball-s.player),Vector2D())
                    else:
                        return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize())
                elif s.ball.y<GAME_HEIGHT/2:
                    return SoccerAction((Vector2D(3*GAME_WIDTH/4,s.ball.y+10)-s.player),Vector2D())
                return SoccerAction((Vector2D(3*GAME_WIDTH/4,s.ball.y-10)-s.player),Vector2D())
            elif s.cannot:
                return SoccerAction((s.ball+4*s.vball-s.player),Vector2D())
            elif s.ball.x<=GAME_WIDTH/5:
                return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize()*5)
            elif s.eproche2v2:
                if s.player.y>GAME_HEIGHT/2:
                    return SoccerAction((s.ball-s.player),(Vector2D(s.player.x-10,s.player.y+15)-s.player).normalize())
                else:
                    return SoccerAction((s.ball-s.player),(Vector2D(s.player.x-10,s.player.y-15)-s.player).normalize())
            else:
                return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize()*0.8)
            
        elif id_team==1:
            if s.ball.x<GAME_WIDTH/4:
                if s.possede2v2 and s.abnorme2v2:
                    if s.cannot:
                        return SoccerAction((s.ball-s.player),Vector2D())
                    else:
                        return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize())
                elif s.ball.y<GAME_HEIGHT/2:
                    return SoccerAction((Vector2D(GAME_WIDTH/4,s.ball.y+10)-s.player),Vector2D())
                return SoccerAction((Vector2D(GAME_WIDTH/4,s.ball.y-10)-s.player),Vector2D())
            elif s.cannot:
               return SoccerAction((s.ball+4*s.vball-s.player),Vector2D())
            elif s.ball.x>=4*GAME_WIDTH/5:
                return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize()*5)
            elif s.eproche2v2:
                if s.player.y>GAME_HEIGHT/2:
                    return SoccerAction((s.ball-s.player),(Vector2D(s.player.x+10,s.player.y+15)-s.player).normalize())
                else:
                    return SoccerAction((s.ball-s.player),(Vector2D(s.player.x+10,s.player.y-15)-s.player).normalize())
            else:
                return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize())
     

#attaquant 4v4 v2 
class attaquant1(Strategy):
     def __init__(self):
        Strategy.__init__(self, "Attaquant")
        
     def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        i=s.goal.x
        if id_team==1:
            if s.milieu:
                return SoccerAction((Vector2D(s.ball.x,80)-s.player),Vector2D())
            elif s.abnorme:
                if s.cannot:
                    return SoccerAction((s.ball+4*s.vball-s.player),Vector2D())
                elif s.player.x>3*GAME_WIDTH/4:
                    if s.ball.y>GAME_HEIGHT/4 and s.ball.y<3*GAME_HEIGHT/4:
                        return SoccerAction((s.ball-s.player),Vector2D(i,GAME_HEIGHT/2)-s.player)
                    else:
                        return SoccerAction((s.ball-s.player),(s.unedeux-s.player))
                elif s.player.x>3*GAME_WIDTH/5:
                    if s.player.y<GAME_HEIGHT/2:
                        return SoccerAction((s.ball-s.player),Vector2D(s.player.x+10,s.player.y+10))
                    else:
                        return SoccerAction((s.ball-s.player),Vector2D(s.player.x+10,s.player.y-10))
                    #if s.player.y<GAME_HEIGHT/2:
                    #    return SoccerAction((s.ball-s.player),Vector2D(s.player.x+10,s.player.y+10)-s.player)
                    #else:
                    #    return SoccerAction((s.ball-s.player),Vector2D(s.player.x+10,s.player.y-10)-s.player)
                else:
                    return SoccerAction((s.ball-s.player),Vector2D(s.unedeux.x+15-s.player.x,s.unedeux.y-s.player.y))
            elif s.possede:
                return SoccerAction(Vector2D(4*GAME_WIDTH/5,GAME_HEIGHT/2)-s.player,Vector2D())
            else:
                if(s.ball.x>GAME_WIDTH/2):
                    return SoccerAction(Vector2D(4*GAME_WIDTH/5,3*GAME_HEIGHT/5)-s.player,Vector2D())
                else:
                    return SoccerAction(Vector2D(GAME_WIDTH/2,GAME_HEIGHT/4)-s.player,Vector2D())
        else:
            if s.milieu:
                return SoccerAction((Vector2D(s.ball.x,80)-s.player),Vector2D())
            elif s.abnorme:
                if s.cannot:
                    return SoccerAction((s.ball+4*s.vball-s.player),Vector2D())
                elif s.player.x<GAME_WIDTH/4:
                    if s.ball.y>GAME_HEIGHT/4 and s.ball.y<3*GAME_HEIGHT/4:
                        return SoccerAction((s.ball-s.player),Vector2D(i,GAME_HEIGHT/2)-s.player)
                    else:
                        return SoccerAction((s.ball-s.player),(s.unedeux-s.player))
                elif s.player.x<2*GAME_WIDTH/5:
                    if s.player.y<GAME_HEIGHT/2:
                        return SoccerAction((s.ball-s.player),(Vector2D(s.player.x-10,s.player.y+10)-s.player).normalize())
                    else:
                        return SoccerAction((s.ball-s.player),(Vector2D(s.player.x-10,s.player.y-10)-s.player).normalize())
                else:
                    return SoccerAction((s.ball-s.player),Vector2D(s.unedeux.x-15-s.player.x,s.unedeux.y-s.player.y))
            elif s.possede:
                return SoccerAction(Vector2D(GAME_WIDTH/5,GAME_HEIGHT/2)-s.player,Vector2D())
            else:
                if(s.ball.x<GAME_WIDTH/2):
                    return SoccerAction(Vector2D(GAME_WIDTH/5,3*GAME_HEIGHT/5)-s.player,Vector2D())
                else:
                    return SoccerAction(Vector2D(GAME_WIDTH/2,GAME_HEIGHT/4)-s.player,Vector2D())
#attanquant 4v4 v2 bis
class attaquant2(Strategy):
     def __init__(self):
        Strategy.__init__(self, "Attaquant")
        
     def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        i=s.goal.x
        if id_team==1:
            if s.milieu:
                return SoccerAction((s.ball-s.player),Vector2D(s.unedeux.x-s.player.x,s.unedeux.y-s.player.y).normalize()*2)
            elif s.abnorme:
                if s.cannot:
                    return SoccerAction((s.ball+4*s.vball-s.player),Vector2D())
                elif s.player.x>3*GAME_WIDTH/4:
                    if s.ball.y>GAME_HEIGHT/4 and s.ball.y<3*GAME_HEIGHT/4:
                        return SoccerAction((s.ball-s.player),Vector2D(i,GAME_HEIGHT/2)-s.player)
                    else:
                        return SoccerAction((s.ball-s.player),(s.unedeux-s.player))
                else:
                    return SoccerAction((s.ball-s.player),Vector2D(s.unedeux.x+10,s.unedeux.y)-s.player)
            elif s.possede:
                if s.ball.x<GAME_WIDTH/2:
                    return SoccerAction(Vector2D(GAME_WIDTH/2,GAME_HEIGHT/4)-s.player,Vector2D())
                else:
                    return SoccerAction(Vector2D(3*GAME_WIDTH/4,GAME_HEIGHT/2)-s.player,Vector2D())
            else:
                if(s.ball.x>GAME_WIDTH/2):
                    return SoccerAction(Vector2D(4*GAME_WIDTH/5,2*GAME_HEIGHT/5)-s.player,Vector2D())
                else:
                    return SoccerAction(Vector2D(GAME_WIDTH/2,3*GAME_HEIGHT/4)-s.player,Vector2D())
        else:
            if s.milieu:
                return SoccerAction((s.ball-s.player),Vector2D(s.unedeux.x-s.player.x,s.unedeux.y-s.player.y).normalize()*2)
            elif s.abnorme:
                if s.cannot:
                    return SoccerAction((s.ball+4*s.vball-s.player),Vector2D())
                elif s.player.x<GAME_WIDTH/4:
                    if s.ball.y>GAME_HEIGHT/4 and s.ball.y<3*GAME_HEIGHT/4:
                        return SoccerAction((s.ball-s.player),Vector2D(i,GAME_HEIGHT/2)-s.player)
                    else:
                        return SoccerAction((s.ball-s.player),(s.unedeux-s.player))
                else:
                    return SoccerAction((s.ball-s.player),Vector2D(s.unedeux.x+10,s.unedeux.y)-s.player)
            elif s.possede:
                if s.ball.x>GAME_WIDTH/2:
                    return SoccerAction(Vector2D(GAME_WIDTH/2,GAME_HEIGHT/4)-s.player,Vector2D())
                else:
                    return SoccerAction(Vector2D(GAME_WIDTH/4,GAME_HEIGHT/2)-s.player,Vector2D())
            else:
                if(s.ball.x<GAME_WIDTH/2):
                    return SoccerAction(Vector2D(GAME_WIDTH/5,2*GAME_HEIGHT/5)-s.player,Vector2D())
                else:
                    return SoccerAction(Vector2D(GAME_WIDTH/2,3*GAME_HEIGHT/4)-s.player,Vector2D())
     
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
        if s.ide==2:
            if s.milieu:
                return SoccerAction((s.ball-s.player),Vector2D(s.unedeux.x-s.player.x,s.unedeux.y-s.player.y).normalize()*2)
            elif s.ball.x<GAME_WIDTH/3 and id_team==1:
                return SoccerAction(Vector2D(GAME_WIDTH/3,2*GAME_HEIGHT/5)-s.player,Vector2D())
            elif s.ball.x>2*GAME_WIDTH/3 and id_team==2:
                return SoccerAction(Vector2D(2*GAME_WIDTH/3,2*GAME_HEIGHT/5)-s.player,Vector2D())
            
            elif  s.ball.y>GAME_HEIGHT/2:
                if(s.ball.x<(5*GAME_WIDTH/6)-15 and id_team==1) or (s.ball.x>(GAME_WIDTH/6)+15 and id_team==2):
                    return SoccerAction((Vector2D(s.ball.x,35)-s.player),Vector2D())
                else:
                    return SoccerAction((Vector2D(i-p,GAME_HEIGHT/2)-s.player),Vector2D())
            else:
                if (s.eproche>20):
                    return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize())
                elif s.cannot:
                    return SoccerAction((s.ball+4*s.vball-s.player),Vector2D())
                elif (s.player.x<5*GAME_WIDTH/6 and s.id_team==1)or(s.player.x>GAME_WIDTH/6 and s.id_team==2):
                   return SoccerAction((s.ball-s.player),Vector2D(s.unedeux.x-s.player.x+p,s.unedeux.y-s.player.y).normalize()*3)
                else:
                    return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize())
                
        if s.ide==3:
            if s.milieu:
                  return SoccerAction((Vector2D(s.ball.x,80)-s.player),Vector2D())
            
            elif s.ball.x<GAME_WIDTH/3 and id_team==1:
                return SoccerAction(Vector2D(GAME_WIDTH/3,3*GAME_HEIGHT/5)-s.player,Vector2D())
            elif s.ball.x>2*GAME_WIDTH/3 and id_team==2:
                return SoccerAction(Vector2D(2*GAME_WIDTH/3,3*GAME_HEIGHT/5)-s.player,Vector2D())
            
            elif s.ball.y<GAME_HEIGHT/3:
               return SoccerAction((Vector2D(s.ball.x,50)-s.player),Vector2D())
            else:
               if (s.eproche>20):
                   return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize())
               elif s.cannot:
                   return SoccerAction((s.ball+5*s.vball-s.player),Vector2D())
               else:
                   return SoccerAction((s.ball-s.player),Vector2D(s.unedeux.x-s.player.x+p,s.unedeux.y-s.player.y).normalize()*3)
        return SoccerAction((s.ball-s.player),Vector2D(i,GAME_HEIGHT/2)-s.player)
    

#joueur_defenceur ameliorer 2v2
class joueur_defenseur2(Strategy):
     def __init__(self):
        Strategy.__init__(self, "Defenseur ameliorer")

     def compute_strategy(self, state, id_team, id_player):
        #foncer sur la balle
        s=SuperState(state,id_team,id_player)
        if id_team==1:
            if s.ball.x>GAME_WIDTH/3:
                return SoccerAction((Vector2D(GAME_WIDTH/4,s.aligne_def)-s.player),Vector2D())
            else:
                if s.cannot:
                    return SoccerAction((s.ball+2*s.vball-s.player),Vector2D())
                else:
                    return SoccerAction((s.ball-s.player),s.allier2v2.normalize()*3)
        else:
             if s.ball.x<2*GAME_WIDTH/3:
                return SoccerAction((Vector2D(3*GAME_WIDTH/4,s.aligne_def)-s.player),Vector2D())
             else:
                if s.cannot:
                    return SoccerAction((s.ball+2*s.vball-s.player),Vector2D())
                else:
                    return SoccerAction((s.ball-s.player),s.allier2v2.normalize()*3)   


# goal pour le 4v4
class joueur_goal(Strategy):
    def __init__(self):
        Strategy.__init__(self, "gardien")
        
    def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        if id_team==1:
            if s.ball.x>GAME_WIDTH/3:
                return SoccerAction(Vector2D(GAME_WIDTH/20,s.aligne_def)-s.player,Vector2D())
            elif s.ball.x<GAME_WIDTH/2 and s.norme<s.enorme and s.norme<=s.fbnorme:
                if s.cannot:
                    return SoccerAction((s.ball+2*s.vball-s.player),Vector2D())
                else:
                    return SoccerAction((s.ball-s.player),s.fproche.normalize()*3)
            else:
                if s.norme>s.enorme and s.ball.x>GAME_WIDTH/9:
                    return SoccerAction(Vector2D(GAME_WIDTH/10,s.aligne_def)-s.player,Vector2D())
                else:
                    if s.cannot:
                        return SoccerAction((s.ball+2*s.vball-s.player),Vector2D())
                    else:
                        return SoccerAction((s.ball-s.player),s.fproche.normalize()*3)
        else:
            if s.ball.x<2*GAME_WIDTH/3:
                return SoccerAction(Vector2D(9*GAME_WIDTH/10,s.aligne_def)-s.player,Vector2D())
            elif s.ball.x>GAME_WIDTH/2 and s.norme<s.enorme and s.norme<=s.fbnorme:
                if s.cannot:
                    return SoccerAction((s.ball+2*s.vball-s.player),Vector2D())
                else:
                    return SoccerAction((s.ball-s.player),s.fproche.normalize()*3)
            else:
                if s.norme>s.enorme and s.ball.x<8*GAME_WIDTH/9:
                    return SoccerAction(Vector2D(19*GAME_WIDTH/20,s.aligne_def)-s.player,Vector2D())
                else:
                    if s.cannot:
                        return SoccerAction((s.ball+2*s.vball-s.player),Vector2D())
                    else:
                        return SoccerAction((s.ball-s.player),s.fproche.normalize()*3)
           
#defenseur 4VS4 v2 test 
class joueur_defenseur(Strategy):
     def __init__(self):
        Strategy.__init__(self, "Defenseur 4vs4 v2")

     def compute_strategy(self, state, id_team, id_player):
        #foncer sur la balle
        s=SuperState(state,id_team,id_player)
        if id_team==1:
            if s.ball.x>GAME_WIDTH/2+1:
                return SoccerAction((Vector2D(GAME_WIDTH/3,s.aligne_def)-s.player),Vector2D())
            elif s.distgb>s.norme:                    
                if s.cannot:
                    return SoccerAction((s.ball-s.player),Vector2D())
                else:
                    return SoccerAction((s.ball-s.player),(s.fproche).normalize()*3)
            else:
                return SoccerAction((Vector2D(GAME_WIDTH/4,s.ball.y)-s.player),Vector2D())
        else:
            if s.ball.x<GAME_WIDTH/2:
                return SoccerAction((Vector2D(2*GAME_WIDTH/3,s.aligne_def)-s.player),Vector2D())
            elif s.distgb>s.norme:                    
                if s.cannot:
                    return SoccerAction((s.ball-s.player),Vector2D())
                else:
                    return SoccerAction((s.ball-s.player),(s.fproche).normalize()*3)
            else:
                return SoccerAction((Vector2D(3*GAME_WIDTH/4,s.ball.y)-s.player),Vector2D())
           
    
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