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
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
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


# Create a square
square_size = 50
square_x = 100
square_y = 100
square_speed_x = 50
square_speed_y = 3
# Define the font and size
font = pygame.font.Font("scr\\JetBrainsMono-Bold.ttf", 30)  # None for default font, 36 for size


# Main loop for the screensaver
running = True
while running:
    screen.fill(get_color("BLACK"))
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
    # Move the square
    # square_x += square_speed_x
    # square_y += square_speed_y

    # # Bounce the square off the screen edges
    # if square_x < 0 or square_x + square_size > screen.get_width():
    #     square_speed_x = -square_speed_x
    # if square_y < 0 or square_y + square_size > screen.get_height():
    #     square_speed_y = -square_speed_y

    # Fill the screen with black


    # Draw the red square
    #pygame.draw.rect(screen, get_color("RED"), (square_x, square_y, square_size, square_size))

    # Update the screen
    pygame.display.flip()

    # Set the frame rate
    pygame.time.Clock().tick(30)

# Quit pygame and exit
pygame.quit()
sys.exit()
