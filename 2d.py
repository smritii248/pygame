import pygame
import sys
import math
pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rotating Circle Example")
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
def draw_ellipse(xc, yc, rx, ry):
    x = 0
    y = ry
    p1 = round(ry * ry - rx * rx * ry + 0.25 * rx * rx)
    while (2 * ry * ry * x) <= (2 * rx * rx * y ):
        if(p1 < 0):
            x = x + 1
            y = y
            p1 = p1 + (2 * ry * ry * x) + ry * ry
        else:
            x = x+1
            y = y-1
            p1 = p1 + (2 * ry * ry * x) - (2 * rx * rx * y )+ ry * ry
        screen.set_at(( x + xc , y + yc) , "red") 
        screen.set_at((x + xc , -y + yc) , "red") 
        screen.set_at((-x + xc , y + yc) , "red") 
        screen.set_at((-x + xc , -y + yc) , "red") 

    p2 = round(ry * ry *(x + 1/2) ** 2  + rx * rx * (y-1) ** 2 - rx * rx * ry * ry)
    while y != 0:
        if(p2 >  0):
            x = x 
            y = y-1
            p2 = p2 -  (2 * rx * rx * y )+ rx * rx
        else:
            x = x+1
            y = y-1
            p2 = p2 + (2 * ry * ry * x) - (2 * rx * rx * y )+ rx * rx
        screen.set_at(( x + xc , y + yc) , "red") 
        screen.set_at((x + xc , -y + yc) , "red") 
        screen.set_at((-x + xc , y + yc) , "red") 
        screen.set_at((-x + xc , -y + yc) , "red") 


running = True
angle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(WHITE)

    radius = 100
    center = (width // 2, height // 2)
    x = center[0] + int(radius * math.cos(math.radians(angle)))
    y = center[1] + int(radius * math.sin(math.radians(angle)))
    pygame.draw.circle(screen, "red", (x, y), 20)
    draw_ellipse(width // 2, height // 2, 100, 100)
    pygame.display.flip()
    angle += 1
    if angle >= 360:
        angle = 0

   
    pygame.time.Clock().tick(60)


pygame.quit()
sys.exit()











