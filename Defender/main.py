import arcade
from euclid import Vector2
import euclid
import random
import time


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 2000

LANDER_HEIGHT = 50

player_list = arcade.SpriteList()
enemy_list = []

lander_list = arcade.SpriteList()
mutant_list = arcade.SpriteList()
baiter_list = arcade.SpriteList()
bomber_list = arcade.SpriteList()
pod_list = arcade.SpriteList()
swarmer_list = arcade.SpriteList()

enemy_list.append(lander_list)
enemy_list.append(mutant_list)
enemy_list.append(baiter_list)
enemy_list.append(bomber_list)
enemy_list.append(pod_list)
enemy_list.append(swarmer_list)

LANDER = 0
MUTANT = 1
BAITER = 2
BOMBER = 3
POD = 4
SWARMER = 5

def randomVector():
    vector = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
    vector.normalize()
    return vector

def predictLocation(target, origin, speed):
    
    desired_positon = euclid.Vector2()
    
    time = 0

    deltaV = speed - abs(target.velocity)
    deltaP = self.target.position - self.origin
    time = abs(deltaP/deltaV)

    #knowing time, we are able to find the predicted position
    desired_positon = self.target.position + self.target.velocity * time
    desired_direction = desired_positon - self.origin_position
    desired_direction.normalize()

    print(desired_direction)
    
    return desired_direction    
    

class Player(arcade.Sprite):
    
    def __init__(self, sprite, scale, position):
        
        #add standard init for sprite
        super().__init__(sprite, scale)
        
        self.position = Vector2(position)
        self.velocity = Vector2(0, 0)
        
    def update(self):
        self.position += self.velocity
        
        self.center_x = self.position.x
        self.center_y = self.position.y
        
        
        
class Manti(arcade.Sprite):

    def __init__(self, sprite, scale, position):
        
        #add standard init for sprite
        super().__init__(sprite, scale)
        
        self.position = Vector2(position)
        self.velocity = Vector2(0, 0)
        
        self.shot_deviation = 0
        
        self.frequency_of_direction_delta = 0
        self.direction_delta_randomness = 2
        
        self.timer = time.time()
        self.time_till_next_change = 0
        
    def update(self):
        self.position += self.velocity
        
        self.center_x = self.position.x
        self.center_y = self.position.y
    
    def movementPattern(self):
        pass
    
    def firingPattern(self):
        pass
    

class Lander(Manti):
    
    def __init__(self, sprite, scale, position):
        
        super().__init__(sprite, scale)
        
        self.max_height = LANDER_HEIGHT
        
        self.has_human = False
        
        self.maxVelocity = 1
        
        self.velocity.x = random.uniform(-self.maxVelocity, self.maxVelocity)
        self.velocity.y = random.uniform(-self.maxVelocity/2, self.maxVelocity/2)
        
        self.frequency_of_change_in_direction = 3        
            
    def movementPattern(self):
        #I need to find out how to make the lander fly near the ground. I'm thinking that if i have a certain height threshold, then
        #I can have the lander reverse it's y velocity to keep it from getting too high.
        #Of course, only sdo this if it doesn't have a human, but if it does, then beeline for the top of the screen.
        if self.has_human:
            pass
        
        else:
            if self.position.y <= self.max_height:
                self.velocity.y = -self.velocity.y
            
            if time.time() - self.timer >= self.time_till_next_change:
                self.velocity.x = random.uniform(-self.maxVelocity, self.maxVelocity)
                self.velocity.y = random.uniform(-self.maxVelocity/2, self.maxVelocity/2)
                self.timer = time.time()
                self.time_till_next_change = self.frequency_of_change_in_direction + random.uniform(-self.direction_delta_randomness, self.direction_delta_randomness)
            
            
                
            
            
            
                 