# graphics_package/scene3d.py
from graphics_package.view3d import View3d
from graphics_package.igraphic_object3d import IGraphicObject3d

class Scene3d:
    def __init__(self, view=None):
        self.objects = []
        self.view = view if view is not None else View3d()
        self.lights = []  # placeholder for future light objects

    def add_object(self, obj: IGraphicObject3d):
        if not isinstance(obj, IGraphicObject3d):
            raise TypeError("Scene3d accepts only IGraphicObject3d")
        self.objects.append(obj)

    def clear(self):
        self.objects.clear()

    def set_view(self, view: View3d):
        self.view = view

    def add_light(self, light):
        self.lights.append(light)

    def transform_all(self, matrix):
        """Apply a transform to every object in the scene."""
        for obj in self.objects:
            obj.transform(matrix)

    def render(self):
        """
        Render the scene by projecting all 3D objects into 2D.
        Returns: list of Line2d objects.
        """
        primitives = []
        for obj in self.objects:
            primitives.extend(obj.to_2d())
        return primitives

    def __len__(self):
        return len(self.objects)

    def __iter__(self):
        return iter(self.objects)

    def __str__(self):
        return f"Scene3d({len(self.objects)} objects, {len(self.lights)} lights)"
