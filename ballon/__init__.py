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
        team.add("alfonse", alfonseur())
    if nb_players == 2:
        team.add("umtiti",joueur_defenseur2())
        team.add("zizou" ,joueur_attaquant())
        
    if nb_players == 4:
        team.add("umtiti", joueur_defenseur())
        team.add("lloris", joueur_goal())
        team.add("zizou",joueur_unedeux())
        team.add("trezeguet",joueur_unedeux())
  
    if nb_players == 3:
        team.add("mbappe",joueur_attaquant())
        team.add("mbappe",joueur_attaquant())
        team.add("pavard",joueur_defenseur2())
        team.add("pavard",joueur_defenseur2())
    return team
