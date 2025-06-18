import random
import math
from Code.constants import *


def gen_coords():
    coord = 0
    while not coord:
        coord = random.randint(-MOVEMENT, MOVEMENT)
    return coord


def get_start_coords(x, y):
    start_x = (x - SIZE) // 2
    start_y = (y - SIZE) // 2
    return start_x, start_y


def calculate_coords(angel, width, height):
    radius = min(width, height) // RADIUS
    angel = math.radians(angel)

    x = round(math.cos(angel) * radius) + width // 2
    x = x - SIZE // 2
    y = round(math.sin(angel) * radius) + height // 2
    y = y - SIZE // 2

    return x, y


def move_x_y(x, y, coords):
    if x not in [coords[0] - 1, coords[0], coords[0] + 1]:
        x = x - 2 if x > coords[0] else x + 2
    elif x != coords[0]:
        x = x - 1 if x > coords[0] else x + 1
    if y not in [coords[1] - 1, coords[1], coords[1] + 1]:
        y = y - 2 if y > coords[1] else y + 2
    elif y != coords[1]:
        y = y - 1 if y > coords[0] else y + 1

    return x, y
