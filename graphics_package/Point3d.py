
class Point3d:
    """3D point with x, y, z coordinates."""

    def __init__(self, x: float, y: float, z: float):
        self._x = x
        self._y = y
        self._z = z

    def x(self) -> float: return self._x
    def y(self) -> float: return self._y
    def z(self) -> float: return self._z

    def set_x(self, val: float) -> None: self._x = val
    def set_y(self, val: float) -> None: self._y = val
    def set_z(self, val: float) -> None: self._z = val

    def as_tuple(self) -> tuple[float, float, float]:
        return (self._x, self._y, self._z)

    def transform(self, matrix: "Transformation3d") -> "Point3d":
        return matrix.apply_point(self)

    def __str__(self) -> str:
        return f"{self._x} {self._y} {self._z}"
