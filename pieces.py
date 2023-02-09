from PIL import Image, ImageTk

class Piece:
  def __init__(self, color, x, y):
      self.color = color
      self.position = (x, y)
      self.moves = []
      self.symbol = ImageTk.PhotoImage(Image.open(f"images/{self.color.lower()}_{self.__class__.__name__.lower()}.jpg"))
  def is_valid_move(self, x, y):
    return (x, y) in self.moves

class Pawn(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.moves = [(x, y + 1)]  # Pawn can move one square forward
        if y == 1:  # Pawn's starting position
            self.moves.append((x, y + 2))

class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.moves = [(x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1),
                      (x + 1, y + 2), (x + 1, y - 2), (x - 1, y + 2), (x - 1, y - 2)]

class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        # A bishop can move any number of squares diagonally
        self.moves = [(x + i, y + i) for i in range(1, 8)] + [(x - i, y - i) for i in range(1, 8)] + \
                     [(x + i, y - i) for i in range(1, 8)] + [(x - i, y + i) for i in range(1, 8)]


class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        # A rook can move any number of squares horizontally or vertically
        self.moves = [(x + i, y) for i in range(1, 8)] + [(x - i, y) for i in range(1, 8)] + \
                     [(x, y + i) for i in range(1, 8)] + [(x, y - i) for i in range(1, 8)]


class Queen(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        # A queen can move any number of squares diagonally, horizontally, or vertically
        self.moves = [(x + i, y + i) for i in range(1, 8)] + [(x - i, y - i) for i in range(1, 8)] + \
                     [(x + i, y - i) for i in range(1, 8)] + [(x - i, y + i) for i in range(1, 8)] + \
                     [(x + i, y) for i in range(1, 8)] + [(x - i, y) for i in range(1, 8)] + \
                     [(x, y + i) for i in range(1, 8)] + [(x, y - i) for i in range(1, 8)]

class King(Piece):
  def init(self, color, x, y):
    super().init(color, x, y)
    self.moves =   [(x + i, y + i) for i in range(-1, 2)] + [(x - i, y - i) for i in range(-1, 2)] + \
                   [(x + i, y - i) for i in range(-1, 2)] + [(x - i, y + i) for i in range(-1, 2)] + \
                   [(x + i, y) for i in range(-1, 2)] + [(x - i, y) for i in range(-1, 2)] + \
                   [(x, y + i) for i in range(-1, 2)] + [(x, y - i) for i in range(-1, 2)]