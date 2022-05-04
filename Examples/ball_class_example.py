import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "My Arcade Window")
arcade.set_background_color(arcade.csscolor.KHAKI)



class Ball():
    def __init__(self):
        # --- Class Attributes ---
        # Ball position
        self.x = 0
        self.y = 0

        # Ball's vector
        self.change_x = 0
        self.change_y = 0

        # Ball size
        self.size = 10

        # Ball color
        self.color = [255, 255, 255]

    # --- Class Methods ---
    def move(self):
        self.x += self.change_x
        self.y += self.change_y

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color )
        
        
        
ball = Ball()
ball.x = 300
ball.y = 300
ball.change_x = 1

arcade.start_render()


while True:

    
    
    ball.draw()
    ball.move()
    
    arcade.finish_render()

arcade.run()

