import pygame
import sys

x1=int(input("Enter x coordinate of the first point:    "))
y1=int(input("Enter y coordinate of the first point:    "))
x2=int(input("Enter x coordinate of the second point:    "))
y2=int(input("Enter y coordinate of the second point:    "))

pygame.init()

WIDTH, HEIGHT = 700,800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bresenham's Line Algorithm")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_line_bla(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    x = x1
    y = y1

    lx = 1 if x2 > x1 else -1
    ly = 1 if y2 > y1 else -1


    if dx > dy:
        p = 2 * dy - dx
        for _ in range(dx):
            if p < 0:
                x += lx
                p += 2 * dy
            else:
                x += lx
                y += ly
                p += 2 * dy - 2 * dx
            screen.set_at((round(x), HEIGHT - round(y)), BLACK)
    else:
        p = 2 * dx - dy
        for _ in range(dy):
            if p < 0:
                y += ly
                p += 2 * dx
            else:
                x += lx
                y += ly
                p += 2 * dx - 2 * dy
            screen.set_at((round(x), HEIGHT - round(y)), BLACK)

def main():
    screen.fill(WHITE)
    draw_line_bla(x1,y1,x2,y2)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()