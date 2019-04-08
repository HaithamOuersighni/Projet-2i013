# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, math
from soccersimulator import VolleySimulation, volley_show_simu
from tools import *

class Attaque(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        if id_team==1:
            if s.ball==s.player:
                return SoccerAction((s.ball-s.player),((Vector2D(2*GAME_WIDTH/5,GAME_HEIGHT/2)-s.player).normalize()*3))
            elif s.ball.x>2*GAME_WIDTH/5 and s.ball.x<GAME_WIDTH/2:
                if s.cannot:
                    return SoccerAction((s.ball-s.player), Vector2D())
                
                elif s.pos_eproche.x<3*GAME_WIDTH/4 and s.pos_eproche.y<GAME_HEIGHT/2: #adv coin bas gauche
                    return SoccerAction((s.ball-s.player), (Vector2D(GAME_WIDTH-5,GAME_HEIGHT-15)-s.player).normalize()*6)
                    
                elif s.pos_eproche.x>3*GAME_WIDTH/4 and s.pos_eproche.y<GAME_HEIGHT/2: #adv coin bas droit
                    return SoccerAction((s.ball-s.player), (Vector2D((GAME_WIDTH/2)+10,GAME_HEIGHT-20)-s.player).normalize()*2)
                    
                elif s.pos_eproche.x<3*GAME_WIDTH/4 and s.pos_eproche.y>GAME_HEIGHT/2:#adv coin haut gauche
                    return SoccerAction((s.ball-s.player), (Vector2D(GAME_WIDTH-5,15)-s.player).normalize()*6)
                    
                else:#adv coin haut droit
                    return SoccerAction((s.ball-s.player), (Vector2D((GAME_WIDTH/2)+10,20)-s.player).normalize()*2)
            else:
                return SoccerAction(Vector2D(2*GAME_WIDTH/5,GAME_HEIGHT/2)-s.player)
        else:
            if s.ball==s.player:
                return SoccerAction((s.ball-s.player),((Vector2D(3*GAME_WIDTH/5,GAME_HEIGHT/2)-s.player).normalize()*3))
            elif s.ball.x>GAME_WIDTH/2 and s.ball.x<3*GAME_WIDTH/5:
                if s.cannot:
                    return SoccerAction((s.ball-s.player), Vector2D())
                
                elif s.pos_eproche.x<GAME_WIDTH/4 and s.pos_eproche.y<GAME_HEIGHT/2: #adv coin bas gauche
                    return SoccerAction((s.ball-s.player), (Vector2D((GAME_WIDTH/2)-10,GAME_HEIGHT-20)-s.player).normalize()*2)
                    
                elif s.pos_eproche.x>3*GAME_WIDTH/4 and s.pos_eproche.y<GAME_HEIGHT/2: #adv coin bas droit
                    return SoccerAction((s.ball-s.player), (Vector2D(5,GAME_HEIGHT-15)-s.player).normalize()*6)
                    
                elif s.pos_eproche.x<3*GAME_WIDTH/4 and s.pos_eproche.y>GAME_HEIGHT/2:#adv coin haut gauche
                    return SoccerAction((s.ball-s.player), (Vector2D((GAME_WIDTH/2)-10,20)-s.player).normalize()*2)
                    
                else:#adv coin haut droit
                    return SoccerAction((s.ball-s.player), (Vector2D(15,15)-s.player).normalize()*6)
            else:
                return SoccerAction(Vector2D(3*GAME_WIDTH/5,GAME_HEIGHT/2)-s.player)
            
            
class Defenseur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        if id_team==1:
            if s.ball.x<2*GAME_WIDTH/5:
                if s.cannot:
                    return SoccerAction((s.ball-s.player), Vector2D())
                else:
                    return SoccerAction((s.ball-s.player),(s.pos2v2-s.player).normalize()*2)
            else:   
                return SoccerAction(Vector2D(GAME_WIDTH/5,s.ball.y)-s.player,Vector2D())
        else:
            if s.ball.x>3*GAME_WIDTH/5:
                if s.cannot:
                    return SoccerAction((s.ball-s.player), Vector2D())
                else:
                    return SoccerAction((s.ball-s.player),(s.pos2v2-s.player).normalize()*2)
            else:   
                return SoccerAction(Vector2D(4*GAME_WIDTH/5,s.ball.y)-s.player,Vector2D())




# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("atk", Attaque())  # Random strategy
team2.add("atk", Attaque())   # Random strategy
team1.add("def", Defenseur())  # Random strategy
team2.add("def", Defenseur())   # Random strategy
# Create a match
simu = VolleySimulation(team1, team2)

# Simulate and display the match
volley_show_simu(simu)