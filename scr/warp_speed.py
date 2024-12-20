from icecream import ic
import pygame
import sys
import time
from random import choice,randint
import copy
import math


# num_drawing_frames=30
tickrate = 120

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

def get_color(name):
    if name == "random":
        color = choice(list(colors.values()))
        return color
    color = colors.get(name)
    return color
def divide(n,d):
    return d and n / d

def distance(point,center):
    d = math.sqrt((point.x-center.x)**2 + (point.y-center.y)**2)
    return d


class Canvas:
    """
    Represents the whole screen and stores its height and width. Gets
    overwritten whenever the screen resizes. Serves as a container for columns.
    """

    def __init__(self):

        self.screen_width = 1920//2 # Each column is 10 pixels wide
        self.screen_height = 1080//2 # Each row is 20 pixels high
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))#,pygame.FULLSCREEN)
        self.row_height = 20
        self.col_width = 20
        self.col_count = self.screen_width // self.col_width
        self.row_count = self.screen_height // self.row_height
        self.num_cells = self.col_count*self.row_count
        self.columns = []
        self.starting_number = randint(1,self.num_cells+1)

        self.center = pygame.math.Vector2(self.screen_width // 2,self.screen_height // 2)
        # for col in range(0, self.col_count):
        #     self.columns.append(Column(col*self.col_width))
        self.stars =[]
    def draw_center(self):
        pygame.draw.line(self.screen, get_color("RED"), self.center,self.center)

class Star:

    def __init__(self,c):
        self.point=pygame.math.Vector2(self.get_random_point(c))
        self.color =get_color("WHITE")
        self.center_vector=self.get_center_vector(c.center).normalize()


    def get_random_point(self,c):
        x = randint(1,c.screen_width)
        y = randint(1,c.screen_height)
        return (x,y)
    
    def get_multiplier(self,c,val):
        return distance(self.point,c.center)*val
    
    def draw(self,c):
        x =(self.center_vector)*self.get_multiplier(c,0.08)
        pygame.draw.line(c.screen, self.color, self.point,self.point-x,1)
        return self.point - x
    

    def get_center_vector(self,center):
        v1 = (self.point.x - center.x)
        v2 = (self.point.y - center.y)
        return pygame.math.Vector2(v1,v2)



# Initialize pygame
pygame.init()

def main():
    # Main loop for the screensaver
    c=Canvas()
    frame_count=1

    running = True
    paused = False
    manual_step =False
    
    while running:
        if not paused or manual_step:
            c.screen.fill(get_color("BLACK"))

            star1= Star(c)
            star2= Star(c)
            star3= Star(c)
            star4= Star(c)
            c.stars.append(star1)
            c.stars.append(star2)
            c.stars.append(star3)
            c.stars.append(star4)

            c.draw_center()

            for star in c.stars:
                star.point += star.center_vector * star.get_multiplier(c,0.04)

                endpoint = star.draw(c)
                #ic(star.point,endpoint)
                d = distance(star.point,endpoint)
                if not 0-d < star.point.x < c.screen_width+d or not 0-d < star.point.y < c.screen_height+d:
                    #print("removed")
                    c.stars.remove(star)







            pygame.display.flip()
            if not paused:
                frame_count += 1
                pygame.time.Clock().tick(tickrate)
            manual_step = False  # Reset the manual step flag after updating

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Press 'Q' to quit
                    running = False
                elif event.key == pygame.K_p:  # Press 'P' to pause/unpause
                    paused = not paused
                    print(f"Paused: {paused}")
                elif event.key == pygame.K_RIGHT and paused:  # Step manually if paused
                    manual_step = True
                    print("Manually stepped frame.")
                elif event.key == pygame.K_r:  # Reset frame count
                    frame_count = 1
                    print("Frame count reset.")      

                
            


            # # Event handling (check for user input to stop the screensaver)
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         running = False
            #     elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            #         running = False  # Exit on any key press or mouse click


        # Draw the red square
        #pygame.draw.rect(screen, get_color("RED"), (square_x, square_y, square_size, square_size))

        # # # Update the screen
        # # if frame_count % 4 == 0:
        #     pygame.display.flip()
        #     frame_count+=1
        #     #pygame.display.update()
        #     # Set the frame rate
        #     pygame.time.Clock().tick(15)

# Quit pygame and exit
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()