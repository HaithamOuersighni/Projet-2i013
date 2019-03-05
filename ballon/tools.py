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
        def cannot(self):
            if self.norme>PLAYER_RADIUS+BALL_RADIUS:
                return True
            else:
                return False
        @property
        def milieu(self):
            if self.ball.x==GAME_WIDTH/2 and self.ball.y==GAME_HEIGHT/2:
                return True 
            else:
                return False
        @property
        def ide(self):
            return self.id_player
        @property
        def step(self):
            return self.state.step
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
        def gnorme(self):
            return math.sqrt(((self.id_team%2)*GAME_WIDTH-self.player.x)**2+(45-self.player.y)**2)
        @property
        def cnorme(self):
            i=0
            n=len(self.state.players)/2
            v=Vector2D(GAME_WIDTH,GAME_HEIGHT)
            while i<n:
                if 0<(math.sqrt((self.state.player_state(self.id_team%2+1,i).position.x-(self.id_team%2+1)*GAME_WIDTH)**2+(self.state.player_state(self.id_team%2+1,i).position.y-GAME_HEIGHT/2)**2)) and (math.sqrt((self.state.player_state(self.id_team%2+1,i).position.x-(self.id_team%2+1)*GAME_WIDTH)**2+(self.state.player_state(self.id_team%2+1,i).position.y-GAME_HEIGHT/2)**2))<math.sqrt(v.x**2+v.y**2):
                    v=Vector2D(self.state.player_state(self.id_team%2+1,i).position.x-(self.id_team%2)*GAME_WIDTH,self.state.player_state(self.id_team%2+1,i).position.y-GAME_HEIGHT/2)
                i=i+1
            return math.sqrt(v.x**2+v.y**2)
        @property
        def fnorme(self):
            i=0
            n=len(self.state.players)/2
            v=Vector2D(GAME_WIDTH,GAME_HEIGHT)
            while i<n:
                if 0<(math.sqrt((self.state.player_state(self.id_team,i).position.x-self.ball.x)**2+(self.state.player_state(self.id_team,i).position.y-self.ball.y)**2) and (math.sqrt((self.state.player_state(self.id_team,i).position.x-self.player.x)**2+(self.state.player_state(self.id_team,i).position.y-self.player.y)**2)<math.sqrt(v.x**2+v.y**2))):
                    v=Vector2D(self.state.player_state(self.id_team,i).position.x-self.ball.x,self.state.player_state(self.id_team,i).position.y-self.ball.y)
                i=i+1
            return math.sqrt(v.x**2+v.y**2)
        @property
        def enorme(self): #distance ball et adversaire
            i=0
            n=len(self.state.players)/2
            v=Vector2D(GAME_WIDTH,GAME_HEIGHT)
            while i<n:
                if (math.sqrt((self.state.player_state(self.id_team%2+1,i).position.x-self.ball.x)**2+(self.state.player_state(self.id_team%2+1,i).position.y-self.ball.y)**2)<math.sqrt(v.x**2+v.y**2)):
                    v=Vector2D(self.state.player_state(self.id_team%2+1,i).position.x-self.ball.x,self.state.player_state(self.id_team%2+1,i).position.y-self.ball.y)
                i=i+1
            return math.sqrt(v.x**2+v.y**2)
        @property
        def eproche(self):
            i=0
            n=len(self.state.players)/2
            v=Vector2D(GAME_WIDTH,GAME_HEIGHT)
            while i<n:
                if (math.sqrt((self.state.player_state(self.id_team%2+1,i).position.x-self.player.x)**2+(self.state.player_state(self.id_team%2+1,i).position.y-self.player.y)**2)<math.sqrt(v.x**2+v.y**2)):
                    v=Vector2D(self.state.player_state(self.id_team%2+1,i).position.x-self.player.x,self.state.player_state(self.id_team%2+1,i).position.y-self.player.y)
                i=i+1
            return math.sqrt(v.x**2+v.y**2)
        
        @property
        def pos_eproche(self): # retourne la position de l'ennemie le plus proche
            i=0
            n=len(self.state.players)/2
            v=Vector2D(GAME_WIDTH,GAME_HEIGHT)
            while i<n:
                if (math.sqrt((self.state.player_state(self.id_team%2+1,i).position.x-self.player.x)**2+(self.state.player_state(self.id_team%2+1,i).position.y-self.player.y)**2)<math.sqrt(v.x**2+v.y**2)):
                    v=Vector2D(self.state.player_state(self.id_team%2+1,i).position.x-self.player.x,self.state.player_state(self.id_team%2+1,i).position.y-self.player.y)
                    j=self.state.player_state(self.id_team%2+1,i).position
                i=i+1
            return j
                
            
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
        
        @property
        def aligne_def(self): #s'aligne entre la balle et les cage pour un x donné
            if self.id_team==1:
                a=(self.ball.y-45)/self.ball.x
                b=45
            else:
                a=(self.ball.y-45)/(self.ball.x-150)
                b=45-150*a
            return a*self.player.x+b
        
        @property
        def aligne_def_y(self): #s'aligne entre la balle et les cage pour un y donné
            if self.id_team==1:
                a=(self.ball.y-45)/self.ball.x
                b=45
            else:
                a=(self.ball.y-45)/(self.ball.x-150)
                b=45-150*a
            return (self.player.y-b)/a
        
        @property
        def enemy1v1(self):
            if self.id_team==1:
                return self.state.player_state(2,0).position
            else:
                return self.state.player_state(1,0).position
        @property
        def unedeux(self):
            if self.id_team==1:
                if(self.id_player==0):
                    return self.state.player_state(1,1).position
                else:
                    return self.state.player_state(1,0).position
            else:
                if(self.id_player==1):
                    return self.state.player_state(2,1).position
                else:
                    return self.state.player_state(2,0).position

        #@property
        """def pgoal(self):
            if self.id_team==1:
                yb=self.ball.y
                ya=GAME_HEIGHT/2
                xb=self.ball.x
                xa=0
                
                a=(yb-ya)/(xb-xa)
                b=yb/xb*a
                print(a,b)
                #y=ax+b
                delta=(2*a*b-90*a)**2-4*(1+a)*(b**2-90*b+1961)
                x=(-(2*a*b-90*a)+math.sqrt(delta))/2*(1+a)
                if(x<0):
                    x=(-(a*b-90*a)-math.sqrt(delta))/2*(1+a)
                y=a*x+b
            else:
                yb=self.ball.y
                ya=GAME_HEIGHT/2
                xb=self.ball.x
                xa=GAME_WIDTH
                
                a=(yb-ya)/(xb-xa)
                b=yb/xb*a
                
                delta = (-300+2*a*b-90*a)-4*(1+a)*(24461+b**2+90*b)
                x=(-(-300+2*a*b-90*a))+math.sqrt(delta)/2*(1+a)
                if x>150:
                    x=(-(-300+2*a*b-90*a))-math.sqrt(delta)/2*(1+a)
                y=ax+b
                
            return Vector2D(x,y)"""
            
class Decorator():
    def __init__ ( self , state ):
            self.state = state
    def __getattr__ ( self , attr ):
            return getattr ( self . state , attr )
class Shoot ( Decorator ):
    def __init__ ( self , state ):
        self.state=state
    def shoot ( self , p ):
        dist=self.norme
        if dist<PLAYER_RADIUS+BALL_RADIUS:
            return SoccerAction ( shoot=p)
        else:
            return SoccerAction()
    def to_goal(self, strength):
        return self.shoot((self.state.goal-self.state.player).normalize()*strength)
class Passe ( Decorator ):
    def __init__ ( self , state ):
        Decorator . __init__ ( self , state )        
    def passe ( self , p ):
        return SoccerAction ( Vector2D (...))
class Move(object):
    def __init__(self,state):
        self.state=state
    def move(self,acceleration=None):
        return SoccerAction(acceleration=acceleration)
    def to_ball(self):
        return self.move(self.state.ball-self.state.player)