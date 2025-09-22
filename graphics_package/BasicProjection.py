
from .Matrix import Matrix

def perspective(d: float) -> Matrix:
    # p' = M * p, w' = z/d -> divide to get (d*x/z, d*y/z)
    return Matrix.from_list([
        [1,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [0,0,1/d,0],
    ])

def orthographic() -> Matrix:
    # drop z, keep x,y
    return Matrix.from_list([
        [1,0,0,0],
        [0,1,0,0],
        [0,0,0,0],
        [0,0,0,1],
    ])
