# graphics_package/compound_graphic_object3d.py
from graphics_package.line3d import Line3d
from graphics_package.transformation3d import Transformation3d

class CompoundGraphicObject3d:
    def __init__(self):
        self.objects = []  # list of Line3d (or later: Polygon3d, etc.)

    def add(self, obj):
        if isinstance(obj, Line3d):
            self.objects.append(obj)
        else:
            raise TypeError("CompoundGraphicObject3d supports Line3d (for now)")

    def clear(self):
        self.objects.clear()

    def transform(self, matrix: Transformation3d):
        """Apply a transformation to all contained 3D objects."""
        for obj in self.objects:
            obj.transform(matrix)

    def to_2d(self):
        """Convert all 3D objects into their 2D equivalents (list of Line2d)."""
        return [obj.line2d() for obj in self.objects]

    def __iter__(self):
        return iter(self.objects)

    def __len__(self):
        return len(self.objects)

    def __str__(self):
        return f"CompoundGraphicObject3d({len(self.objects)} objects)"
