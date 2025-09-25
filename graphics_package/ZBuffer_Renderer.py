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

    def render_scene(self, scene: Scene3d):
        """
        Rasterize polygons from a Scene3d using z-buffer hidden-surface elimination.
        Each Polygon3d is filled with a flat color (default white).
        """
        for poly in scene.objects:
            if isinstance(poly, Polygon3d):
                self._rasterize_polygon(poly)

    def _rasterize_polygon(self, poly: Polygon3d, color=(1.0, 1.0, 1.0)):
        """
        Fill polygon using barycentric coordinates and z-buffer.
        Assumes poly.vertices is a list of Point3d with projected (x, y, z).
        """
        verts = [(int(v.x()), int(v.y()), v.z()) for v in poly.vertices]
        xs, ys, zs = zip(*verts)

        # Bounding box
        min_x, max_x = max(min(xs), 0), min(max(xs), self.width - 1)
        min_y, max_y = max(min(ys), 0), min(max(ys), self.height - 1)

        # Triangle only (extend later for quads/polys)
        if len(verts) != 3:
            return

        (x0, y0, z0), (x1, y1, z1), (x2, y2, z2) = verts

        # Edge function
        def edge(xa, ya, xb, yb, xc, yc):
            return (xc - xa) * (yb - ya) - (yc - ya) * (xb - xa)

        area = edge(x0, y0, x1, y1, x2, y2)
        if area == 0:
            return  # Degenerate polygon

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                w0 = edge(x1, y1, x2, y2, x, y)
                w1 = edge(x2, y2, x0, y0, x, y)
                w2 = edge(x0, y0, x1, y1, x, y)

                if (w0 >= 0 and w1 >= 0 and w2 >= 0) or (w0 <= 0 and w1 <= 0 and w2 <= 0):
                    # Barycentric weights
                    alpha = w0 / area
                    beta = w1 / area
                    gamma = w2 / area

                    # Interpolated depth
                    z = alpha * z0 + beta * z1 + gamma * z2

                    if z < self.z_buffer[y, x]:
                        self.z_buffer[y, x] = z
                        self.color_buffer[y, x] = color

    def show(self):
        plt.imshow(self.color_buffer, origin="lower")
        plt.axis("off")
        plt.show()
