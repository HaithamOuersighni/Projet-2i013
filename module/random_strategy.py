# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu, math
from soccersimulator import settings 
from .tools import SuperState
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
        Strategy.__init__(self,"Fonceur")
        
    def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        i=s.goal.x
        if s.norme>BALL_RADIUS:
            return SoccerAction((s.ball-s.player),Vector2D())
        return SoccerAction((s.ball-s.player),Vector2D(i,GAME_HEIGHT/2)-s.player)
    
class joueur_attaquant(Strategy):
     def __init__(self):
        Strategy.__init__(self, "Attaquant")
        
     def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        i=s.goal.x
        if id_team==2: 
           if  s.ball.x>GAME_WIDTH/100*70:  
                return SoccerAction((Vector2D(GAME_WIDTH/100*65,GAME_HEIGHT/2)-s.player),Vector2D())
        if id_team==1:
            if s.ball.x<GAME_WIDTH/100*30:
                return SoccerAction((Vector2D(GAME_WIDTH/100*35,GAME_HEIGHT/2)-s.player),Vector2D())
        if s.norme>SHORT_RANGE:
            return SoccerAction((s.ball+s.vball*10-s.player).normalize()*maxPlayerAcceleration,Vector2D())
        if s.norme>BALL_RADIUS:
            return SoccerAction((s.ball-s.player),Vector2D())
        if (s.player.x<GAME_WIDTH/2 and s.id_team==1)or(s.player.x>GAME_WIDTH/2 and s.id_team==2):
            if s.eproche<SHORT_RANGE:
                return SoccerAction((s.ball-s.player),(s.fproche).normalize()*2)
            return SoccerAction((s.ball-s.player),(Vector2D(i,GAME_HEIGHT/2)-s.player).normalize()*2)
        else:
            return SoccerAction((s.ball-s.player),Vector2D(i,GAME_HEIGHT/2)-s.player)

class joueur_defenceur(Strategy):
     def __init__(self):
        Strategy.__init__(self, "Defenceur")
        
     def compute_strategy(self, state, id_team, id_player):
        #foncer sur la balle
        s=SuperState(state,id_team,id_player)
        if id_team==1:
                if  s.ball.x>GAME_WIDTH/2-1:  
                    return SoccerAction((Vector2D(GAME_WIDTH/5,GAME_HEIGHT/2)-s.player),Vector2D())
        if id_team==2:
            if s.ball.x<GAME_WIDTH/2+1:
                return SoccerAction((Vector2D(4*GAME_WIDTH/5,GAME_HEIGHT/2)-s.player),Vector2D())
        return SoccerAction((s.ball+4*s.vball-s.player),Vector2D(s.goal.x,GAME_HEIGHT/2)-s.player)