from .IGraphicObject import IGraphicObject
from .Point2d import Point2d
from .Transformation2d import Transformation2d

class GraphicObject2d(IGraphicObject):
    className = "GraphicObject2d"

    def __init__(self, localOrigin: Point2d | None = None):
        self.localOrigin = localOrigin or Point2d(0, 0)

    def draw(self, g=None) -> None:
        pass

    def erase(self, g=None) -> None:
        pass

    def transform(self, trans: Transformation2d) -> None:
        # Assumes Transformation2d supports matrix @ Point2d multiplication
        self.localOrigin = trans @ self.localOrigin

    def getLocalOrigin(self) -> Point2d:
        return self.localOrigin

    def setLocalOrigin(self, p: Point2d) -> None:
        self.localOrigin = p

    def __str__(self) -> str:
        return f"{self.className} at {self.localOrigin}"
