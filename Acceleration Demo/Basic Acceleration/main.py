import arcade
from euclid import Vector2
import useful

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 100

class BALL():
    
    def __init__(self):
        self.pos = Vector2(0, SCREEN_HEIGHT/2)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(1, 0)
        self.maxVel = 20
        
    def show(self):
        arcade.draw_point(self.pos.x, self.pos.y, arcade.color.BLACK, 6)
    
    def update(self):
        self.vel += self.acc
        self.pos += self.vel
        
        if abs(self.vel) > 5:
            self.vel.normalize()
            self.vel = useful.setMag(self.vel, self.maxVel)
           
           
newBall = BALL() 
            
class myWindow(arcade.Window):
    def __init__(self, width, height, title):
        
        super().__init__(width, height, title)
        
        arcade.set_background_color(arcade.color.ASH_GREY)
        
    def on_draw(self):
        arcade.start_render()
        
        newBall.show()
        
    def on_update(self, deltaTime):
        newBall.update()
        
        
if __name__ == "__main__":
    window = myWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "Title Goes Here")
    
    arcade.run()