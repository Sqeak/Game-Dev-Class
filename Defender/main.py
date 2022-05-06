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

bullet_list = arcade.SpriteList()

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
        self.bullet_speed = 0
        
        self.frequency_of_direction_delta = 0
        self.frequency_of_fire = 0
        self.direction_delta_randomness = 2
        self.shot_randomness = 4
        
        self.timer1 = time.time()
        self.timer2 = time.time()
        self.time_till_next_change = 0
        self.time_till_next_shot = 0
        
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
        
        self.shot_deviation = 5
        self.bullet_speed = 3
        
        self.velocity.x = random.uniform(-self.maxVelocity, self.maxVelocity)
        self.velocity.y = random.uniform(-self.maxVelocity/2, self.maxVelocity/2)
        
        self.frequency_of_change_in_direction = 3
        self.frequency_of_fire = 4
        
        self.myhuman = None
            
    def movementPattern(self):
        #I need to find out how to make the lander fly near the ground. I'm thinking that if i have a certain height threshold, then
        #I can have the lander reverse it's y velocity to keep it from getting too high.
        #Of course, only sdo this if it doesn't have a human, but if it does, then beeline for the top of the screen.
        if self.has_human:
            #If it has a human then cut off horizontal thrust and go streight to the top.
            self.velocity.x = 0
            self.velocity.y = -self.maxVelocity
            
            #If you reach the top of the screen the call the mutate function
            if self.position.y >= SCREEN_HEIGHT:
                self.mutate()
        
        else:
            if self.position.y <= self.max_height:
                self.velocity.y = -self.velocity.y
            
            #If movement cooldown is over
            if time.time() - self.timer1 >= self.time_till_next_change:
                #Randomly change velocity
                self.velocity.x = random.uniform(-self.maxVelocity, self.maxVelocity)
                self.velocity.y = random.uniform(-self.maxVelocity/2, self.maxVelocity/2)
                #Reset cool down and add or remove a random amount of time to add variety to it's behaviour
                self.timer1 = time.time()
                self.time_till_next_change = self.frequency_of_change_in_direction + random.uniform(-self.direction_delta_randomness, self.direction_delta_randomness)
                
    def firingPattern(self):
        #If firing cooldown is over
        if time.time() - self.timer2 >= self.time_till_next_shot:
            #Find future position of player and aim in that direction with some inaccuracy
            bullet_direction = predictLocation(player.position, self.position, self.bullet_speed)
            bullet_direction += Vector2(random.uniform(-self.shot_deviation, self.shot_deviation), random.uniform(-self.shot_deviation, self.shot_deviation)).normalize()
            bullet_list.append(Bullet(self.position, bullet_direction, self.bullet_speed))
            #Reset firing cooldown and add or remove a random amount
            self.time_till_next_shot = self.frequency_of_fire + random.uniform(-self.shot_randomness, self.shot_randomness)
                
                
            
            
            
                 