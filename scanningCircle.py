import pygame
import sys
import math

x=int(input("Enter x coordinate of the centre:  "))
y=int(input("Enter y coordinate of the centre:  "))
r=int(input("Enter radius of the circle:  "))

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint Circle Drawing Algorithm")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def flip_y(y):
    return HEIGHT - y

def plot_circle_points(xc, yc, x, y):
    points = [
        (xc + x, flip_y(yc + y)),
        (xc - x, flip_y(yc + y)),
        (xc + x, flip_y(yc - y)),
        (xc - x, flip_y(yc - y)),
        (xc + y, flip_y(yc + x)),
        (xc - y, flip_y(yc + x)),
        (xc + y, flip_y(yc - x)),
        (xc - y, flip_y(yc - x)),
    ]
    for px, py in points:
        if 0 <= px < WIDTH and 0 <= py < HEIGHT:
            screen.set_at((px, py), BLACK)

def midpointCircle(xc, yc, r):
    x = 0
    y = r
    d = 1 - r
    plot_circle_points(xc, yc, x, y)

    while x < y:
        x += 1
        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1
            d += 2 * (x - y) + 1
        plot_circle_points(xc, yc, x, y)

def main():
    screen.fill(WHITE)
    
    midpointCircle(x,y,r)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()