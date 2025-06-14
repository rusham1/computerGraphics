
import pygame
import sys

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DDA Algorithm")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_line_dda(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    step = max(abs(dx), abs(dy))

    xinc = dx / step
    yinc = dy / step

    x = x1
    y = y1

    for _ in range(step + 1):
        screen.set_at((round(x), HEIGHT - round(y)), BLACK)
        x += xinc
        y += yinc
        

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        draw_line_dda(x1, y1, x2, y2)
        pygame.display.flip()

if __name__ == "__main__":
    main()