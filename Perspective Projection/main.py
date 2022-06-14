import arcade
import numpy as np
import math

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

POINT_RADIUS = 6

points = np.abs(np.random.rand(4, 3) * SCREEN_WIDTH)
print(points)

fov = 60

projection_matrix = [
    [1, 0, 0],
    [0, 1, 0]
]


weak_perspective_projection_matrix = [
    [1/z*math.tan(math.radians(fov)/2), 0, 0],
    [0, 1/z*math.tan(math.radians(fov)/2), 0]
]

def draw_with_projection(points, projection):
    projection2d = []
    for point in points:
        projection2d.append(np.matmul(projection, point))
        
    for i in projection2d:
        arcade.draw_circle_filled(i[0], i[1], POINT_RADIUS, arcade.color.BLACK)
        

class MainWindow(arcade.Window):
    
    def __init__(self, x, y, title):
        
        super().__init__(x, y, title)
        
        arcade.set_background_color(arcade.color.BURNT_ORANGE)
        
    def on_draw(self):
        arcade.start_render()
        draw_with_projection(points, weak_perspective_projection_matrix)
        
    
    #def on_update(self, deltaTime):
        
    

if __name__ == "__main__":
    window = MainWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "Insert Title Here")
    arcade.run()