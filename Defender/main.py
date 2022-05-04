import arcade
import euclid

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 2000

player_list = arcade.SpriteList()
enemy_list = []

lander_list = arcade.SpriteList()
mutant_list = arcade.SpriteList()
baiter_list = arcade.SpriteList()
bomber_list = arcade.SpriteList()
pod_list = arcade.SpriteList()
swarmer_list = arcade.SpriteList()

enemy_list.append(lander_list)
enemy_list.append(mutant_list)
enemy_list.append(baiter_list)
enemy_list.append(bomber_list)
enemy_list.append(pod_list)
enemy_list.append(swarmer_list)

LANDER = 0
MUTANT = 1
BAITER = 2
BOMBER = 3
POD = 4
SWARMER = 5

manti_species_list = ["Lander", "Mutant", "Baiter", "Bomber", "Pod", "Swarmer"]

class Player(arcade.Sprite):
    
    def __init__(self, sprite, scale, position):
        
        #add standard init for sprite
        super().__init__(sprite, scale)
        
class Manti(arcade.Sprite):

    def __init__(self, sprite, scale, position, species):
        
        #add standard init for sprite
        super().__init__(sprite, scale)
        
        self.center_x = position.x
        self.center_y = position.y
        
        self.species = manti_species_list[species]
        
        
