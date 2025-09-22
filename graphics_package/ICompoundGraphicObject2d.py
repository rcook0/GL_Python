from abc import ABC, abstractmethod
from .IGraphicObject import IGraphicObject

class ICompoundGraphicObject2d(IGraphicObject, ABC):
    @abstractmethod
    def add(self, obj: IGraphicObject) -> None: ...
    @abstractmethod
    def clear(self) -> None: ...
