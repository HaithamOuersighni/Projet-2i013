#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:05:58 2019

@author: 3700351
"""
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu, math
from soccersimulator.settings import *

class SuperState(object):
        def __init__(self,state,id_team,id_player):
            self.state = state
            self.id_team = id_team
            self.id_player = id_player
        @property
        def ball(self):
            return self.state.ball.position
        @property
        def vball(self):
            return self.state.ball.vitesse
        @property
        def player(self):
            return self.state.player_state(self.id_team, self.id_player).position
        @property
        def goal(self):
            return Vector2D((self.id_team%2)*GAME_WIDTH,GAME_HEIGHT/2)
        @property
        def norme(self):
            return math.sqrt((self.ball.x-self.player.x)**2+(self.ball.y-self.player.y)**2)
        @property
        def eproche(self):
            i=0
            n=len(self.state.players)/2
            v=Vector2D(GAME_WIDTH,GAME_HEIGHT)
            while i<n:
                if (math.sqrt((self.state.player_state(self.id_team%2+1,i).position.x-self.player.x)**2+(self.state.player_state(self.id_team%2+1,i).position.y-self.player.y)**2)<math.sqrt(v.x**2+v.y**2)):
                    v=Vector2D(self.state.player_state(self.id_team%2+1,i).position.x-self.player.x,self.state.player_state(self.id_team%2+1,i).position.y-self.player.y)
                i=i+1
            return v.x**2+v.y**2
        @property
        def fproche(self):
            i=0
            n=len(self.state.players)/2
            v=Vector2D(GAME_WIDTH,GAME_HEIGHT)
            while i<n:
                if 0<(math.sqrt((self.state.player_state(self.id_team,i).position.x-self.player.x)**2+(self.state.player_state(self.id_team,i).position.y-self.player.y)**2) and (math.sqrt((self.state.player_state(self.id_team,i).position.x-self.player.x)**2+(self.state.player_state(self.id_team,i).position.y-self.player.y)**2)<math.sqrt(v.x**2+v.y**2))):
                    v=Vector2D(self.state.player_state(self.id_team,i).position.x-self.player.x,self.state.player_state(self.id_team,i).position.y-self.player.y)
                i=i+1
            return v