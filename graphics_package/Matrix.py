
from __future__ import annotations
from typing import List

class Matrix:
    def __init__(self, rows: int, columns: int, init: float = 0.0):
        self.rows = rows
        self.columns = columns
        self.m: List[List[float]] = [[init for _ in range(columns)] for _ in range(rows)]

    @staticmethod
    def identity(n: int) -> 'Matrix':
        M = Matrix(n, n, 0.0)
        for i in range(n):
            M.m[i][i] = 1.0
        return M

    @staticmethod
    def from_list(vals: List[List[float]]) -> 'Matrix':
        rows = len(vals)
        cols = len(vals[0]) if rows else 0
        M = Matrix(rows, cols, 0.0)
        for i in range(rows):
            for j in range(cols):
                M.m[i][j] = float(vals[i][j])
        return M

    def copy(self) -> 'Matrix':
        out = Matrix(self.rows, self.columns, 0.0)
        for i in range(self.rows):
            for j in range(self.columns):
                out.m[i][j] = self.m[i][j]
        return out

    def mul(self, other: 'Matrix') -> 'Matrix':
        if self.columns != other.rows:
            raise ValueError("Dimension mismatch: %dx%d * %dx%d" % (self.rows, self.columns, other.rows, other.columns))
        result = Matrix(self.rows, other.columns, 0.0)
        for i in range(self.rows):
            for j in range(other.columns):
                s = 0.0
                for k in range(self.columns):
                    s += self.m[i][k] * other.m[k][j]
                result.m[i][j] = s
        return result

    def __matmul__(self, other: 'Matrix') -> 'Matrix':
        return self.mul(other)

    def apply_to_vec(self, vec: List[float]) -> List[float]:
        if len(vec) != self.columns:
            raise ValueError("Vector length %d != columns %d" % (len(vec), self.columns))
        out = [0.0]*self.rows
        for i in range(self.rows):
            s = 0.0
            for j in range(self.columns):
                s += self.m[i][j] * vec[j]
            out[i] = s
        return out

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        rows = []
        for i in range(self.rows):
            rows.append("(" + ", ".join(str(self.m[i][j]) for j in range(self.columns)) + ")")
        return "[\n" + "\n".join(rows) + "\n]"
