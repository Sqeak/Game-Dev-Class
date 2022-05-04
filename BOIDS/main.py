import random
#imports parts of the arcade library to lessen load time
from arcade import Window, start_render, finish_render, run, set_background_color, color, SpriteList
#imports boidClass from the file boid.py
from boid import boidClass, SCREEN_HEIGHT, SCREEN_WIDTH

#creates a boidClass named boid
#boid = boidClass()


SCREEN_WIDTH = SCREEN_WIDTH
SCREEN_HEIGHT = SCREEN_HEIGHT
SCREEN_TITLE = "BOIDS Simulation"
BOID_AMOUNT = 10

boids = []

for x in range(BOID_AMOUNT):
    boids.append(boidClass())

"""
the classic game loop, which contains an initial setup (__init__), a function called on draw (meant for displaying),  
and one called on the update (meant for calculating physics)
"""



class gameLoop(Window):
    
    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)
    
        # Set the background color
        set_background_color(color.WHITE)
            
        

    def on_update(self, delta_time):  
        
        #loop through each boid and update their velocity and position
        for boid in boids:
            
            
            #boid.align(boids)
            #boid.attraction(boids)
            boid.seperate(boids)
            boid.update()
            boid.edges()

        
    def on_draw(self):
       
        #Anything that needs to be rendered will be done between arcade.start_render() and arcade.finish_render().
        start_render()
        
        #Draws the sprites of every boid
        for boid in boids:
            boid.draw()
        
        finish_render()   
        
    



def main():
    window = gameLoop(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    
    run()

    
main()