import matplotlib.pyplot as plt
import numpy as np
from graphics_package.point3d import Point3d
from scene3d import Scene3d
from renderer import Renderer

def build_hexagon(radius=0.8, z=0.0):
    vertices = []
    for i in range(6):
        angle = 2 * np.pi * i / 6
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        vertices.append(Point3d(x, y, z, 0, 0, 1))
    return vertices

def main():
    width, height = 400, 400
    renderer = Renderer(width, height)
    scene = Scene3d(renderer)
    hexagon = build_hexagon()
    scene.add_hexagon(hexagon, subdivisions=4)
    img = scene.render(color=(0.2, 0.6, 1.0))
    plt.imshow(img)
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()
