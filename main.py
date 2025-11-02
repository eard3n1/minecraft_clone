from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from generate import generate_terrain
from voxel import VoxelController
from config import WIDTH, DEPTH, MAX_HEIGHT

app = Ursina()

def main():
    generate_terrain(WIDTH, DEPTH, MAX_HEIGHT)
    FirstPersonController()
    VoxelController()
    Sky()
    app.run()

if __name__ == "__main__":
    main()