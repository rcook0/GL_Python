
from typing import List, Tuple

def de_casteljau(ctrl: List[Tuple[float,float]], t: float) -> Tuple[float,float]:
    pts = [(float(x),float(y)) for x,y in ctrl]
    n = len(pts)
    for r in range(1, n):
        pts = [((1-t)*pts[i][0] + t*pts[i+1][0],
                (1-t)*pts[i][1] + t*pts[i+1][1]) for i in range(n-r)]
    return pts[0]

def sample(ctrl: List[Tuple[float,float]], segments: int = 10) -> List[Tuple[float,float]]:
    if not ctrl: return []
    if segments <= 0: return [ctrl[0], ctrl[-1]]
    dt = 1.0 / segments
    out = []
    t = 0.0
    for k in range(segments+1):
        out.append(de_casteljau(ctrl, t))
        t += dt
        if t > 1.0: t = 1.0
    return out
