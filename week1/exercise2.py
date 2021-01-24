import math
import random


def rand():
    return random.uniform(-1, 1)


def distance(x: tuple[float, float], y: tuple[float, float]) -> float:
    return math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)


def in_circle(x: tuple[float, float], origin=(0, 0)) -> bool:
    return True if distance(x, origin) <= 1 else False


random.seed(1)

points_inside = 0
points_outside = 0

for __ in range(10000):
    point = (rand(), rand())
    if in_circle(point):
        points_inside += 1
    else:
        points_outside += 1

epsilon = abs(math.pi/4 - (points_inside / (points_inside + points_outside)))
