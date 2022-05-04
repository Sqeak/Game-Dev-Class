import random
import arcade
from time import time

blockTypes = ["I", "L", "J", "S", "Z", "T", "Square"]

I_Tiles = [
    
    #Rotations 0 and 2
    [(0, 0), (0, 1), (0, 2), (0, -1)],
    #Rotations 1 and 3
    [(0, 0), (1, 0), (2, 0), (-1, 0)]
    
    ]

T_Tiles = [
    
    #Rotation 0
    [(0, 0), (0, -1), (-1, -1), (1, -1)],
    #Rotation 1
    [(0, 0), (-1, 0), (-1, 1), (-1, -1)],
    #Rotation 2
    [(0, 0), (0, 1), (1, 1), (-1, 1)],
    #Rotation 3
    [(0, 0), (1, 0), (1, -1), (1, 1)]
    
    ]

L_Tiles = [
    
    #Rotation 0
    [(0, 0), (0, 1), (0, -1), (1, -1)],
    #Rotation 1
    [(0, 0), (1, 0), (-1, 0), (-1, -1)],
    #Rotation 2
    [(0, 0), (0, -1), (0, 1), (-1, 1)],
    #Rotation 3
    [(0, 0), (-1, 0), (1, 0), (1, 1)]
    
    ]

J_Tiles = [
    
    #Rotation 0
    [(0, 0), (0, 1), (0, -1), (-1, -1)],
    #Rotation 1
    [(0, 0), (1, 0), (-1, 0), (-1, 1)],
    #Rotation 2
    [(0, 0), (0, -1), (0, 1), (1, 1)],
    #Rotation 3
    [(0, 0), (-1, 0), (1, 0), (1, -1)]
    
    ]


Z_Tiles = [
    
    #Rotations 0 and 2
    [(0, 0), (-1, 0), (0, -1), (1, -1)],
    #Rotations 1 and 3
    [(0, 0), (0, 1), (-1, 0), (-1, -1)],
    
    ]

S_Tiles = [
    
    #Rotations 0 and 2
    [(0, 0), (1, 0), (0, -1), (-1, -1)],
    #Rotations 1 and 3
    [(0, 0), (0, -1), (-1, 0), (-1, 1)]
     
    ]
    
Square_Tiles = [[(0, 0), (-1, 0), (-1, -1), (0, -1)]]
    

class Block():
    
    def __init__(self, x, y, fallingSpeed, gridSize, blockType=None):
        self.gridX = x
        self.gridY = y
        self.dX = 0
        self.dY = 0
        #Falling Speed represents how many seconds will pass before the block is moved down 1 cell
        self.fallingSpeed = fallingSpeed
        self.blockType = blockType
        self.blockStates = None
        if blockType != None:
            self.blockStates = globals()[self.blockType + "_Tiles"]
        self.gridSize = gridSize
        self.rotation = 0
        self.start = time()
        self.touchedBottom = False
        self.locked = False
        self.drop = False
        
    def setup(self):
        
        #Determine block type
        if self.blockType == None:
            #Chooses random block type
            self.blockType = blockTypes[random.randint(0, len(blockTypes) -1 )]
            print("Block Created: " + self.blockType)
            #Assigns tetriminoes depending on selected block type
            self.blockStates = globals()[self.blockType + "_Tiles"]
                                        
            
    def show(self):
        
        #Draw tetriminoes depending on rotation and block type
        for i in self.blockStates[self.rotation]:
            drawX = ((self.gridX+i[0])*self.gridSize)-self.gridSize/2
            drawY = ((self.gridY+i[1])*self.gridSize)-self.gridSize/2
            arcade.draw_rectangle_filled(drawX, drawY, self.gridSize, self.gridSize, arcade.color.RED)
            
    def move(self):
        
        #Move Y value down one cell if the current fallingSpeed has passed
        if self.drop:
            self.dY = -1        
        elif time() - self.start >= self.fallingSpeed and self.touchedBottom == False:
            self.start = time()
            self.dY = -1   
        elif time() - self.start >= self.fallingSpeed and self.touchedBottom:
            self.locked = True
        
        if self.gridX < 1:
            self.gridX += 1
            self.dX = 0
        elif self.dX > 1:
            self.dX = 1
        
        if self.dY < -1:
            self.dY = -1
        elif self.dY > 1:
            self.dY = 1           
            
        self.gridX += self.dX
        self.gridY += self.dY
        self.dX = 0
        self.dY = 0
        
            
            
    def checkEdges(self):
        
        for tile in self.blockStates[self.rotation]:
            if self.gridX + tile[0] > 10:
                self.dX = -1
            elif self.gridX + tile[0] < 1:
                self.dX = 1
            
            if self.gridY + tile[1] < 1:
                self.touchedBottom = True
                self.dY = 1
                
            else:
                self.touchedBottom = False
                
    def setRotation(self):
        
        #Reset rotation depending on block if value is greater
        if self.rotation >= 4 and (self.blockType == "J" or self.blockType == "L" or self.blockType == "T"):
            self.rotation = 0
        elif self.rotation >= 2 and (self.blockType == "S" or self.blockType == "Z" or self.blockType == "I"):
            self.rotation = 0
        elif self.rotation >= 1 and self.blockType == "Square":
            self.rotation = 0        
        


        
        
        
globals()["side" + str(random) + ".jpeg"]