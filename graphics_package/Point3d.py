# graphics_package/point3d.py
from graphics_package.matrix import Matrix

class Point3d(Matrix):
    def __init__(self, in_x, in_y, in_z, nx=0.0, ny=0.0, nz=0.0):
        """
        Construct a 3D point (homogeneous coordinates).
        Optional normal (nx, ny, nz) can be attached.
        """
        super().__init__(4, 1, 1)
        self.m[0][0] = in_x
        self.m[1][0] = in_y
        self.m[2][0] = in_z
        self.m[3][0] = 1.0

        # Store normal separately
        self.nx = nx
        self.ny = ny
        self.nz = nz

    # --------------------------
    # Position accessors
    # --------------------------
    def x(self): return self.m[0][0]
    def y(self): return self.m[1][0]
    def z(self): return self.m[2][0]

    def set_x(self, val): self.m[0][0] = val
    def set_y(self, val): self.m[1][0] = val
    def set_z(self, val): self.m[2][0] = val

    # --------------------------
    # Normal accessors
    # --------------------------
    def normal(self):
        return (self.nx, self.ny, self.nz)

    def set_normal(self, nx, ny, nz):
        self.nx, self.ny, self.nz = nx, ny, nz

    def normalize_normal(self):
        import math
        length = math.sqrt(self.nx**2 + self.ny**2 + self.nz**2)
        if length > 1e-9:
            self.nx /= length
            self.ny /= length
            self.nz /= length

    # --------------------------
    # Transformation
    # --------------------------
    def transform(self, matrix):
        super().transform(matrix)

    def __str__(self):
        return f"({self.x():.3f}, {self.y():.3f}, {self.z():.3f}; n=({self.nx:.2f},{self.ny:.2f},{self.nz:.2f}))"
