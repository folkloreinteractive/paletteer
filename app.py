import pygame
import os
import math

def run(source, target):
    colors = []
    # Get list of RGBs from text file
    with open(source, "r") as f:
        lines = f.readlines()
        for line in lines:
            colors.append(line.strip('\n'))
    
    # Print the colors to the console
    for color in colors:
        print(color)
    colorCount = len(colors)

    sampleSize = (16, 16)
    rows = math.ceil(colorCount / 8)
    height = rows * sampleSize[1]
    width = 8 * sampleSize[0]

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    palette = pygame.Surface((width, height)).convert()

    for c in colors:
        x = colors.index(c) % 8
        y = colors.index(c) // 8
        print(x, y)
        pygame.draw.rect(palette, pygame.Color(c), (x * sampleSize[0], y * sampleSize[1], sampleSize[0], sampleSize[1]))

    pygame.image.save(palette, target)
    print(f"Your palette has been saved to {target}")
