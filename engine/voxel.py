from ursina import *
import random

MODEL = "cube"
TEXTURE = "assets/grass.png"

class Voxel(Entity):
    def __init__(self, position=(0, 0, 0)):
        color_variation = Vec4(
            (100 + random.randint(-20, 20)) / 255,
            (180 + random.randint(-30, 30)) / 255,
            (100 + random.randint(-20, 20)) / 255, 1
        )
        super().__init__(
            parent=scene,
            model=MODEL,
            position=position,
            origin_y=1,
            texture=TEXTURE,
            color=color_variation,
            collider="box",
        )

class VoxelController(Entity):
    def __init__(self):
        super().__init__()

    def input(self, key):
        if mouse.hovered_entity and isinstance(mouse.hovered_entity, Voxel):
            target = mouse.hovered_entity
            if key == "right mouse down":
                Voxel(position=target.position + mouse.normal)
            elif key == "left mouse down":
                destroy(target)
