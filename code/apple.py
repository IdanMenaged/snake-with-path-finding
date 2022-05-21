import pyglet
import random
import CONSTANTS

def main():
    apple = Apple()
    
    @CONSTANTS.WINDOW.event
    def on_draw():
        apple.draw_self()
        
    pyglet.app.run()

class Apple:
    def __init__(self):
        self.x, self.y = random.randrange(0, CONSTANTS.WINDOW.width-CONSTANTS.TILE_SIZE, CONSTANTS.TILE_SIZE), random.randrange(0, CONSTANTS.WINDOW.height-CONSTANTS.TILE_SIZE, CONSTANTS.TILE_SIZE)
        self.form = pyglet.shapes.Rectangle(x=self.x, y=self.y, width=20, height=20, color=(255, 0, 0))
    
    def draw_self(self):
        self.form.draw()

if __name__ == '__main__':
    main()
    