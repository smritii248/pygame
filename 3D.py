import pygame
import sys
import math

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("3D Cube - Plot Style")
clock = pygame.time.Clock()

original_points = [
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1]
]

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

def rotate_x(p, a):
    x, y, z = p
    r = math.radians(a)
    return x, y * math.cos(r) - z * math.sin(r), y * math.sin(r) + z * math.cos(r)

def rotate_y(p, a):
    x, y, z = p
    r = math.radians(a)
    return z * math.sin(r) + x * math.cos(r), y, z * math.cos(r) - x * math.sin(r)

def rotate_z(p, a):
    x, y, z = p
    r = math.radians(a)
    return x * math.cos(r) - y * math.sin(r), x * math.sin(r) + y * math.cos(r), z

def scale(p, s):
    x, y, z = p
    return x * s, y * s, z * s

def translate(p, tx, ty, tz):
    x, y, z = p
    return x + tx, y + ty, z + tz

def project(p, scale=100, d=5):
    x, y, z = p
    f = scale / (z + d)
    return int(x * f + 300), int(-y * f + 300)

def plot(points, edges):
    for start, end in edges:
        pygame.draw.line(screen, (0, 255, 200), points[start], points[end], 2)

angle_x = 0
angle_y = 0
angle_z = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((15, 15, 15))

    angle_x += 1
    angle_y += 1
    angle_z += 1

    transformed_points = []
    for p in original_points:
        p = scale(p, 1.5)
        p = rotate_x(p, angle_x)
        p = rotate_y(p, angle_y)
        p = rotate_z(p, angle_z)
        p = translate(p, 0, 0, 3)
        projected = project(p)
        transformed_points.append(projected)

    plot(transformed_points, edges)

    pygame.display.flip()
    clock.tick(60)
