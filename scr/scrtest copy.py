import pygame

# Initialize pygame
pygame.init()

# Set up the display (assuming 95 columns and 53 rows)
screen_width = 95 * 10  # Each column is 10 pixels wide
screen_height = 53 * 10  # Each row is 10 pixels high
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the window caption
pygame.display.set_caption("Grid with 53 Rows and 95 Columns")

# Cell dimensions
cell_width = screen_width // 95
cell_height = screen_height // 53

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with a color (black in this case)
    screen.fill((0, 0, 0))
    
    # Draw the grid
    for row in range(53):
        for col in range(95):
            # Calculate the top-left corner of each cell
            x = col * cell_width
            y = row * cell_height
            # Draw the cell (you can adjust the color as needed)
            pygame.draw.rect(screen, (255, 255, 255), (x, y, cell_width, cell_height), 1)  # White grid lines
    
    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
