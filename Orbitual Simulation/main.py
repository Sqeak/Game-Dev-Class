import arcade
import euclid
from euclid import Vector2
import math

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

G = .05

CLICK_BUFFER = 20

#All I need to know is the gravitational force acted on each planetary object. To do this, I'll use the equation F=G(m1*m2)/r^2

#Velocity needed for stable orbit. V=sqrt(Gm/r)

objects = []

empty_body = None

def distanceBetween(a, b):
    return math.sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)

def nearest(a):
    nearest = None
    for i in a:
        if nearest == None:
            nearest = i
        else:
            if i.influenceRadius < nearest.influenceRadius:
                nearest = i
    
    return nearest

def orbitalVel(center, d):
    #V=sqrt(Gm/r)
    return math.sqrt((G*center.mass)/d)
            
        
class PlanetaryObject():
    
    def __init__(self, pos, vel, mass, radius, name):
        
        self.name = name
        self.pos = pos
        self.orbitalVel = Vector2(0, 0)
        self.vel = vel
        self.acc = Vector2(0, 0)
        self.mass = mass
        self.drawnRadius = self.mass ** (1/3)
        self.influenceRadius = radius
        self.primary = None
        self.escapeVel = Vector2(0, 0)
        
        
    def setup(self):
        #Find orbital velocity
                
        #Finding nearest influencer: Create list of every influencer that you are effected by. To choose which one to orbit around, find the closest one to you
        self.findPrimary()
        
        
        if self.primary != None:
            if self.primary != self:
                mag = orbitalVel(self.primary, distanceBetween(self.pos, self.primary.pos))   
                direction = (self.pos - self.primary.pos).normalized()
                self.vel += Vector2(-direction.y, direction.x) * mag + self.primary.vel
            
    def findEV(self):
        #Uhhhhhhhhhhhhhhhhhhhh
        if self.primary != None:
            return abs(self.vel) * math.sqrt((2*G*self.primary.mass)/distanceBetween(self.pos, self.primary.pos)) 
        else:
            return 0
        
    def attract(self):
        
        totalForce = Vector2(0, 0)
        
        body = self.primary
        if body != None:  
            distance = math.sqrt((body.pos.x - self.pos.x) ** 2 + (body.pos.y - self.pos.y) ** 2)
            
            if distance < body.influenceRadius:
                direction = Vector2(body.pos.x - self.pos.x, body.pos.y - self.pos.y)
                direction.normalize()
                
                
                #F=G(m1*m2)/r^2
                num1 = self.mass * body.mass * G
                
                gForce = num1/(distance ** 2)
                gForce = direction * gForce
                totalForce = totalForce + gForce
        
        return totalForce
    
    def findInfluencers(self):
        influencers = []
        for body in objects:
            if distanceBetween(self.pos, body.pos) < body.influenceRadius:
                if body is not self:
                    influencers.append(body)
        return influencers
    
    def findPrimary(self):
        closest = self.findInfluencers()
        primary = nearest(closest)
        
        if primary != None:
            self.primary = primary        
        
    def draw(self):
        arcade.draw_circle_filled(self.pos.x, self.pos.y, self.drawnRadius, arcade.color.WHITE)
        
    def update(self):
        
        self.escapeVel = self.findEV()
        
        #self.findPrimary()   
        
        gForce = self.attract()
        
        #F = ma
        #a = F/m
        
        #Newton's Second Law
        self.acc = gForce/self.mass
        
        self.vel += self.acc
        if self.primary != None:
            if self.primary != self:
                pass
            
        self.pos += self.vel
        


objects.append(PlanetaryObject(Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), Vector2(0, 0), 100000, 2000, "Sun"))

objects.append(PlanetaryObject(Vector2(840, SCREEN_HEIGHT/2), Vector2(0, -1.5), 150, 30, "Earth"))

#objects.append(PlanetaryObject(Vector2(860, SCREEN_HEIGHT/2), Vector2(0, 0), 10, 0, "Moon"))

objects.append(PlanetaryObject(Vector2(970, SCREEN_HEIGHT/2), Vector2(0, -1), 100, 10, "Planet2"))


for i in objects:
    i.setup()
        

class Simulation(arcade.Window):
    
    def __init__(self, x, y, title):
        super().__init__(x, y, title)
        
        arcade.set_background_color(arcade.color.BLACK)
        self.selected = None
        
    def on_draw(self):
        if hasattr(objects[0].primary, "name"):
            print(objects[0].primary.name)
        arcade.start_render()
        buffer = 10
        text_size = 15
        spacing = text_size + buffer
        if hasattr(self.selected, "name"):
            arcade.draw_text(f"Selected Body: {self.selected.name} \nPosition: ({int(self.selected.pos.x)}, {int(self.selected.pos.y)}) \nVelocity: ({int(self.selected.vel.x)}, {int(self.selected.vel.y)}) \nSpeed: {int(abs(self.selected.vel))} \nEscape Velocity: {int(abs(self.selected.escapeVel))}", 
                             buffer, 
                             SCREEN_HEIGHT - spacing, 
                             arcade.color.WHITE, 
                             text_size, 
                             width=300,
                             multiline=True)
        else: 
            arcade.draw_text(f"Selected Body: {self.selected}", buffer, SCREEN_HEIGHT - spacing, arcade.color.WHITE, text_size)
        
        for body in objects:
            body.draw()
        
    def on_update(self, deltaTime):
        
        for body in objects:
            body.update()
            
    def on_mouse_press(self, x, y, key, mod):
        
        mousePos = Vector2(x, y)
        
        for body in objects:
            if distanceBetween(mousePos, body.pos) < body.drawnRadius + CLICK_BUFFER:
                self.selected = body
                print(self.selected.name)
            
        
        
if __name__ == "__main__":
    window = Simulation(SCREEN_WIDTH, SCREEN_HEIGHT, "Title goes here")
    arcade.run()