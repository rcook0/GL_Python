
import math
from .Point3d import Point3d

class Transformation3d:
    """3D homogeneous transformation matrix."""

    def __init__(self):
        self.m = [[0.0]*4 for _ in range(4)]
        for i in range(4):
            self.m[i][i] = 1.0

    def transform(self, other: "Transformation3d") -> None:
        result = [[0.0]*4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    result[i][j] += self.m[i][k] * other.m[k][j]
        self.m = result

    def translate(self, dx: float, dy: float, dz: float) -> None:
        t = Transformation3d()
        t.m[0][3] = dx
        t.m[1][3] = dy
        t.m[2][3] = dz
        self.transform(t)

    def scale(self, sx: float, sy: float, sz: float) -> None:
        s = Transformation3d()
        s.m[0][0] = sx
        s.m[1][1] = sy
        s.m[2][2] = sz
        self.transform(s)

    def rotate_x(self, theta: float) -> None:
        r = Transformation3d()
        c, s = math.cos(theta), math.sin(theta)
        r.m[1][1] = c;  r.m[1][2] = -s
        r.m[2][1] = s;  r.m[2][2] = c
        self.transform(r)

    def rotate_y(self, theta: float) -> None:
        r = Transformation3d()
        c, s = math.cos(theta), math.sin(theta)
        r.m[0][0] = c;  r.m[0][2] = s
        r.m[2][0] = -s; r.m[2][2] = c
        self.transform(r)

    def rotate_z(self, theta: float) -> None:
        r = Transformation3d()
        c, s = math.cos(theta), math.sin(theta)
        r.m[0][0] = c;  r.m[0][1] = -s
        r.m[1][0] = s;  r.m[1][1] = c
        self.transform(r)

    def apply_point(self, p: Point3d) -> Point3d:
        x, y, z = p.x(), p.y(), p.z()
        vec = [x, y, z, 1.0]
        res = [0.0]*4
        for i in range(4):
            for j in range(4):
                res[i] += self.m[i][j] * vec[j]
        if abs(res[3]) > 1e-9:
            return Point3d(res[0]/res[3], res[1]/res[3], res[2]/res[3])
        else:
            return Point3d(res[0], res[1], res[2])

    def __matmul__(self, p: Point3d) -> Point3d:
        return self.apply_point(p)

    def __str__(self):
        return "\n".join([" ".join(f"{v: .3f}" for v in row) for row in self.m])
