class Location:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __iter__(self):
        return iter((self.x, self.y))
    
    def __repr__(self):
        return f"({self.x}, {self.y})"
