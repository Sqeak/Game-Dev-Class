import arcade
import useful
from blocks import Block

SCREEN_WIDTH = 250
SCREEN_HEIGHT = 500

gridSize = 25

grid = useful.create2DArray(10, 20, 0)
print(grid)

block = Block(5, 18, 1, gridSize, "I")
block.setup()


class MyGame(arcade.Window):
    
    def __init__(self, x, y, Title):
        
        super().__init__(x, y, Title)
            
        arcade.set_background_color(arcade.color.BLACK)
        
    def on_draw(self):
        arcade.start_render()
        #arcade.draw_rectangle_filled((5*gridSize)-gridSize/2, (18*gridSize)-gridSize/2, gridSize, gridSize, arcade.color.WHITE)
        block.show()
        
        for i in range(0, SCREEN_WIDTH, gridSize):
            arcade.draw_line(i, SCREEN_HEIGHT, i, 0, arcade.color.WHITE, 1)
            
        for i in range(0, SCREEN_HEIGHT, gridSize):
            arcade.draw_line(SCREEN_WIDTH, i, 0, i, arcade.color.WHITE, 1)
            
    def on_update(self, deltaTime):
        block.checkEdges()
        block.move()
        
            
    def on_key_press(self, key, mod):
        if key == arcade.key.SPACE:
            block.rotation += 1
            block.setRotation()
        
        if key == arcade.key.LEFT:
            block.dX = -1
        
        if key == arcade.key.RIGHT:
            block.dX = 1
        
        if key == arcade.key.DOWN:
            if not block.touchedBottom:
                block.drop = True
            
    def on_key_release(self, key, mod):
        if key == arcade.key.DOWN:
            block.drop = False


if __name__ == "__main__":
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Title Goes Here")
    arcade.run()
    