from icecream import ic
import pygame
import sys
import time
from random import choice,randint
import copy

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
def compute_num_matching_points(rect1,rect2):
    rect1.sort()
    rect2.sort()
    both = []

    for point in rect1:
        if point in rect2:
            both.append(point)
    return len(both)




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
        self.columns = []
        self.starting_number = randint(0,(self.screen_width/self.col_width)*(self.screen_height / self.row_height))
        # for col in range(0,self.col_count):
        #     self.columns.append(Column(col*cell_width, self.row_count))
        # self.nodes = []
        #self.flashers = set



# Initialize pygame
pygame.init()

def main():
    # Main loop for the screensaver
    canvas=Canvas()
    h = canvas.row_height
    w = canvas.col_width
    frame_count=1
    rect_list=[]
    rect_points_list=[]
    white_rects=[]
    white_rects_new=[]
    running = True
    while running:
        ic(frame_count)
        canvas.screen.fill(get_color("BLACK"))
        for row in range(canvas.row_count):
            for col in range(canvas.col_count):
                # Calculate the top-left corner of each cell
                x = col * canvas.col_width
                y = row * canvas.row_height
                # Draw the cell (you can adjust the color as needed)

                rect_points_real = [(x,y),(x+w,y),(x+w,y+h),(x,y+h)]
                # if randint(1,3) ==2:
                #     color = get_color("random")

                # else:
                color = (20,20,20)


                rect_points_list.append(rect_points_real)
                pygame.draw.rect(canvas.screen, color, (x, y, canvas.col_width, canvas.row_height), 1) 



        starting_rect_points= rect_points_list[canvas.starting_number]
        #ic(starting_rect_points)
 
        if frame_count ==1:
 
            pygame.draw.polygon(canvas.screen, get_color("WHITE"),starting_rect_points,1)
            white_rects.append(starting_rect_points)
            
        else:
            if white_rects: # if the white rects list has the starting cell
                previous_white_list = copy.copy(white_rects) #set the 'previous whites' list to it (the one cell)
            else: #if white rects has been cleared by me
                previous_white_list = copy.copy(white_rects_new)

            for wr in previous_white_list:
                #wr = [(x,y),(x+w,y),(x+w,y+h),(x,y+h)]
                x = wr[0][0]
                y = wr[0][1]
                
                top=[(x,y-h),(x+w,y-h),(wr[1]),(wr[0])]
                right=[(wr[1]),(x+2*w,y),(x+2*w,y+h),(wr[2])]
                left=[(x-w,y),(wr[0]),(wr[3]),(x-w,y+h)]
                bottom=[(wr[3]),(wr[2]),(x+w,y+2*h),(x,y+2*h)]
                new=[top,right,left,bottom]

                for new_rect in new:
                    if new_rect not in previous_white_list:
                        pygame.draw.polygon(canvas.screen,get_color("WHITE"),new_rect,1)
                        white_rects_new.append(new_rect)
                
                white_rects = []


   





        # Event handling (check for user input to stop the screensaver)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                running = False  # Exit on any key press or mouse click


        # Draw the red square
        #pygame.draw.rect(screen, get_color("RED"), (square_x, square_y, square_size, square_size))

        # # Update the screen
        # if frame_count % 4 == 0:
        pygame.display.flip()
        frame_count+=1
        #pygame.display.update()
        # Set the frame rate
        pygame.time.Clock().tick(1)

# Quit pygame and exit
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()