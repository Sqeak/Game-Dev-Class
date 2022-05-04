import arcade
import useful
from euclid import Vector2

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class BALL():
    
    def __init__(self):
        self.pos = Vector2(0, 0)
        self.pastPos = Vector2(0, 0)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)
        self.maxVel = 10
        self.listOfPositions = []
        
    def show(self):
        arcade.draw_circle_filled(self.pos.x, self.pos.y, 8, arcade.color.BLACK)
        
    def update(self):
        self.acc.normalize()
        self.vel += self.acc
        
        if self.vel.magnitude() >= self.maxVel:
            self.vel = self.vel.normalized() * self.maxVel
            
        self.listOfPositions.append(self.pos.copy())
        
        self.pos += self.vel
        
    def attract(self, mouseX, mouseY):
        desired = Vector2(mouseX - self.pos.x, mouseY - self.pos.y)
        desired.normalize()
        self.acc += desired
        
    def repel(self, mouseX, mouseY):
        desired = Vector2(mouseX - self.pos.x, mouseY - self.pos.y)
        desired.normalize()
        self.acc -= desired
        
    def draw_path(self):
        self.listOfPositions = self.listOfPositions[-20:]
        for i in range(len(self.listOfPositions)):
            if i != 0:
                arcade.draw_line(self.listOfPositions[i-1].x, self.listOfPositions[i-1].y, self.listOfPositions[i].x, self.listOfPositions[i].y, arcade.color.BLACK + (i*6,), 5)
        
newBALL = BALL()
        
class myWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        
        arcade.set_background_color(arcade.color.ASH_GREY)
        
        self.mouseX = 0
        self.mouseY = 0
        
        self.repel = False
        
    def on_draw(self):
        arcade.start_render()
        newBALL.show()
        newBALL.draw_path()
        
    def on_update(self, deltaTime):
        if self.repel:
            newBALL.repel(self.mouseX, self.mouseY)
        else:
            newBALL.attract(self.mouseX, self.mouseY)
        
        newBALL.update()
        
        
    def on_mouse_motion(self, mouseX, mouseY, dx, dy):
        self.mouseX = mouseX
        self.mouseY = mouseY
        
    def on_mouse_press(self, mouseX, mouseY, button, mod):
        self.repel = True
        
    def on_mouse_release(self, mouseX, mouseY, button, mod):
        self.repel = False
    
if __name__ == "__main__":
    window = myWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "Insert Title Here")
    
    arcade.run()