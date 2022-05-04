import random
from math import sqrt
from arcade import draw_circle_filled, color
from euclid import Vector2
from useful import setMag, findDist, findSlope

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600



class boidClass():
    
    def __init__(self): 
        self.pos = Vector2(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
        self.vel = Vector2(random.randint(-99, 99) / 100, random.randint(-99, 99) / 100)
        self.vel.normalize()
        self.acc = Vector2(0, 0)
        self.scale = .75
        #self.sprite = Sprite("sprites/triangle2.png", self.scale)
        self.maxVel = 3
        self.maxAcc = 1
        self.vel = setMag(self.vel, self.maxVel)
        #self.sprite.center_x = self.pos.x
        #self.sprite.center_y = self.pos.y
        
    def draw(self):
        draw_circle_filled(self.pos.x, self.pos.y, 6, color.BLACK)
        
    def edges(self):
        if self.pos.x < 0:
            self.pos.x = SCREEN_WIDTH
        elif self.pos.x > SCREEN_WIDTH:
            self.pos.x = 0
            
        if self.pos.y < 0:
            self.pos.y = SCREEN_HEIGHT
        elif self.pos.y > SCREEN_HEIGHT:
            self.pos.y = 0
            
    def align(self, boids):
        desiredDirection = Vector2()
        perceptionRadius = 100
        nearbyBoids = self.boidWithinPerception(boids, perceptionRadius)
        total = 0
        
        for other in nearbyBoids:
            desiredDirection += other.vel
            total += 1
        
        if len(self.boidWithinPerception(boids, perceptionRadius)) > 1:
            averageDirection = desiredDirection / total
            averageDirection.normalize()
            averageDirection = setMag(averageDirection, self.maxVel)
            
            self.vel = averageDirection
    
    def seperate(self, boids):
        repellingFactor = 30
        a = repellingFactor
        desiredDirection = Vector2()
        averagePosition = Vector2()
        perceptionRadius = 100
        nearbyBoids = self.boidWithinPerception(boids, perceptionRadius)
        total = 0
        
        for other in nearbyBoids:
            averagePosition += other.pos
            total += 1
            
        if len(self.boidWithinPerception(boids, perceptionRadius)) > 0:
            averagePosition = averagePosition / total
            
            desiredDirection = findSlope(averagePosition, self.pos)
            desiredDirection.normalize()
            desiredDirection = setMag(desiredDirection, a / (findDist(self.pos, averagePosition) * findDist(self.pos, averagePosition)))
            
            self.acc += desiredDirection
            
    def attraction(self, boids):
        repellingFactor = 6
        a = repellingFactor        
        averagePosition = Vector2()
        desiredDirection = Vector2()
        perceptionRadius = 100
        nearbyBoids = self.boidWithinPerception(boids, perceptionRadius)
        total = 0
        
        for other in nearbyBoids:
            averagePosition += other.pos
            total += 1
            
            
        if len(self.boidWithinPerception(boids, perceptionRadius)) > 1:   
            averagePosition = averagePosition / total
            
            desiredDirection = findSlope(averagePosition, self.pos)
            desiredDirection.normalize()
            desiredDirection = setMag(desiredDirection, a / (findDist(self.pos, averagePosition) * findDist(self.pos, averagePosition)))
            
            self.acc -= desiredDirection        
    
    def update(self):
        self.vel += self.acc
        self.pos += self.vel
        
        if self.vel.magnitude() >= self.maxVel:
            self.vel.normalize()
            self.vel = setMag(self.vel, self.maxVel)
        
        if self.acc.magnitude() >= self.maxAcc:
            self.acc.normalize()
            self.acc = setMag(self.acc, self.maxAcc)               
            
    def boidWithinPerception(self, boids, perception):
        selectedBoids = []
        
        for other in boids:
            d = findDist(other.pos, self.pos)
            if d < perception and other != self:
                selectedBoids.append(other)
                
        return selectedBoids
        
            