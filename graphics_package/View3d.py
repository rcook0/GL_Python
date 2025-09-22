"""Auto-translated skeleton from WINDOWS/Desktop/GraphicsPackage/View3d.java.
This file preserves classes, methods, and fields.
Bodies marked TODO.
"""
from __future__ import annotations
from typing import Any, Optional, List, Dict, Tuple, Iterable
import math

class View3d:
    def __init__(self):
        self.PT_PARALLEL = None
        self.PT_PERSPECTIVE = None
        self.PT_DEFAULT = None
        self.projectionType = None
        self.CLIP_HITHER = None
        self.CLIP_YON = None
        self.umin = None
        self.umax = None
        self.vmin = None
        self.vmax = None
        self.backDistance = None
        self.frontDistance = None
        self.Xvmin = None
        self.Xvmax = None
        self.Yvmin = None
        self.Yvmax = None
        self.Zvmin = None
        self.Zvmax = None
        self.prp = None
        self.frontDistance = None
        self.backDistance = None
        self.DOPx = None
        self.DOPy = None
        self.DOPz = None
        self.DOPw = None
        self.SHXpar = None
        self.SHYpar = None
        self.vrp_z = None
        self.sx = None
        self.sy = None
        self.sz = None
        self.nper = None
        self.tmin = None
        self.dx = None
        self.dz = None
        self.accept = None
        self.dy = None
        self.true = None
        self.false = None
        self.t = None
        self.false = None
        self.false = None
        self.tL = None
        self.false = None
        self.true = None
        self.mVV3DV = None
        """TODO: Translate constructor body from Java."""
        pass

    def prp(self):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def switch(self, PROJECTION_TYPE):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def setParallelViewport(self):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def setPerspectiveViewport(self):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def setOrientation(self, vrp_in, vpn_in, vup_in):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def setWindow(self, new_umin, new_umax, new_vmin, new_vmax):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def width(self):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def height(self):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def integerWidth(self):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def integerHeight(self):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def setPRP(self, prp_in):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def setViewport(self, xmin, xmax, ymin, ymax, zmin, zmax):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def f(self):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def b(self):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def perspectiveProject(self):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def nPar(self):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def nPer(self):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def clip3d(self, line, zmin):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def if(self, 1.0):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def if(self, 0.0):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def if(self, accept):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def CLIPt(self, denom, num, tE, tL):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def if(self, 0):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def if(self, 0):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def mVV3DV(self):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def project2D(self):
        """TODO: Translate method body from Java."""
        raise NotImplementedError

    def main(self, args):
        """TODO: Translate method body from Java."""
        raise NotImplementedError
