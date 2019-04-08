# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, math
from soccersimulator import VolleySimulation, volley_show_simu
from tools import *

class Echauffement(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        s=SuperState(state,id_team,id_player)
        if id_team==1:
            if s.ball.x<GAME_WIDTH/2:
                if s.cannot:
                    return SoccerAction((s.ball-s.player), Vector2D())
                else:
                    return SoccerAction((s.ball-s.player), (Vector2D(3*GAME_WIDTH/4,GAME_HEIGHT/2)-s.player))
        else:
            if s.ball.x>GAME_WIDTH/2:
                if s.cannot:
                    return SoccerAction((s.ball-s.player), Vector2D())
                else:
                    return SoccerAction((s.ball-s.player), (Vector2D(GAME_WIDTH/4,GAME_HEIGHT/2)-s.player))

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
