
import math
from .Matrix import Matrix
from .Point3d import Point3d

class Transformation3d(Matrix):
    def __init__(self):
        super().__init__(4, 4, 0.0)
        for i in range(4): self.m[i][i] = 1.0

    @staticmethod
    def translate(tx: float, ty: float, tz: float) -> 'Transformation3d':
        M = Transformation3d()
        M.m[0][3] = float(tx)
        M.m[1][3] = float(ty)
        M.m[2][3] = float(tz)
        return M

    @staticmethod
    def scale(sx: float, sy: float, sz: float) -> 'Transformation3d':
        M = Transformation3d()
        M.m[0][0] = float(sx); M.m[1][1] = float(sy); M.m[2][2] = float(sz)
        return M

    @staticmethod
    def rotate_x(theta: float) -> 'Transformation3d':
        c, s = math.cos(theta), math.sin(theta)
        M = Transformation3d()
        M.m[1][1] = c; M.m[1][2] = -s
        M.m[2][1] = s; M.m[2][2] = c
        return M

    @staticmethod
    def rotate_y(theta: float) -> 'Transformation3d':
        c, s = math.cos(theta), math.sin(theta)
        M = Transformation3d()
        M.m[0][0] = c;  M.m[0][2] = s
        M.m[2][0] = -s; M.m[2][2] = c
        return M

    @staticmethod
    def rotate_z(theta: float) -> 'Transformation3d':
        c, s = math.cos(theta), math.sin(theta)
        M = Transformation3d()
        M.m[0][0] = c; M.m[0][1] = -s
        M.m[1][0] = s; M.m[1][1] = c
        return M

    def apply_point(self, p: Point3d) -> Point3d:
        vec = [p.m[0][0], p.m[1][0], p.m[2][0], 1.0]
        x,y,z,w = self.apply_to_vec(vec)
        if w != 0.0:
            x,y,z = x/w, y/w, z/w
        return Point3d(x,y,z)
