import pygame
import sys

#intended for 
#Pixilart palette import format
pygame.init()


width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("n-Step 2-Color Gradieant")


start_color = (40,55,65)   #put color here manually
end_color = (5,5,5)   

steps = 32

step_r = (end_color[0] - start_color[0]) / (steps - 1)
step_g = (end_color[1] - start_color[1]) / (steps - 1)
step_b = (end_color[2] - start_color[2]) / (steps - 1)


step_width = width // steps

hex_colors = []

for i in range(steps):
    r = int(start_color[0] + step_r * i)
    g = int(start_color[1] + step_g * i)
    b = int(start_color[2] + step_b * i)
    hex_color = f"{r:02x}{g:02x}{b:02x}"
    hex_colors.append(hex_color)

print(",".join(hex_colors))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((255, 255, 255))


    for i in range(steps):
        r = int(start_color[0] + step_r * i)
        g = int(start_color[1] + step_g * i)
        b = int(start_color[2] + step_b * i)
        color = (r, g, b)
        pygame.draw.rect(screen, color, (i * step_width, 0, step_width, height))


    pygame.display.flip()


pygame.quit()
sys.exit()