import pygame
import sys
from random import choice, randint

def get_char():
    """
    Returns a random character from the active character set
    """
    return chars[randint(0, len(chars)-1)]

def render_char():
    text = font.render(get_char(), True, get_color("random"))  # White color
    return text
def get_color(name):
    if name == "random":
        color = choice(list(colors.values()))
        return color
    color = colors.get(name)
    return color









# Initialize pygame
pygame.init()

# Set the screen to full-screen mode

colors = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "YELLOW": (255, 255, 0),
    "CYAN": (0, 255, 255),
    "MAGENTA": (255, 0, 255),
    "ORANGE": (255, 165, 0),
    "PURPLE": (128, 0, 128),
    "PINK": (255, 192, 203),
    "BROWN": (139, 69, 19),
    "GRAY": (169, 169, 169),
    "LIGHT_GRAY": (211, 211, 211),
    "DARK_GRAY": (169, 169, 169),
    "TURQUOISE": (64, 224, 208),
    "LIME": (0, 255, 0),
    "VIOLET": (238, 130, 238),
    "OLIVE": (128, 128, 0),
    "NAVY": (0, 0, 128),
    "TEAL": (0, 128, 128),
    "CORAL": (255, 127, 80),
    "BEIGE": (245, 245, 220),
    "GOLD": (255, 215, 0),
    "INDIGO": (75, 0, 130),
    "PEACH": (255, 229, 180),
    "TAN": (210, 180, 140)
}


chars="10"


screen_width = 1920 # Each column is 10 pixels wide
screen_height = 1080 # Each row is 10 pixels high

screen = pygame.display.set_mode((screen_width, screen_height))

# Set the window caption
\
# Cell dimensions
cell_width = screen_width // 95
cell_height = screen_height // 53*2



# Define the font and size
font = pygame.font.Font("scr\\JetBrainsMono-Bold.ttf", 30)  # None for default font, 36 for size




class Canvas:
    """
    Represents the whole screen and stores its height and width. Gets
    overwritten whenever the screen resizes. Serves as a container for columns.
    """

    def __init__(self,screen):

        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        screen.fill(get_color("BLACK"))
        self.screen_width = 1920 # Each column is 10 pixels wide
        self.screen_height = 1080 # Each row is 20 pixels high
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        cell_width = screen_width // 95
        cell_height = screen_height // 53*2
        rows = 95
        cols = 53
        self.col_count = cols
        self.row_count = rows
        #self.size_changed = False
        self.columns = []
        #for col in range(0, cols, 2):
        for col in range(0,cols):
            self.columns.append(Column(col*cell_width, self.row_count))
        self.nodes = []
        #self.flashers = set()


class Column:
    """
    Creates nodes (points that move down the screen) that are then stored in
    canvas.nodes. Countdown timer determines time to spawn new node.
    """

    def __init__(self, x_coord, row_count):
        self.drawing = None  # None means not yet. Later will be True or False
        self.x_coord = x_coord
        self.timer = randint(1, row_count)
        self.async_speed = randint(1, 3)
        # if args.single_wave:
        #     # Speeds it up a bit
        #     self.timer = int(0.6 * self.timer)

    def spawn_node(self, canvas):
        """
        Creates nodes: points that move down the screen either writing or
        erasing characters as they go down
        """
        # if args.single_wave and self.drawing is False:
        #     return

        self.drawing = not self.drawing

        # Multiplier (mult) is for spawning slow-moving asynchronous nodes
        # less frequently in order to maintain their length
        if args.asynchronous:
            mult = self.async_speed
        else:
            mult = 1

        if self.drawing:
            # "max_range" prevents crash with very small terminal height
            max_range = max((3 * mult), ((canvas.row_count - 3) * mult))
            self.timer = randint(3 * mult, max_range)
            # if args.single_wave:
            #     # A bit faster for single wave mode
            #     self.timer = int(0.8 * self.timer)
        else:
            self.timer = randint(1 * mult, canvas.row_count * mult)

        x = self.x_coord
        n_type = 'eraser'
        async_speed = self.async_speed
        white = False
        if self.drawing:
            n_type = 'writer'
            if randint(0, 2) == 0:
                white = True

        canvas.nodes.append(Node(x, n_type, async_speed, white))


class Node:
    """
    A point that runs down the screen drawing or erasing characters.
    n_type    -> 'writer' or 'eraser'
    white     -> Bool. If True, a white char is written before the green one.
    last_char -> Stores last character, since white characters have to be
                     overwritten with the same one in green one.
    expired   -> Bool. If True, node is marked for deletion
    """

    def __init__(self, x_coord, n_type, async_speed, white=False):
        self.x_coord = x_coord
        self.y_coord = 0
        self.n_type = n_type
        self.white = white
        self.last_char = None
        self.expired = False
        self.async_speed = async_speed





# Main loop for the screensaver
running = True
while running:

    for row in range(53):
        for col in range(95):
            # Calculate the top-left corner of each cell
            x = col * cell_width
            y = row * cell_height
            # Draw the cell (you can adjust the color as needed)
            pygame.draw.rect(screen, (255, 255, 255), (x, y, cell_width, cell_height), 1)  # White grid lines
            screen.blit(render_char(),(x+1,y-1))
    # Event handling (check for user input to stop the screensaver)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            running = False  # Exit on any key press or mouse click


    # Draw the red square
    #pygame.draw.rect(screen, get_color("RED"), (square_x, square_y, square_size, square_size))

    # Update the screen
    pygame.display.flip()

    # Set the frame rate
    pygame.time.Clock().tick(30)

# Quit pygame and exit
pygame.quit()
sys.exit()
