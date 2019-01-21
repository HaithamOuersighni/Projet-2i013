# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu, math


class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        return SoccerAction(Vector2D.create_random(),
                            Vector2D.create_random())
class joueur_fonceur(Strategy):
     def __init__(self):
        Strategy.__init__(self, "Fonceur")
        
     def compute_strategy(self, state, id_team, id_player):
        #foncer sur la balle
        i=0
        if id_team==1:
                i=150
                if math.sqrt((state.ball.position.x-state.player_state(id_team ,id_player).position.x)*(state.ball.position.x-state.player_state(id_team ,id_player).position.x)+(state.ball.position.y-state.player_state(id_team ,id_player).position.y)*(state.ball.position.y-state.player_state(id_team ,id_player).position.y))>0.65:
                    return SoccerAction((state.ball.position-state.player_state(id_team ,id_player).position),
                            Vector2D(0,0))
        return SoccerAction((state.ball.position-state.player_state(id_team ,id_player).position),
                            Vector2D(i,45)-state.player_state(id_team ,id_player).position)


class joueur_defenceur(Strategy):
     def __init__(self):
        Strategy.__init__(self, "Fonceur")
        
     def compute_strategy(self, state, id_team, id_player):
        #foncer sur la balle
        i=0
        
        if id_team==1:
                i=150
                if  state.ball.position.x>75:  
                    return SoccerAction((Vector2D(20,45)-state.player_state(id_team ,id_player).position),
                            Vector2D(0,0))
        if id_team==2:
            if state.ball.position.x<75:
                return SoccerAction((Vector2D(130,45)-state.player_state(id_team ,id_player).position),
                            Vector2D(0,0))
        return SoccerAction(((state.ball.position-state.player_state(id_team ,id_player).position)),
                            Vector2D(i,45)-state.player_state(id_team ,id_player).position)
# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Fonceur", joueur_fonceur())  # Random strategy
team1.add("defenceur", Strategy())
team2.add("defenceur", Strategy())
team2.add("Static", Strategy())   # Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)
