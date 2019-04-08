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
            if s.ball.x<GAME_WIDTH/2:
                if s.cannot:
                    return SoccerAction((s.ball-s.player), Vector2D())
                elif s.enemy1v1.x<3*GAME_WIDTH/4 and s.enemy4v4.y<GAME_HEIGHT/2: #adv coin bas gauche
                    if s.ball.x<GAME_HEIGHT/3:
                        return SoccerAction((s.ball-s.player), (Vector2D(2*GAME_WIDTH/5,2*GAME_HEIGHT/3)-s.player))
                    else:
                        return SoccerAction((s.ball-s.player), (Vector2D(GAME_WIDTH-5,GAME_HEIGHT-5)-s.player))
                    
                elif s.enemy1v1.x>3*GAME_WIDTH/4 and s.enemy4v4.y<GAME_HEIGHT/2: #adv coin bas droit
                        return SoccerAction((s.ball-s.player), (Vector2D((GAME_WIDTH/2)+5,(GAME_HEIGHT/2)-5)-s.player))
                    
                elif s.enemy1v1.x<3*GAME_WIDTH/4 and s.enemy4v4.y>GAME_HEIGHT/2:#adv coin haut gauche
                    if s.ball.x<GAME_HEIGHT/3:
                        return SoccerAction((s.ball-s.player), (Vector2D(2*GAME_WIDTH/5,GAME_HEIGHT/3)-s.player))
                    else:
                        return SoccerAction((s.ball-s.player), (Vector2D(GAME_WIDTH-5,5)-s.player))
                    
                else:#adv coin haut droit
                    if s.ball.x<GAME_HEIGHT/3:
                        return SoccerAction((s.ball-s.player), (Vector2D(2*GAME_WIDTH/5,2*GAME_HEIGHT/3)-s.player))
                    else:
                        return SoccerAction((s.ball-s.player), (Vector2D(GAME_WIDTH,5*GAME_HEIGHT/6)-s.player))
            else:   
                return SoccerAction(Vector2D(GAME_WIDTH/4,GAME_HEIGHT/2)-s.player,Vector2D())
        else:
            if s.ball.x>GAME_WIDTH/2:
                if s.cannot:
                    return SoccerAction((s.ball-s.player), Vector2D())
                else:
                    return SoccerAction((s.ball-s.player), (Vector2D(GAME_WIDTH/4,GAME_HEIGHT/2)-s.player))
            else:
                return SoccerAction(Vector2D(3*GAME_WIDTH/4,GAME_HEIGHT/2)-s.player,Vector2D())




# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Player 1", Echauffement())  # Random strategy
team2.add("Player 2", Echauffement())   # Random strategy

# Create a match
simu = VolleySimulation(team1, team2)

# Simulate and display the match
volley_show_simu(simu)