# graphics_package/Buffer.py
import threading
import time
from .Point2d import Point2d
from .Drawing2d import Drawing2d  # must exist or be stubbed

class Buffer:
    """
    Python port of Buffer.
    Manages a drawing object with double-buffered update loop and mouse events.
    """

    def __init__(self):
        self.myDrawing: Drawing2d | None = None
        self.running = False
        self.thread: threading.Thread | None = None

        # Interaction state
        self.click = False
        self.drag = False
        self.selectionPoint = Point2d(0.0, 0.0)

    def setDrawing(self, externalDrawing: Drawing2d) -> None:
        self.myDrawing = externalDrawing

    def getSelectionPoint(self) -> Point2d:
        self.click = False
        return self.selectionPoint

    def animateStart(self) -> None:
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.run, daemon=True)
            self.thread.start()

    def run(self) -> None:
        while self.running:
            # Instead of repaint(), we call update once per cycle
            self.update()
            time.sleep(0.05)

    def animateStop(self) -> None:
        self.running = False
        self.thread = None

    def update(self) -> None:
        """
        Perform one buffer update. In Java this painted via Graphics,
        here we just call draw/erase hooks on myDrawing.
        """
        if self.myDrawing is None:
            self.myDrawing = Drawing2d()
        # Draw then erase — app should override Drawing2d behavior
        self.myDrawing.draw()
        self.myDrawing.erase()

    # --- Interaction emulation (mouse events in Java) ---

    def click_event(self, x: float, y: float) -> None:
        """
        Simulate mouse press: record a selection point.
        """
        if not self.click:
            self.selectionPoint = Point2d(x, y)
        self.click = True
        self.drag = False

    def release_event(self, x: float, y: float) -> None:# graphics_package/Buffer.py
class Buffer:
    """
    Simple 2D buffer for integer pixel values.
    """
# graphics_package/Buffer.py
class Buffer:
    """
    Simple 2D buffer for integer pixel values.
    """

    def __init__(self, width: int, height: int, init: int = 0):
        self.width = width
        self.height = height
        self.data = [[init for _ in range(width)] for _ in range(height)]

    def clear(self, value: int = 0) -> None:
        for y in range(self.height):
            for x in range(self.width):
                self.data[y][x] = value

    def set(self, x: int, y: int, value: int) -> None:
        self.data[y][x] = value

    def get(self, x: int, y: int) -> int:
        return self.data[y][x]

    def __init__(self, width: int, height: int, init: int = 0):
        self.width = width
        self.height = height
        self.data = [[init for _ in range(width)] for _ in range(height)]

    def clear(self, value: int = 0) -> None:
        for y in range(self.height):
            for x in range(self.width):
                self.data[y][x] = value

    def set(self, x: int, y: int, value: int) -> None:
        self.data[y][x] = value

    def get(self, x: int, y: int) -> int:
        return self.data[y][x]

        self.drag = False

    def drag_event(self, x: float, y: float) -> None:
        self.drag = True
        self.selectionPoint = Point2d(x, y)

    def click_ack(self, ck: bool) -> None:
        """
        Application uses this to acknowledge processing of selection.
        """
        self.click = ck

    def currentSelectionPointIsNew(self) -> bool:
        return self.click is True

    def dragging(self) -> bool:
        return self.drag is True
