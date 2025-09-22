
from .Matrix import Matrix

class Point3d(Matrix):
    def __init__(self, in_x: float, in_y: float, in_z: float):
        super().__init__(4, 1, 1.0)
        self.m[0][0] = float(in_x)
        self.m[1][0] = float(in_y)
        self.m[2][0] = float(in_z)

    def x(self) -> float: return float(self.m[0][0])
    def y(self) -> float: return float(self.m[1][0])
    def z(self) -> float: return float(self.m[2][0])
    def set_x(self, v: float) -> None: self.m[0][0] = float(v)
    def set_y(self, v: float) -> None: self.m[1][0] = float(v)
    def set_z(self, v: float) -> None: self.m[2][0] = float(v)

    def __str__(self) -> str:
        return f"{self.m[0][0]} {self.m[1][0]} {self.m[2][0]}"
