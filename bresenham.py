import sys
import pygame

pygame.init()
width, height = 500, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bresenham Line Algorithm (Using p)")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def bresenham_with_p(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    x, y = x1, y1

    if dx > dy:
        p = 2 * dy - dx
        for _ in range(dx + 1):
            pygame.draw.circle(win, BLACK, (x, y), 1)
            x = x + 1 if x1 < x2 else x - 1
            if p < 0:
                p = p + 2 * dy
            else:
                y = y + 1 if y1 < y2 else y - 1
                p = p + 2 * (dy - dx)
    else:
        p = 2 * dx - dy
        for _ in range(dy + 1):
            pygame.draw.circle(win, BLACK, (x, y), 1)
            y = y + 1 if y1 < y2 else y - 1
            if p < 0:
                p = p + 2 * dx
            else:
                x = x + 1 if x1 < x2 else x - 1
                p = p + 2 * (dx - dy)

def main():
    win.fill(WHITE)

    x1, y1 = 50, 50
    x2, y2 = 400, 300

    bresenham_with_p(x1, y1, x2, y2)

    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()







