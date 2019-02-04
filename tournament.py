from module import joueur_fonceur, joueur_attaquant, joueur_defenceur
#from module import random_strategy

# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Attaquant", joueur_attaquant())  # Random strategy
team1.add("Defenceur", joueur_defenceur())
team2.add("Defenceur", joueur_defenceur())
team2.add("Fonceur",  joueur_fonceur()) # Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match