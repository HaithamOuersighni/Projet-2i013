#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 16:20:22 2019

@author: 3670841
"""
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu, math
from soccersimulator import settings 
from ballon.code_alea import GoalSearch
from ballon.random_strategy import GoTestStrategy

strength=[0.1,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6]
gs=GoalSearch(GoTestStrategy(),{'strength':strength})
gs.start()

