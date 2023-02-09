import tkinter as tk
from pieces import *


class Color:
    BLACK = 'black'
    WHITE = 'white'


class ChessBoard(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.current_player = Color.WHITE
        self.selected_piece = None

    def create_widgets(self):
        # create the chess board
        self.board = []
        for i in range(8):
            row = []
            for j in range(8):
                square = tk.Label(self, text=" ", bg="white")
                square.grid(row=i, column=j)
                row.append(square)
            self.board.append(row)
        # add a mouse click event to each square
        for row in self.board:
            for square in row:
                square.bind("<Button-1>", self.square_clicked)

        # create the pieces and place them on the board
        self.pieces = []
        for i in range(8):
            self.pieces.append(Pawn(Color.WHITE, i, 6))
            self.pieces.append(Pawn(Color.BLACK, i, 1))
        self.pieces.append(Rook(Color.WHITE, 0, 7))
        self.pieces.append(Rook(Color.WHITE, 7, 7))
        self.pieces.append(Rook(Color.BLACK, 0, 0))
        self.pieces.append(Rook(Color.BLACK, 7, 0))
        self.pieces.append(Knight(Color.WHITE, 1, 7))
        self.pieces.append(Knight(Color.WHITE, 6, 7))
        self.pieces.append(Knight(Color.BLACK, 1, 0))
        self.pieces.append(Knight(Color.BLACK, 6, 0))
        self.pieces.append(Bishop(Color.WHITE, 2, 7))
        self.pieces.append(Bishop(Color.WHITE, 5, 7))
        self.pieces.append(Bishop(Color.BLACK, 2, 0))
        self.pieces.append(Bishop(Color.BLACK, 5, 0))
        self.pieces.append(Queen(Color.WHITE, 3, 7))
        self.pieces.append(Queen(Color.BLACK, 3, 0))
        self.pieces.append(King(Color.WHITE, 4, 7))
        self.pieces.append(King(Color.BLACK, 4, 0))

        # update the display of the pieces on the board
        self.update_pieces()

    def update_pieces(self):
        # update the display of each piece on the board
        for piece in self.pieces:
            row, col = piece.position
            square = self.board[row][col]
            square.config(image=piece.symbol, bg="white" if (
                row + col) % 2 == 0 else "gray")

    def run(self):
        # start the GUI
        self.mainloop()

    def square_clicked(self, event):
        # get the square that was clicked
        square = event.widget
        row, col = (square.grid_info()["row"], square.grid_info()["column"])

        # find the piece on the square, if any
        piece = next(
            (p for p in self.pieces if p.position == (row, col)), None)

        # if a piece is selected, try to move it to the new square
        if self.selected_piece is not None:
            if piece is None and self.selected_piece.can_move_to(row, col):
                self.selected_piece.move_to(row, col)
                self.selected_piece = None
                self.current_player = Color.BLACK if self.current_player == Color.WHITE else Color.WHITE
                self.update_pieces()
        # otherwise, select the piece
        elif piece is not None and piece.color == self.current_player:
            self.selected_piece = piece
            self.highlight_moves(piece)

    def highlight_moves(self, piece):
        # for all the available moves for a piece: highlight the given square from its current position
        available_moves = piece.moves
        for move in available_moves:
            row, col = move
            square = self.board[row][col]
            square["bg"] = "green"


if __name__ == "__main__":
    board = ChessBoard()
    board.run()
