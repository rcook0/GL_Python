"""
shapes.py
Primitive shape generators for 3D rendering.
Each function returns a list of Polygon3D triangles.
"""

import numpy as np
from point3d import Point3d
from polygon3d import Polygon3D

# ----------------------
# Hardcoded primitives
# ----------------------

def make_cube(size=1.0):
    """Return a cube centered at origin, side length = size."""
    s = size / 2
    # 8 vertices
    v = [
        Point3d(-s, -s, -s), Point3d(s, -s, -s),
        Point3d(s,  s, -s),  Point3d(-s,  s, -s),
        Point3d(-s, -s,  s), Point3d(s, -s,  s),
        Point3d(s,  s,  s),  Point3d(-s,  s,  s)
    ]
    # 12 triangles
    faces = [
        (0,1,2), (0,2,3),   # back
        (4,6,5), (4,7,6),   # front
        (0,4,5), (0,5,1),   # bottom
        (3,2,6), (3,6,7),   # top
        (1,5,6), (1,6,2),   # right
        (0,3,7), (0,7,4)    # left
    ]
    return [Polygon3D([v[a], v[b], v[c]]) for (a,b,c) in faces]


def make_tetrahedron(size=1.0):
    """Return a tetrahedron centered at origin."""
    s = size / 2
    v = [
        Point3d( s,  s,  s),
        Point3d(-s, -s,  s),
        Point3d(-s,  s, -s),
        Point3d( s, -s, -s)
    ]
    faces = [(0,1,2), (0,3,1), (0,2,3), (1,3,2)]
    return [Polygon3D([v[a], v[b], v[c]]) for (a,b,c) in faces]


# ----------------------
# Parametric primitives
# ----------------------

def make_cone(radius=1.0, height=2.0, n=32):
    """Return a cone with circular base and apex at +z."""
    polys = []
    apex = Point3d(0, 0, height/2)
    base_center = Point3d(0, 0, -height/2)
    # base circle
    angles = np.linspace(0, 2*np.pi, n, endpoint=False)
    pts = [Point3d(radius*np.cos(a), radius*np.sin(a), -height/2) for a in angles]
    for i in range(n):
        p0, p1 = pts[i], pts[(i+1)%n]
        # side triangle
        polys.append(Polygon3D([apex, p0, p1]))
        # base triangle
        polys.append(Polygon3D([base_center, p1, p0]))
    return polys


def make_sphere(radius=1.0, n_lat=16, n_lon=32):
    """Return a parametric sphere."""
    polys = []
    for i in range(n_lat):
        theta1, theta2 = np.pi*i/n_lat, np.pi*(i+1)/n_lat
        for j in range(n_lon):
            phi1, phi2 = 2*np.pi*j/n_lon, 2*np.pi*(j+1)/n_lon

            def sp(theta, phi):
                return Point3d(
                    radius*np.sin(theta)*np.cos(phi),
                    radius*np.sin(theta)*np.sin(phi),
                    radius*np.cos(theta)
                )

            p00 = sp(theta1, phi1)
            p01 = sp(theta1, phi2)
            p10 = sp(theta2, phi1)
            p11 = sp(theta2, phi2)

            if i != 0:
                polys.append(Polygon3D([p00, p10, p11]))
            if i != n_lat-1:
                polys.append(Polygon3D([p00, p11, p01]))
    return polys


def make_torus(R=1.0, r=0.3, nu=32, nv=16):
    """Return a parametric torus centered at origin."""
    polys = []
    for i in range(nu):
        for j in range(nv):
            u1, u2 = 2*np.pi*i/nu, 2*np.pi*(i+1)/nu
            v1, v2 = 2*np.pi*j/nv, 2*np.pi*(j+1)/nv

            def tp(u, v):
                return Point3d(
                    (R + r*np.cos(v))*np.cos(u),
                    (R + r*np.cos(v))*np.sin(u),
                    r*np.sin(v)
                )

            p00, p01 = tp(u1,v1), tp(u1,v2)
            p10, p11 = tp(u2,v1), tp(u2,v2)
            polys.append(Polygon3D([p00, p10, p11]))
            polys.append(Polygon3D([p00, p11, p01]))
    return polys

# ----------------------
# Shape registry with sensible defaults
# ----------------------

def make_shapes_dict():
"""
    Return a dictionary mapping shape names to generator functions
    with reasonable defaults.
    """
    return {
        "cube": lambda: make_cube(size=1.0),
        "tetrahedron": lambda: make_tetrahedron(size=1.0),
        "cone": lambda: make_cone(radius=1.0, height=2.0, n=32),
        "sphere": lambda: make_sphere(radius=1.0, n_lat=16, n_lon=32),
        "torus": lambda: make_torus(R=1.0, r=0.3, nu=32, nv=16),
    }
