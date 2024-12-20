from icecream import ic
import pygame
import sys
import time
from random import choice,randint
import copy


num_drawing_frames=30
tickrate = 30

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


class Canvas:
    """
    Represents the whole screen and stores its height and width. Gets
    overwritten whenever the screen resizes. Serves as a container for columns.
    """

    def __init__(self):

        self.screen_width = 1920#/2 # Each column is 10 pixels wide
        self.screen_height = 1080#//2 # Each row is 20 pixels high
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))#,pygame.FULLSCREEN)
        self.row_height = 20
        self.col_width = 20
        self.col_count = self.screen_width // self.col_width
        self.row_count = self.screen_height // self.row_height
        self.num_cells = self.col_count*self.row_count
        self.columns = []
        self.starting_number = randint(1,self.num_cells+1)
        for col in range(0, self.col_count):
            self.columns.append(Column(col*self.col_width))
        # self.cells = []
        self.blossoms=[]


class Column:

    """
    Creates nodes (points that move down the screen) that are then stored in
    canvas.nodes. Countdown timer determines time to spawn new node.
    """

    def __init__(self, x_coord):
        self.drawing = None  # None means not yet. Later will be True or False
        self.x_coord = x_coord #0->128 step: 15
        self.num_drawing_frames = num_drawing_frames
        self.timer = None
        self.set_col_timer()



    def set_col_timer(self):
        self.timer =  randint(self.num_drawing_frames*2, self.num_drawing_frames*12+1)
        


class Cell:

    def __init__(self,x_coord,y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

class Blossom:
    def __init__(self):
        self.start_cell = None
        self.num_drawing_frames = num_drawing_frames
        self.cells=[]
        self.cardinal_cells=[]
        self.step=0
        self.blossom_color = get_color("random")


    def get_start_cell(self,canvas,column):
        row = randint(1,canvas.row_count+1)
        #col = randint(1,canvas.col_count+1)
        x = column.x_coord
        y = row*canvas.row_height
        start_cell = Cell(x,y)
        self.start_cell = start_cell
        #self.cells.append(start_cell)
        return start_cell

    def get_cardinal_cells(self,canvas):
        self.cardinal_cells=[]
        d = self.step-1
        cell_size = canvas.row_height #could be col_width as well since they are squares
        total_distance=cell_size*d
        startx=self.start_cell.x_coord
        starty=self.start_cell.y_coord
        north = Cell(startx,starty-total_distance)
        south = Cell(startx,starty+total_distance)
        east =  Cell(startx+total_distance,starty)
        west =  Cell(startx-total_distance,starty)
        cardinal_cells = [north,east,south,west]
        for ccell in cardinal_cells:
            self.cells.append(ccell)
            self.cardinal_cells.append(ccell)
        
        

    def get_diagonal_cells(self,canvas):
        cardinal_cells = self.cardinal_cells
        cell_size = canvas.row_height #could be col_width as well since they are squares
        num_diagonal_cells = self.step-2
        
        ccell = cardinal_cells[0]
        for i in range(1,num_diagonal_cells+1):
            self.cells.append(Cell(ccell.x_coord+(cell_size*i),ccell.y_coord+(cell_size*i)))
        ccell = cardinal_cells[1]
        for i in range(1,num_diagonal_cells+1):
            self.cells.append(Cell(ccell.x_coord-(cell_size*i),ccell.y_coord+(cell_size*i)))
        ccell = cardinal_cells[2]
        for i in range(1,num_diagonal_cells+1):
            self.cells.append(Cell(ccell.x_coord-(cell_size*i),ccell.y_coord-(cell_size*i)))
        ccell = cardinal_cells[3]
        for i in range(1,num_diagonal_cells+1):
            self.cells.append(Cell(ccell.x_coord+(cell_size*i),ccell.y_coord-(cell_size*i)))
        
        return 


    def draw_cell(self,cell,canvas):
        step =self.step 
        num_drawing_frames = self.num_drawing_frames
        v = 255
        r = None
        color_blossom = False
        decrement =v//num_drawing_frames
        if r:
            color = r
        elif color_blossom:
            color  = self.blossom_color
            color2 = tuple(max(0, min(255, int(c * 0.99))) for c in color)
            self.blossom_color = color2
                
        elif step==0:
            value = v
            color = (value,value,value)
        else:
            value = (v-(decrement*(step-1)))
            color = (value,value,value)
        
        if 0 > cell.x_coord > canvas.screen_width or 0 > cell.y_coord > canvas.screen_height:
            return
        else:
            pygame.draw.rect(canvas.screen, color, (cell.x_coord, cell.y_coord, canvas.col_width, canvas.row_height), 1) 



# Initialize pygame
pygame.init()

def main():
    # Main loop for the screensaver
    canvas=Canvas()
    frame_count=1



    running = True
    #canvas.screen.fill(get_color("BLACK"))

    paused = False
    manual_step =False

    while running:
        if not paused or manual_step:
            canvas.screen.fill(get_color("BLACK"))
            for row in range(canvas.row_count):
                for col in range(canvas.col_count):
                    # Calculate the top-left corner of each cell
                    x = col * canvas.col_width
                    y = row * canvas.row_height
                    color = (20,20,20)
                    pygame.draw.rect(canvas.screen, color, (x, y, canvas.col_width, canvas.row_height), 1) 
            for col in canvas.columns:
                if col.timer ==0:# and col.x_coord ==canvas.columns[40].x_coord:
                    #ic(col.x_coord)
                    blossom=Blossom() #create blossom obj
                    canvas.blossoms.append(blossom) #add it to list of all blossoms
                    blossom.get_start_cell(canvas,col) #get a start cell and add to b attr
                    blossom.draw_cell(blossom.start_cell, canvas)  #draw start cell
                    col.set_col_timer() #reset the col timer
                    blossom.step +=1     
                else:
                    col.timer -=1
                                    #incr the blossom step
            # ic(len(canvas.blossoms))
            for b in canvas.blossoms:
                #ic(b.__dict__)

                if b.step == 1:
                    b.get_cardinal_cells(canvas) #add card cells to cardinal cells list and full cells list for the blossom
                    for cell in b.cells:
                        b.draw_cell(cell,canvas) #draw all the cells in main cell list (should just be the cardinal cell at this point)
                    b.cardinal_cells = []  #set the cardinal cells list to blank for the next step
                    b.step +=1
                elif b.step >= 2 and b.step <= b.num_drawing_frames:
                    b.get_cardinal_cells(canvas) 
                    b.get_diagonal_cells(canvas)
                    for cell in b.cells:
                        b.draw_cell(cell,canvas)
                    b.cells = []
                    b.step +=1

                else:# b.step > b.num_drawing_frames:
                    canvas.blossoms.remove(b)
                # else:
                #     b.step =+1
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