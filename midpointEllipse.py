import pygame
import sys


pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint Ellipse Drawing Algorithm")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def flip_y(y):
    return HEIGHT - y

def plot_Ellipse_points(xc, yc, x, y):
    points = [
        (xc + x, flip_y(yc + y)),
        (xc - x, flip_y(yc + y)),
        (xc + x, flip_y(yc - y)),
        (xc - x, flip_y(yc - y)),
    ]
    for px, py in points:
        if 0 <= px < WIDTH and 0 <= py < HEIGHT:
            screen.set_at((int(px), int(py)), BLACK)

def midpointEllipse(rx, ry, xc, yc):
    x = 0
    y = ry

    p1 = ry**2 - (rx**2 * ry) + (0.25 * rx**2)
    dx = 2 * ry**2 * x
    dy = 2 * rx**2 * y

    while dx < dy:
        plot_Ellipse_points(xc, yc, x, y)
        x += 1
        dx = dx + 2 * ry**2
        if p1 < 0:
            p1 += dx + ry**2
        else:
            y -= 1
            dy = dy - 2 * rx**2
            p1 += dx - dy + ry**2

    p2 = (ry**2) * ((x + 0.5)**2) + (rx**2) * ((y - 1)**2) - (rx**2 * ry**2)

    while y >= 0:
        plot_Ellipse_points(xc, yc, x, y)
        y -= 1
        dy = dy - 2 * rx**2
        if p2 > 0:
            p2 += rx**2 - dy
        else:
            x += 1
            dx = dx + 2 * ry**2
            p2 += dx - dy + rx**2

def main():
    screen.fill(WHITE)
    midpointEllipse(350,250,400,400)
    midpointEllipse(250,150,400,400)
    midpointEllipse(300,200,400,400)
    midpointEllipse(150,50,400,400)
    midpointEllipse(200,100,400,400)
    midpointEllipse(30,30,350,250)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
