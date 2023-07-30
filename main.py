from tkinter import Label, Tk, Canvas, ALL
from random import randrange

# Constants for game configuration
GAME_HEIGHT = 600
GAME_WIDTH = 600
GRID_SIZE = 40
INITIAL_LENGTH = 3
MOVEMENT_DELAY = 90

class Snake:
    def __init__(self, canvas):
        # Initialize the snake's attributes
        self.score = 0
        self.coords = []
        self.squares = []
        self.direction = "down"
        
        # Create the initial segments of the snake
        for i in range(INITIAL_LENGTH - 1, -1, -1):
            self.coords.append([0, i * 40])

        # Create rectangles on the canvas to represent each segment of the snake
        for coords in self.coords:
            x = coords[0]
            y = coords[1]
            rectangle = canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill="green", tag="snake")
            self.squares.append(rectangle)
            
class Fruit:
    def __init__(self, canvas, snake):
        # Place the fruit on a random position on the canvas, avoiding collision with the snake
        not_placed = True
        while not_placed:
            correct = True
            self.x = randrange(0, GAME_WIDTH, GRID_SIZE)
            self.y = randrange(0, GAME_HEIGHT, GRID_SIZE)
            for (x, y) in snake.coords:
                if self.x == x and self.y == y:
                    correct = False
            not_placed = not correct

        # Create a rectangle on the canvas to represent the fruit
        canvas.create_rectangle(self.x, self.y, self.x + GRID_SIZE, self.y + GRID_SIZE, fill="red", tag="fruit")

def gen_grid(canvas):
    # Generate a grid on the canvas using rectangles
    for x in range(0, GAME_WIDTH, GRID_SIZE):
        for y in range(0, GAME_HEIGHT, GRID_SIZE):
            canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE)

def movement(window, snake, canvas, fruit, label):
    # Move the snake according to its current direction
    x, y = snake.coords[0]
    if snake.direction == "down":
        y += GRID_SIZE
    elif snake.direction == "up":
        y -= GRID_SIZE
    elif snake.direction == "left":
        x -= GRID_SIZE
    else:
        x += GRID_SIZE
    snake.coords.insert(0, [x, y])
    snake.squares.insert(0, canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill="green", tag="snake"))
    
    # Check if the snake has collided with the fruit or if it has collided with a boundary
    if x != fruit.x or y != fruit.y:
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
        del snake.coords[-1]
    else:
        canvas.delete("fruit")
        snake.score += 1
        label.config(text=f"Score: {snake.score}")
        fruit = Fruit(canvas, snake)
    
    # Check if the snake has collided with itself
    if collision_check(snake):
        game_over(canvas, snake, label)
        
    # Schedule the next movement using the given delay
    window.after(MOVEMENT_DELAY, movement, window, snake, canvas, fruit, label)
    
def collision_check(snake):
    # Check if the snake has collided with the boundaries of the canvas
    x, y = snake.coords[0]
    if x > GAME_WIDTH - GRID_SIZE or x < 0 or y > GAME_HEIGHT - GRID_SIZE or y < 0:
        return True
    for (s_x, s_y) in snake.coords[1:]:
        if x == s_x and y == s_y:
            return True

def change_direction(direction, snake):
    # Change the direction of the snake, as long as it does not result in a U-turn
    if direction == "right":
        if snake.direction == "left":
            return
    elif direction == "left":
        if snake.direction == "right":
            return
    elif direction == "up":
        if snake.direction == "down":
            return
    elif direction == "down":
        if snake.direction == "up":
            return
    snake.direction = direction

def game_over(canvas, snake, label):
    canvas.delete("snake")
    snake.score = 0
    label.config(text=f"Score: {snake.score}")
    snake.__init__(canvas)
    

def main():
    window = Tk()
    score = 0
    window.title("Snake!")
    canvas = Canvas(window, width=GAME_WIDTH, height=GAME_HEIGHT, background="#013220")
    canvas.pack()
        
    # Generate the grid and create the snake and fruit objects
    gen_grid(canvas)
    snake = Snake(canvas)
    fruit = Fruit(canvas, snake)
    label = Label(text=f"Score: {snake.score}")
    label.pack()
    # Start moving the snake
    movement(window, snake, canvas, fruit, label)
        
    # Bind the arrow keys for changing the snake's direction
    window.bind("<w>", lambda event : change_direction("up", snake))
    window.bind("<a>", lambda event : change_direction("left", snake))
    window.bind("<s>", lambda event : change_direction("down", snake))
    window.bind("<d>", lambda event : change_direction("right", snake))
    window.bind("<W>", lambda event : change_direction("up", snake))
    window.bind("<A>", lambda event : change_direction("left", snake))
    window.bind("<S>", lambda event : change_direction("down", snake))
    window.bind("<D>", lambda event : change_direction("right", snake))

    # Start the main event loop
    window.mainloop()

if __name__ == "__main__":
    main()