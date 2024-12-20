from icecream import ic
import pygame
import sys
from random import choice, randint
import time

colors = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "GREEN2":(14, 110, 14),
    "BLUE": (0, 0, 255),
    "BLUE2":(85, 85, 242),
    "YELLOW": (255, 255, 0),
    "CYAN": (0, 255, 255),
    "MAGENTA": (255, 0, 255),
    "ORANGE": (255, 165, 0),
    "PURPLE": (128, 0, 128),
    "PINK": (255, 192, 203),
    "BROWN": (139, 69, 19),
    "GRAY": (120, 120, 120),
    "GRAY2": (170, 170, 170),
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
    "TAN": (210, 180, 140),
    "GREYX": (118, 118, 118),
    "GREYX2": (118, 118, 118)

}
ox=2
oy=6

# param combos ox,oy,fontsize,colwidth,rowheight
# 2,6,20,40,20

pygame.font.init()
font = pygame.font.Font(r'C:\Users\evant\Desktop\sandbox\scr\msgothic.ttf', 20)  # None for default font, 36 for size
charsets={
    'a': 'qwertyuiopasdfghjklzxcvbnm',
    'A': 'QWERTYUIOPASDFGHJKLZXCVBNM',
    'c': 'абвгдежзиклмнопрстуфхцчшщъыьэюя',
    'C': 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',
    'e': '☺☻✌♡♥❤⚘❀❃❁✼☀✌♫♪☃❄❅❆☕☂★',
    'g': 'αβγδεζηθικλμνξοπρστυφχψως',
    'G': 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ',
    'k': 'ｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ',
    'm': 'ｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ1234567890',
    'm2' :'1234567890-=*_+|:<>"-=*_+|:<>"-=*_+|:<>"-=*_+|:<>"',
    'n': '1234567890',
    'o': 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890`-=~!@#$%^&*()_+[]{}|\\;\':",./<>?"',
    'p': 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890-=!@#$%^&*()+[]{}|\\;\':",.<>?"ｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ1234567890',
    'P': '',
    'r': 'mcclllxxxxvvvvviiiiii',
    'R': 'MCCLLLXXXXVVVVVIIIIII',
    's': '-=*_+|:<>"',
    'S': '`-=~!@#$%^&*()_+[]{}|\\;\':",./<>?"'
}

#chars="asdjkl;asjdflkasfasdkf;jaskdlfｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ"
#chars ="Alexa"
chars = charsets.get('p')


def get_char():
    return chars[randint(0, len(chars)-1)]

def render_char(char,color):
    character = font.render(char, True, get_color(color))  # White color
    return character

def get_color(name):
    if name == "random":
        color = choice(list(colors.values()))
        return color
    color = colors.get(name)
    return color



class Canvas:

    def __init__(self):
        # Cell dimensions

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = 1920 # Each column is 10 pixels wide
        self.screen_height = 1080 # Each row is 10 pixels high
        self.col_width = 40
        self.row_height = 22

        #set col width to 20 and row height to 10 for cool efect

        self.col_count = self.screen_width//self.col_width
        self.row_count = self.screen_height//self.row_height
        self.columns = []
        for col in range(0, self.col_count):
            self.columns.append(Column(col*self.col_width, self.row_count))
        self.nodes = []


class Column:
    """
    Creates nodes (points that move down the screen) that are then stored in
    canvas.nodes. Countdown timer determines time to spawn new node.
    """

    def __init__(self, x_coord, row_count):
        self.drawing = None  # None means not yet. Later will be True or False
        self.x_coord = x_coord #0->128 step: 15
        self.timer = randint(1, row_count)#1->36
        self.async_speed = randint(1, 3)

    def spawn_node(self, canvas):
        """
        Creates nodes: points that move down the screen either writing or
        erasing characters as they go down
        """
        # if args.single_wave and self.drawing is False:
        #     return

        self.drawing = not self.drawing

        mult = 1

        if self.drawing:
            # "max_range" prevents crash with very small terminal height
            max_range = max((3 * mult), ((canvas.row_count - 3) * mult))
            self.timer = randint(3 * mult, max_range) #3 -> 32


        else:
            self.timer = randint(1 * mult, canvas.row_count * mult) #1 -> 32
        
        x = self.x_coord
        n_type = 'eraser'
        async_speed = self.async_speed
        white = False
        if self.drawing:
            n_type = 'writer'
            if randint(0, 2) == 0: #%50
                white = True
        #create a node 
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



def draw(node, canvas):
    """
    Draws characters, included spaces to overwrite/erase characters.
    """
    color_pair="GRAY"
    leader_color= "RED"
    def get_color_from_pair(color):
        
        if randint(0,3)<2:
            return color
        else:
            return color+'2'
        
    color = get_color_from_pair(color_pair)    
    y = node.y_coord+oy
    x = node.x_coord+ox
    character = ' '
    #add ability to set a color pair, ie green and a slightly diff shade of green for each base color
    # if node.last_char is not None:
    if node.n_type =='eraser':
        color = "BLACK"
        #canvas.screen.blit(render_char('', color), (x, y - canvas.row_height))
        pygame.draw.rect(canvas.screen, color, (x,y,canvas.col_width,canvas.row_height))
    if node.n_type == 'writer':
        #color = "GREEN"
        if not node.white and node.last_char:
            # Special green character for overwriting last white one
            # at bottom of column that was not being overwritten.
            character = node.last_char
        else:
            character = get_char()
        if node.white:
            color = leader_color



    # Draw the character
    canvas.screen.blit(render_char(character,color),(x,y))


    if node.white:
        if node.last_char:
            # If it's a white node, also write a green character above
            # to overwrite last white character
            pygame.draw.rect(canvas.screen, "BLACK", (x,y-canvas.row_height,canvas.col_width,canvas.row_height))

            canvas.screen.blit(render_char(node.last_char,get_color_from_pair(color_pair)),(x,y-canvas.row_height))
        node.last_char = character
        #if node.y_coord ?


def main():
# Main loop for the screensaver
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font(r'C:\Users\evant\Desktop\sandbox\scr\msgothic.ttf', 30)  # None for default font, 36 for size

    canvas = Canvas()
    running = True
    while running:
        ##########canvas.screen.fill(get_color("BLACK"))
        # for colls in range(canvas.col_count):
        #     for row in range(canvas.row_count):
        #         x = colls * 15
        #         y = row * 30
        #         pygame.draw.rect(canvas.screen, (18, 18, 17), (x,  y, 15, 30), 1)  # White grid lines


        for col in canvas.columns:

            if col.timer == 0:
                col.spawn_node(canvas)
            col.timer -= 1

            for node in canvas.nodes:
                if node.x_coord == col.x_coord:
                    draw(node,canvas)
                    node.y_coord += canvas.row_height

                        # Mark old nodes for deletion
                    if node.y_coord > canvas.row_count*canvas.row_height:
                        if node.white:
                            # Stop white nodes from staying 'stuck' on last row.
                            # Creates a special green node with a last_char
                            # attribute to overwrite last white node.
                            node.white = False
                            node.y_coord -= 1
                        else:
                            node.expired = True
                # Rewrite nodes list without expired nodes
            canvas.nodes = [node for node in canvas.nodes if not node.expired]

        
        # Event handling (check for user input to stop the screensaver)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                running = False  # Exit on any key press or mouse click


    # Update the screen
        pygame.display.flip()

        # Set the frame rate
        pygame.time.Clock().tick(30)

    # Quit pygame and exit
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()