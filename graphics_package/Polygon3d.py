# graphics_package/polygon3d.py
from graphics_package.point3d import Point3d
from graphics_package.line2d import Line2d
from graphics_package.igraphic_object3d import IGraphicObject3d
from graphics_package.vector4d import Vector4d

class Polygon3d(IGraphicObject3d):
    def __init__(self, vertices=None):
        self.vertices = vertices if vertices is not None else []

    def add_vertex(self, p: Point3d):
        if not isinstance(p, Point3d):
            raise TypeError("Polygon3d only accepts Point3d vertices")
        self.vertices.append(p)

    def transform(self, matrix):
        for v in self.vertices:
            v.transform(matrix)

    def normal(self):
        """Compute surface normal using first 3 vertices (assumes CCW order)."""
        if len(self.vertices) < 3:
            return Vector4d(0, 0, 0, 0)

        a, b, c = self.vertices[:3]
        ab = Vector4d.from_points(a, b)
        ac = Vector4d.from_points(a, c)
        n = Vector4d.product(ab, ac)  # cross product
        return n

    def is_front_facing(self, view_dir: Vector4d) -> bool:
        """Return True if polygon faces the viewer."""
        n = self.normal()
        dot = n.x() * view_dir.x() + n.y() * view_dir.y() + n.z() * view_dir.z()
        return dot < 0  # negative means facing camera

    def to_2d(self, view_dir=None):
        """Project to 2D edges, with optional back-face culling."""
        if view_dir is not None and not self.is_front_facing(view_dir):
            return []  # cull back-facing polygon

        lines = []
        if len(self.vertices) < 2:
            return lines

        for i in range(len(self.vertices)):
            p1 = self.vertices[i]
            p2 = self.vertices[(i + 1) % len(self.vertices)]
            lines.append(Line2d(p1.x(), p1.y(), p2.x(), p2.y()))
        return lines

    def __len__(self):
        return len(self.vertices)

    def __iter__(self):
        return iter(self.vertices)

    def __str__(self):
        verts_str = ", ".join(str(v) for v in self.vertices)
        return f"Polygon3d({verts_str})"
