import pyglet
import CONSTANTS

def main():
    snake = Snake()
    
    @CONSTANTS.WINDOW.event
    def on_draw():
        snake.draw_self()
        
    @CONSTANTS.WINDOW.event
    def on_key_press(symbol, modifiers):
        pass
        
    pyglet.app.run()

class Snake:
    def __init__(self):
        self.x, self.y = 0, 0
        self.form = pyglet.shapes.Rectangle(x=self.x, y=self.y, width=20, height=20, color=(0, 255, 0))
    
    def draw_self(self):
        self.form.draw()
        
    def cal_move(self, dir:str):
        """gets new x and y values WITHOUT CHANGING THE ACTUAL POSITION
        to change it you need to set the self.x and self.y attributes to the returned values
        that is done so that we can calculate different moves without actually executing them

        Args:
            dir (str): left right up and down

        Raises:
            Exception: if dir is not one of those 4 values

        Returns:
            tuple: new x, new y
        """
        
        new_x, new_y = self.x, self.y
        match dir:
            case 'right':
                new_x = self.x + CONSTANTS.TILE_SIZE
            case 'left':
                new_x = self.x - CONSTANTS.TILE_SIZE
            case 'up':
                new_y = self.y + CONSTANTS.TILE_SIZE
            case 'down':
                new_y = self.y - CONSTANTS.TILE_SIZE
            case _:
                raise Exception(f'INVALID DIRECTION - {dir}')
        return new_x, new_y

if __name__ == '__main__':
    main()
    