import pygame
import sys

def draw_pixelated_circle(surface, color, center, radius, pixel_size=10):
    def draw_pixel(x, y):
        pygame.draw.rect(surface, color, 
                         ((x + center[0]) * pixel_size, (y + center[1]) * pixel_size, 
                          pixel_size, pixel_size))

    def draw_symmetric_pixels(x, y):
        draw_pixel(x, y)
        draw_pixel(-x, y)
        draw_pixel(x, -y)
        draw_pixel(-x, -y)
        draw_pixel(y, x)
        draw_pixel(-y, x)
        draw_pixel(y, -x)
        draw_pixel(-y, -x)

    x, y = radius, 0
    decision = 1 - radius

    while y <= x:
        draw_symmetric_pixels(x, y)
        y += 1
        if decision <= 0:
            decision += 2 * y + 1
        else:
            x -= 1
            decision += 2 * (y - x) + 1


pygame.init()


pixel_size = 20 # thebigger the better
radius = 8 #input radius here .
display_size = (radius * 2 + 1) * pixel_size
screen = pygame.display.set_mode((display_size, display_size))
pygame.display.set_caption(f"Pixelated Circle (Radius: {radius})")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255) 
RED = (255, 0, 0)

center = (radius, radius)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

  
    screen.fill(WHITE)
    draw_pixelated_circle(screen, RED, center, radius, pixel_size)
    for i in range(0, display_size + 1, pixel_size):
        pygame.draw.line(screen, BLACK, (i, 0), (i, display_size), 1)
        pygame.draw.line(screen, BLACK, (0, i), (display_size, i), 1)
    pygame.display.flip()
pygame.quit()
sys.exit()