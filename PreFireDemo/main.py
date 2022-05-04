import arcade
import euclid

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

bullet_list = []
bullet_speed = 5

class Bullet():
    
    def __init__(self, position, direction):
        self.position = euclid.Vector2(position.x, position.y)
        self.direction = euclid.Vector2(direction.x, direction.y)
        
    def update(self):
        self.position += self.direction * bullet_speed

class DemoWindow(arcade.Window):
    
    def __init__(self, x, y, title):
        super().__init__(x, y, title)
        
        self.target_position = euclid.Vector2(50, 50)
        self.target_velocity = euclid.Vector2(1, 0)
        
        self.origin_position = euclid.Vector2(100, 100)
        self.origin_velocity = euclid.Vector2(-1, .5)
        
        arcade.set_background_color(arcade.color.WHITE)
        
    def on_draw(self):
        
        arcade.start_render()
        
        arcade.draw_circle_filled(self.target_position.x, self.target_position.y, 4, arcade.color.BLACK)
        
        arcade.draw_circle_filled(self.origin_position.x, self.origin_position.y, 8, arcade.color.BLACK)
        
        for bullet in bullet_list:
            arcade.draw_circle_filled(bullet.position.x, bullet.position.y, 2, arcade.color.BLACK)
            
    def on_update(self, deltaTime):
        
        self.target_position += self.target_velocity
        self.origin_position += self.origin_velocity
        
        for bullet in bullet_list:
            bullet.update()
            
    def on_key_press(self, key, mod):
        
        if key == arcade.key.SPACE:
            bullet_list.append(Bullet(self.origin_position, self.predict()))
            
    def predict(self):
        
        desired_positon = euclid.Vector2()
        
        time = 0
        
        deltaV = bullet_speed - abs(self.target_velocity)
        deltaP = self.target_position - self.origin_position
        time = abs(deltaP/deltaV)
        
        #knowing time, we are able to find the predicted position
        desired_positon = self.target_position + self.target_velocity * time
        desired_direction = desired_positon - self.origin_position
        desired_direction.normalize()
        
        print(desired_direction)
        
        return desired_direction
    
    
def main():
    window = DemoWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "Pre Fire Demo")
    arcade.run()
    
main()