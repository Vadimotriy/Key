import random
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