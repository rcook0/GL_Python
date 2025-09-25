# graphics_package/polygon3d.py
from graphics_package.point3d import Point3d
from graphics_package.line2d import Line2d
from graphics_package.igraphic_object3d import IGraphicObject3d

class Polygon3d(IGraphicObject3d):
    def __init__(self, vertices=None):
        """
        vertices: list of Point3d
        """
        self.vertices = vertices if vertices is not None else []

    def add_vertex(self, p: Point3d):
        if not isinstance(p, Point3d):
            raise TypeError("Polygon3d only accepts Point3d vertices")
        self.vertices.append(p)

    def transform(self, matrix):
        for v in self.vertices:
            v.transform(matrix)

    def to_2d(self):
        lines = []
        if len(self.vertices) < 2:
            return lines

        for i in range(len(self.vertices)):
            p1 = self.vertices[i]
            p2 = self.vertices[(i + 1) % len(self.vertices)]  # wrap around
            lines.append(Line2d(p1.x(), p1.y(), p2.x(), p2.y()))
        return lines

    def __len__(self):
        return len(self.vertices)

    def __iter__(self):
        return iter(self.vertices)

    def __str__(self):
        verts_str = ", ".join(str(v) for v in self.vertices)
        return f"Polygon3d({verts_str})"
