# graphics_package/scene3d.py
from graphics_package.view3d import View3d
from graphics_package.igraphic_object3d import IGraphicObject3d
from graphics_package.transformation3d import Transformation3d

class Scene3d:
    def __init__(self, view=None):
        self.objects = []
        self.view = view if view is not None else View3d()
        self.lights = []  # placeholder for future lighting models

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

    def transform_all(self, matrix: Transformation3d):
        """Apply a transform to every object in the scene."""
        for obj in self.objects:
            obj.transform(matrix)

    def render(self):
        """
        Full pipeline:
          1. Normalize using perspective projection (view.nPer()).
          2. Map into viewport (view.mVV3DV()).
          3. Convert each 3D object to 2D primitives.
        Returns: list of Line2d
        """
        primitives = []
        # Step 1 + 2: compute combined transformation
        nper = self.view.nPer()               # perspective normalization
        viewport = self.view.mVV3DV()         # map to 3D viewport
        pipeline = Transformation3d()
        pipeline.transform(nper)
        pipeline.transform(viewport)

        # Apply pipeline to all objects
        for obj in self.objects:
            obj.transform(pipeline)
            primitives.extend(obj.to_2d())

        return primitives

    def __len__(self):
        return len(self.objects)

    def __iter__(self):
        return iter(self.objects)

    def __str__(self):
        return f"Scene3d({len(self.objects)} objects, {len(self.lights)} lights)"
