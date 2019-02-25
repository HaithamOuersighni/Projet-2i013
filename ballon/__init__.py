#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 17:48:05 2019

@author: 3670841
"""

from .random_strategy import *

def get_team ( nb_players ):
    team = SoccerTeam(name=" HUP's Team ")
    if nb_players == 1: 
        team.add("fonceur", joueur_fonceur2())
    if nb_players == 2:
        team.add("defenseur",joueur_defenseur())
        team.add("attaquant",joueur_attaquant())
    if nb_players == 3:
        team.add("defenseur",joueur_fonceur())
        team.add("attaquant",joueur_attaquant())
    if nb_players == 4:
        team.add("neymar" , joueur_fonceur())
    return team