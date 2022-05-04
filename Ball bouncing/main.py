import arcade
from ball import Ball

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

balls = []

for x in range(4):
    balls.append(Ball(SCREEN_WIDTH, SCREEN_HEIGHT))

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.ATOMIC_TANGERINE)



    def on_draw(self):
        arcade.start_render()
        for ball in balls:
            ball.show()
            ball.connect(balls)

    def on_update(self, deltaTime):
        for ball in balls:
            ball.checkEdges()
            ball.move()


if __name__ == "__main__":
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Title")

    arcade.run()

