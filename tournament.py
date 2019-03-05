from ballon import joueur_fonceur, joueur_attaquant, joueur_defenseur2 ,joueur_defenseur, joueur_fonceur2,alfonseur,joueur_unedeux, get_team
from soccersimulator import SoccerTeam

"""def get_team ( nb_players ):
    team = SoccerTeam(name=" ulysse's Team ")
    if nb_players == 1: 
        team.add("Fonceur" , joueur_fonceur())
    if nb_players == 2:
        team.add("defenseur",joueur_defenseur())
        team.add("attaquant",joueur_attaquant())
    if nb_players == 3:
        team.add("attaquant",joueur_fonceur2())
    return team """


if __name__ == '__main__':
    from soccersimulator import Simulation , show_simu

    # Check teams with 1 player and 2 players
    team1 = get_team(1)
    team2 = get_team(4)

    # Create a match
    simu = Simulation(team1,team2)

    # Simulate and display the match
    show_simu(simu)