import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Draw Tree Function")
arcade.set_background_color(arcade.color.WHITE)


#origin for tree is bottom left corner

def drawTree (posX, posY, width, height):
    
    #draw trunk
    arcade.draw_rectangle_filled((width / 2) + posX, (height / 4) + posY, width * .3, height * .6, arcade.color.DARK_BROWN)
    
    arcade.draw_circle_filled((width / 2) + posX, (height / 2) + posY, width * .6, arcade.color.ANDROID_GREEN)
    





arcade.start_render()

drawTree(300, 400, 200, 400)

arcade.finish_render()

arcade.run()