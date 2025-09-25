# graphics_package/scene3d.py
from graphics_package.view3d import View3d
from graphics_package.igraphic_object3d import IGraphicObject3d
from graphics_package.transformation3d import Transformation3d
from graphics_package.line3d import Line3d

class Scene3d:
    def __init__(self, view=None):
        self.objects = []
        self.view = view if view is not None else View3d()
        self.lights = []  # placeholder for lighting models

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
        for obj in self.objects:
            obj.transform(matrix)

    def render(self):
        """
        Full pipeline:
          1. Normalize using perspective projection (view.nPer()).
          2. Clip against canonical view volume (view.clip3d()).
          3. Map surviving objects into viewport (view.mVV3DV()).
          4. Project to 2D.
        Returns: list of Line2d
        """
        primitives = []

        # Prepare combined transform (normalize + viewport)
        nper = self.view.nPer()
        viewport = self.view.mVV3DV()
        pipeline = Transformation3d()
        pipeline.transform(nper)
        pipeline.transform(viewport)

        for obj in self.objects:
            if isinstance(obj, Line3d):
                # Clipping test (zmin = -1, same as Java test)
                if self.view.clip3d(obj, zmin=-1.0):
                    obj.transform(pipeline)
                    primitives.extend(obj.to_2d())
            else:
                # For polygons/meshes: transform, then defer clipping to their edges
                obj.transform(pipeline)
                primitives.extend(obj.to_2d())

        return primitives

    def __len__(self):
        return len(self.objects)

    def __iter__(self):
        return iter(self.objects)

    def __str__(self):
        return f"Scene3d({len(self.objects)} objects, {len(self.lights)} lights)"
