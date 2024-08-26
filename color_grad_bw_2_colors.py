import pygame
import sys

pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("n-Step n-Color Gradient")

# Define the colors and steps
colors = [(255, 244, 116), (240, 101, 83), (56, 28, 42)]  # Add more colors as needed
steps = 128

def interpolate_color(color1, color2, t):
    return tuple(int(a + (b - a) * t) for a, b in zip(color1, color2))

def generate_gradient(colors, steps):
    gradient = []
    segments = len(colors) - 1
    steps_per_segment = steps // segments
    remaining_steps = steps % segments

    for i in range(segments):
        if i !=0:
            steps_per_segment +=1 
        start_color = colors[i]
        end_color = colors[i+1]
        segment_steps = steps_per_segment + (1 if i < remaining_steps else 0)
        
        for step in range(segment_steps):
            t = step / (segment_steps - 1) if segment_steps > 1 else 1
            color = interpolate_color(start_color, end_color, t)
            if len(gradient)>1:
                if gradient[-1] != color:
                    gradient.append(color)
            else:
                gradient.append(color)
    
    return gradient

gradient_colors = generate_gradient(colors, steps)
hex_colors = [f"{r:02x}{g:02x}{b:02x}" for r, g, b in gradient_colors]
print(",".join(hex_colors))
print(f"Number of colors generated: {len(gradient_colors)}")

step_width = width // steps
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    for i, color in enumerate(gradient_colors):
        pygame.draw.rect(screen, color, (i * step_width, 0, step_width, height))
    
    pygame.display.flip()

pygame.quit()
sys.exit()