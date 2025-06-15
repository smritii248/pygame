import pygame
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Rectangle Transformations")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

rect = [(0, 0), (100, 0), (100, 60), (0, 60)]
def translate(points, tx, ty):
    return [(x + tx, y + ty) for x, y in points]

def scale(points, sx, sy, center=(0, 0)):
    cx, cy = center
    return [((x - cx) * sx + cx, (y - cy) * sy + cy) for x, y in points]

def rotate(points, angle_deg, center=(0, 0)):
    angle_rad = math.radians(angle_deg)
    cos_theta = math.cos(angle_rad)
    sin_theta = math.sin(angle_rad)
    cx, cy = center
    rotated = []
    for x, y in points:
        x -= cx
        y -= cy
        x_new = x * cos_theta - y * sin_theta
        y_new = x * sin_theta + y * cos_theta
        rotated.append((x_new + cx, y_new + cy))
    return rotated


def draw_polygon(points, color):
    pygame.draw.polygon(screen, color, points, 2)


clock = pygame.time.Clock()
angle = 0
running = True


tx, ty = 350, 250

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    translated = translate(rect, tx, ty)
    rotated = rotate(translated, angle, center=(tx + 50, ty + 30))  
    scaled = scale(rotated, 1.5, 1.5, center=(tx + 50, ty + 30))

  
    draw_polygon(translated, BLUE)   
    draw_polygon(scaled, RED)        

    angle += 1  

    pygame.display.flip()
    clock.tick(60)

pygame.quit()











