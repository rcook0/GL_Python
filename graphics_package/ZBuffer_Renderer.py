# graphics_package/zbuffer_renderer.py
import numpy as np
import matplotlib.pyplot as plt
from graphics_package.scene3d import Scene3d
from graphics_package.polygon3d import Polygon3d

class ZBufferRenderer:
    def __init__(self, width=400, height=400):
        self.width = width
        self.height = height
        self.color_buffer = np.zeros((height, width, 3), dtype=np.float32)  # RGB
        self.z_buffer = np.full((height, width), np.inf)  # depth values

    def clear(self):
        self.color_buffer.fill(0.0)
        self.z_buffer.fill(np.inf)

    def render_scene(self, scene: Scene3d, color=(1.0, 1.0, 1.0)):
        """
        Rasterize polygons from a Scene3d using z-buffer hidden-surface elimination.
        """
        primitives = scene.render()  # currently returns Line2d edges
        # To be more accurate, we should rasterize polygons directly.
        # Here: fill edges as white pixels (wireframe mode).
        for line in primitives:
            self._draw_line(line, color)

    def _draw_line(self, line, color):
        """Simple Bresenham line rasterization with depth test (wireframe)."""
        x0, y0 = int(line.x1), int(line.y1)
        x1, y1 = int(line.x2), int(line.y2)
        dx = abs(x1 - x0)
        dy = -abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx + dy
        while True:
            if 0 <= x0 < self.width and 0 <= y0 < self.height:
                z = 0.0  # TODO: interpolate z from 3D vertices
                if z < self.z_buffer[y0, x0]:
                    self.z_buffer[y0, x0] = z
                    self.color_buffer[y0, x0] = color
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x0 += sx
            if e2 <= dx:
                err += dx
                y0 += sy

    def show(self):
        plt.imshow(self.color_buffer, origin="lower")
        plt.axis("off")
        plt.show()
