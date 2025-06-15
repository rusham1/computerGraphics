import pygame
import sys
import math

pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Revolving Circles Around Ellipses")

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
        dx += 2 * ry**2
        if p1 < 0:
            p1 += dx + ry**2
        else:
            y -= 1
            dy -= 2 * rx**2
            p1 += dx - dy + ry**2

    p2 = (ry**2)*(x+0.5)**2 + (rx**2)*(y-1)**2 - rx**2 * ry**2

    while y >= 0:
        plot_Ellipse_points(xc, yc, x, y)
        y -= 1
        dy -= 2 * rx**2
        if p2 > 0:
            p2 += rx**2 - dy
        else:
            x += 1
            dx += 2 * ry**2
            p2 += dx - dy + rx**2

ellipses = [
    {"rx": 350, "ry": 250, "xc": 400, "yc": 400, "angle": 0},
    {"rx": 250, "ry": 150, "xc": 400, "yc": 400, "angle": 1},
    {"rx": 300, "ry": 200, "xc": 400, "yc": 400, "angle": 2},
    {"rx": 150, "ry": 50,  "xc": 400, "yc": 400, "angle": 3},
    {"rx": 200, "ry": 100, "xc": 400, "yc": 400, "angle": 4},
]

def main():
    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)

        for ellipse in ellipses:
            midpointEllipse(ellipse["rx"], ellipse["ry"], ellipse["xc"], ellipse["yc"])

            angle = ellipse["angle"]
            x = int(ellipse["xc"] + ellipse["rx"] * math.cos(angle))
            y = int(ellipse["yc"] + ellipse["ry"] * math.sin(angle))
            pygame.draw.circle(screen, BLACK, (x, flip_y(y)), 10)

            ellipse["angle"] += 0.01

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
