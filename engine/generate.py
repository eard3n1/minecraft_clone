from ursina import *
import random
from .voxel import Voxel

def generate_heightmap(width, depth, max_height, seed=None):
    if seed is None:
        random.seed(random.randint(0, 10**32))
    else:
        random.seed(seed)

    heights = [[0 for _ in range(width)] for _ in range(depth)]
    for z in range(depth):
        for x in range(width):
            neighbors = []
            if x > 0:
                neighbors.append(heights[z][x - 1])
            if z > 0:
                neighbors.append(heights[z - 1][x])
            if neighbors:
                avg = sum(neighbors) / len(neighbors)
                new_height = int(clamp(round(avg + random.randint(-1, 1)), 1, max_height))
            else:
                new_height = random.randint(1, max_height)
            heights[z][x] = new_height
    return heights

def generate_terrain(width, depth, max_height, seed):
    heights = generate_heightmap(width, depth, max_height, seed)
    for z in range(depth):
        for x in range(width):
            for y in range(heights[z][x]):
                Voxel(position=(x, y, z))