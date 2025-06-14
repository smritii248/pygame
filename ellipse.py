import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)

def plot_ellipse_points(screen, xc, yc, x, y, color):
    screen.set_at((xc + x, yc + y), color)
    screen.set_at((xc - x, yc + y), color)
    screen.set_at((xc + x, yc - y), color)
    screen.set_at((xc - x, yc - y), color)

def midpoint_ellipse(screen, xc, yc, rx, ry, color):
    x = 0
    y = ry

    dx = 2 * (ry * ry) * x
    dy = 2 * (rx * rx) * y

    p1 = (ry * ry) - (rx * rx * ry) + (0.25 * rx * rx)
    while dx < dy:
        plot_ellipse_points(screen, xc, yc, x, y, color)
        x += 1
        dx = 2 * (ry * ry) * x
        if p1 < 0:
            p1 += (ry * ry) * (2 * x + 1)
        else:
            y -= 1
            dy = 2 * (rx * rx) * y
            p1 += (ry * ry) * (2 * x + 1) - dy

    p2 = (ry * ry) * (x + 0.5) ** 2 + (rx * rx) * (y - 1) ** 2 - (rx * rx * ry * ry)
    while y >= 0:
        plot_ellipse_points(screen, xc, yc, x, y, color)
        y -= 1
        dy = 2 * (rx * rx) * y
        if p2 > 0:
            p2 += (rx * rx) * (1 - 2 * y)
        else:
            x += 1
            dx = 2 * (ry * ry) * x
            p2 += dx - dy + (rx * rx)

def main():
    width, height = 600, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Midpoint Ellipse Drawing")
    screen.fill(WHITE)
    xc, yc = width // 2, height // 2
    rx, ry = 150, 100
    midpoint_ellipse(screen, xc, yc, rx, ry, RED)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()

















