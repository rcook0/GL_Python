# graphics_package/line3d.py
from graphics_package.point3d import Point3d
from graphics_package.vector4d import Vector4d
from graphics_package.transformation3d import Transformation3d
from graphics_package.line2d import Line2d

class Line3d:
    def __init__(self, *args):
        """
        Constructors:
        - Line3d(x1, y1, z1, x2, y2, z2)
        - Line3d(Point3d, Point3d)
        - Line3d(Vector4d, Vector4d)
        """
        if len(args) == 6:  # raw coords
            x1, y1, z1, x2, y2, z2 = args
            self.src = Point3d(x1, y1, z1)
            self.dest = Point3d(x2, y2, z2)
        elif len(args) == 2 and isinstance(args[0], Point3d):
            self.src, self.dest = args
        elif len(args) == 2 and isinstance(args[0], Vector4d):
            a, b = args
            self.src = Point3d.from_vector(a)
            self.dest = Point3d.from_vector(b)
        else:
            raise TypeError("Invalid constructor arguments for Line3d")

    def get_source_point(self) -> Point3d:
        return self.src

    def get_destination_point(self) -> Point3d:
        return self.dest

    def line2d(self) -> Line2d:
        """Project to 2D by stripping z-coordinate."""
        return Line2d(self.src.x(), self.src.y(), self.dest.x(), self.dest.y())

    def transform(self, matrix: Transformation3d):
        """Apply transformation to both endpoints (via Matrix inheritance)."""
        self.src.transform(matrix)
        self.dest.transform(matrix)

    def __str__(self):
        return f"Line3d[{self.src} -> {self.dest}]"
