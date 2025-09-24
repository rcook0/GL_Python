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
