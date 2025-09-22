
from .Matrix import Matrix
from .Point3d import Point3d

class Vector4d(Matrix):
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, w: float = 0.0):
        super().__init__(4, 1, 0.0)
        self.m[0][0] = float(x)
        self.m[1][0] = float(y)
        self.m[2][0] = float(z)
        self.m[3][0] = float(w)

    def x(self) -> float: return float(self.m[0][0])
    def y(self) -> float: return float(self.m[1][0])
    def z(self) -> float: return float(self.m[2][0])
    def w(self) -> float: return float(self.m[3][0])

    def to_point3d(self) -> Point3d:
        return Point3d(self.m[0][0], self.m[1][0], self.m[2][0])
