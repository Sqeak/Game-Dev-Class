import useful
from euclid import Vector3, Vector2
import random
from arcade import draw_circle_filled, color, draw_line
class Ball():

    def __init__(self, width, height):
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        self.radius = 16
        self.position = Vector2(random.randint(self.radius, width - self.radius), random.randint(self.radius, height - self.radius))
        self.velocity = Vector2(random.random(), random.random())
        self.maxacc = 5
        self.maxspeed = 10




    def show(self):
        draw_circle_filled(self.position.x, self.position.y, self.radius, color.BLACK)

    def move(self):

        self.velocity.normalize()
        self.velocity = self.velocity * self.maxspeed

        self.position += self.velocity


    def checkEdges(self):
        if self.position.x < self.radius:
            self.velocity = self.velocity.reflect(Vector2(1, 0))

        if self.position.x > self.SCREEN_WIDTH - self.radius:
            self.velocity = self.velocity.reflect(Vector2(1, 0))

        if self.position.y < self.radius:
            self.velocity = self.velocity.reflect(Vector2(0, 1))

        if self.position.y > self.SCREEN_HEIGHT - self.radius:
            self.velocity = self.velocity.reflect(Vector2(0, 1))


    def connect(self, others):
        for other in others:
            if other != self:
                draw_line(self.position.x, self.position.y, other.position.x, other.position.y, color.BLACK, 3)