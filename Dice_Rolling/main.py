import arcade
import random
from time import sleep

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

screenBuffer = 10

diceNumber = 5
sprite_list = arcade.SpriteList()
dice_list = []

class Dice():
    
    def __init__(self):
        self.value = random.randint(1, 6)
        self.posX = random.randint(screenBuffer, SCREEN_WIDTH-screenBuffer)
        self.posY = random.randint(screenBuffer, SCREEN_HEIGHT-screenBuffer)
        
    def roll(self):
        self.value = random.randint(1, 6)
    
    def updateImage(self):
        image = "images/dieRed" + str(self.value) + ".png"
        dice = arcade.Sprite(image, .75)
        dice.center_x = random.randint(screenBuffer, SCREEN_WIDTH-screenBuffer)
        dice.center_y = random.randint(screenBuffer, SCREEN_HEIGHT-screenBuffer)        
        sprite_list.append(dice)
        
for i in range(diceNumber):
    dice_list.append(Dice())
    
print(dice_list)

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.set_mouse_visible(False)        
        arcade.set_background_color(arcade.color.ASH_GREY)   
       
        self.roll = False
        
        self.yahtzee = False
        
    def roll_the_dice(self):
        
        sprite_list = arcade.SpriteList()

        """ Add Your Code Here """
        for i in sprite_list:
            i.remove_from_sprite_lists()
        
        for i in dice_list:
            i.roll()
            i.updateImage()
            
        for i in dice_list:
            if dice_list[0].value == i.value:
                self.yahtzee == True
            else:
                self.yahtzee == False
                   
        sprite_list.update()   
            
            
        
    def on_draw(self):
        arcade.start_render()
        """ Add Your Code Here """
        
        sprite_list.draw()
        
        if self.yahtzee:
            arcade.draw_text("Yahtzee!", (SCREEN_WIDTH/4), (SCREEN_HEIGHT/4), arcade.color.WHITE, 12)

    def update(self, delta_time):
        if self.roll == True:
            self.roll_the_dice()

    def on_key_press(self, key, modifiers):

        if key == arcade.key.SPACE:
            self.roll = True

    def on_key_release(self, key, modifiers):

        if key == arcade.key.SPACE:
            self.roll = False 


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Roll the Dice")        
    window.roll_the_dice()
    arcade.run()

main()
