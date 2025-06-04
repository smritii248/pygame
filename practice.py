
import sys
import pygame

# Initialize pygame
pygame.init()

# Set window size and title
width, height = 500, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("DDA Line Algorithm")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# DDA Line Drawing Function
def digital_differential(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    step = max(abs(dx), abs(dy))

    x_inc = dx / step
    y_inc = dy / step

    x, y = x1, y1
    for _ in range(int(step) + 1):  # Include last point
        pygame.draw.circle(win, BLACK, (round(x), round(y)), 1)
        x += x_inc
        y += y_inc

# Main loop
def main():
    win.fill(WHITE)

    # Coordinates (fit within 500x500 screen)
    x1, y1 = 50, 30
    x2, y2 = 450, 300  # Adjusted to stay within window bounds

    digital_differential(x1, y1, x2, y2)

    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Fixed '=' to '=='
                running = False

    pygame.quit()
    sys.exit()

# Corrected syntax for main call
if __name__ == "__main__":
    main()

    
    
 








