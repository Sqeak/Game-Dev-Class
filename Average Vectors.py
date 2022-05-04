'''
This program was created to aid me in creating a BOID simulation, it creates a certain amount of dots of choice, and then assigns random positions and velocities.
The last blue dot is then used to represent the average location and velocities of all of the dots.
'''
#imports graphic library, the vector library, random (which is used to assign positions for the dots, and my own personal library
import arcade
from euclid import Vector2
import random
from useful import setMag

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Averaged Vectors"


#set dot amount and create dots array
DOT_AMOUNT = 5
dots = []

#set up windows
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.set_background_color(arcade.color.WHITE)

#Declare dot class
class dot():
    
    #when initialized, so that means it's gets automatically called when the class is created in line 52
    def __init__ (self):
        #this is just the length of the line, but later it can be used as the strength of a force
        self.mag = 30
        #creating the positions in random positions within the screen dimensions
        self.pos = Vector2(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
        #Creats a random direction of the dot, each will be between -.99 and .99
        self.direction = Vector2(random.randint(-99, 99) / 100, random.randint(-99, 99) / 100)
        #normalize, also known as simplify as much as possible, this will bring any vector to the same base magnitude of 1
        self.direction.normalize()
        #pretty sure it effectivly multiplies it, which is why every vector needs to be normalized before the magnitude is set, or else the results would be
        #incosistent
        self.direction = setMag(self.direction, self.mag)
        #defines where the second x,y coords will be for the line that represents the vector
        self.linePos = self.direction + self.pos
        
    def draw(self):
        #draws a circle at pos.x and pos.y ( from line 27 )
        arcade.draw_circle_filled(self.pos.x, self.pos.y, 10, arcade.color.BLACK)
        #draws a line starting at the circle center and going to linePos
        arcade.draw_line(self.pos.x, self.pos.y, self.linePos.x, self.linePos.y, arcade.color.BLACK, 4)
        

#create a dot and add it to the dots array 5 times        
for x in range(DOT_AMOUNT):
    dots.append(dot())
    

#begins the rendering, everything after this and before finish_render will be drawn to the canvas        
arcade.start_render()

#sets total to zero
total = 0
#Creates the 2d Vectors that will be used to find the average direction and positions of all 'DOT_AMOUNT' dots
averageDirection = Vector2()
averagePosition = Vector2()

#for every element in the dots array, display the dot and it's corresponding vector
for dot in dots:
    dot.draw()
    
    #add the current dot's direction and position to the variables created in 56-57
    averageDirection += dot.direction
    averagePosition += dot.pos
    #Adds 1 to total for every dot in the array
    total += 1
    
#calculate average by dividing the sum of all dot values by the total
averagePosition = averagePosition / total
averageDirection = averageDirection / total
#normalizes average direction
averageDirection.normalize()
#sets the magnitude of average direction to the same as the dot class
averageDirection = setMag(averageDirection, 30)
#create the second coords for the vector line
linePos = averageDirection + averagePosition

#debugging :D
print(averagePosition)
print(linePos)

#draws the circle and vector that will represent all of the dots average locations and speeds
arcade.draw_circle_filled(averagePosition.x, averagePosition.y, 10, arcade.color.DARK_BLUE)
arcade.draw_line(averagePosition.x, averagePosition.y, linePos.x, linePos.y, arcade.color.DARK_BLUE, 4)


#finish rendering
arcade.finish_render()

#keep the window open until closed
arcade.run()
    
    