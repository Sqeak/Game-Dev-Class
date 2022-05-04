import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

path = []

class myWindow(arcade.Window):
    def __init__(self, width, height, title):
        
        super().__init__(width, height, title)
        
        arcade.set_background_color(arcade.color.WHITE)
        
        self.posX = SCREEN_WIDTH/2
        self.posY = SCREEN_HEIGHT/2
        
        self.size = 2
        
    
    def on_draw(self):
        
        arcade.start_render()
        
        arcade.draw_points(tuple(path), arcade.color.BLACK + (100,), self.size)
        arcade.draw_point(path[-1][0], path[-1][1], arcade.color.RED_ORANGE, self.size*2)
        
        
    def on_update(self, deltaTime):
         
        choice = random.randint(0, 3)
        
        if choice == 0:
            self.posX += self.size
        elif choice == 1:
            self.posX -= self.size
        elif choice == 2:
            self.posY += self.size
        elif choice == 3:
            self.posY -= self.size
            
        path.append((self.posX, self.posY))
        self.reposition()
        
    def reposition(self):
        totalX = 0
        totalY = 0
        for point in path:
            totalX += point[0]
            totalY += point[1]
        totalX = totalX/len(path)
        totalY = totalY/len(path)
        
        arcade.set_viewport(totalX - SCREEN_WIDTH/2, totalX + SCREEN_WIDTH/2, totalY - SCREEN_HEIGHT/2, totalY + SCREEN_HEIGHT/2)
            
if __name__ == "__main__":
    window = myWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "Title Goes Here")
    arcade.run()
            