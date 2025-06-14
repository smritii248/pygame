import sys
import pygame
pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mid-point Circle Algorithm")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

def draw_circle_points(xc, yc, x, y):
    screen.set_at((xc + x, yc + y), RED)
    screen.set_at((xc - x, yc + y), RED)
    screen.set_at((xc + x, yc - y), RED)
    screen.set_at((xc - x, yc - y), RED)
    screen.set_at((xc + y, yc + x), RED)
    screen.set_at((xc - y, yc + x), RED)
    screen.set_at((xc + y, yc - x), RED)
    screen.set_at((xc - y, yc - x), RED)

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r
    draw_circle_points(xc, yc, x, y)
    while x < y:
        x = x + 1
        if p < 0:
            p = p + 2 * x + 3
        else:
            y = y - 1
            p = p + 2 * (x - y) + 5
        draw_circle_points(xc, yc, x, y)  

def main():
    screen.fill(WHITE)
    center_x = width // 2
    center_y = height // 2
    radius = 150
    midpoint_circle(center_x, center_y, radius)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()











