
from .Point3d import Point3d
from .Line2d import Line2d
from .Transformation3d import Transformation3d

class Line3d:
    def __init__(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float):
        self.src = Point3d(x1, y1, z1)
        self.dest = Point3d(x2, y2, z2)

    @classmethod
    def from_points(cls, pSrc: Point3d, pDest: Point3d) -> "Line3d":
        return cls(pSrc.x(), pSrc.y(), pSrc.z(), pDest.x(), pDest.y(), pDest.z())

    def getSourcePoint(self) -> Point3d:
        return self.src

    def getDestinationPoint(self) -> Point3d:
        return self.dest

    def line2d(self) -> Line2d:
        src = self.getSourcePoint()
        dest = self.getDestinationPoint()
        return Line2d(src.x(), src.y(), dest.x(), dest.y())

    def transform(self, matrix: Transformation3d) -> None:
        self.src = matrix @ self.src
        self.dest = matrix @ self.dest

    def __str__(self) -> str:
        return f"Line3d({self.src} -> {self.dest})"
