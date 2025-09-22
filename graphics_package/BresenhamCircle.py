
from typing import List, Tuple

def rasterize(cx: int, cy: int, r: int) -> List[Tuple[int,int]]:
    x, y = 0, r
    d = 1 - r
    pts = []
    def emit(a,b):
        pts.extend([
            (cx + a, cy + b),
            (cx + b, cy + a),
            (cx - a, cy + b),
            (cx - b, cy + a),
            (cx + a, cy - b),
            (cx + b, cy - a),
            (cx - a, cy - b),
            (cx - b, cy - a),
        ])
    emit(x,y)
    while x < y:
        if d < 0:
            d += 2*x + 3
        else:
            d += 2*(x - y) + 5
            y -= 1
        x += 1
        emit(x,y)
    return sorted(set(pts))
