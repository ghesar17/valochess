import pygame as p
import game
import os


class Piece:

    def __init__(self, board, turn, img, row, col, x, y):
        self.turn = turn
        self.board = board
        self.img = img
        self.row = row
        self.col = col
        self.x = x
        self.y = y

    def draw_piece(self):
        self.board.blit(p.image.load(os.path.join("chess pngs", self.img)),
                        (self.x, self.y))
        # piece = p.image.load(os.path.join("chess pngs", self.img))
        # new_piece = p.transform.scale_by(piece, 2)
        # self.board.blit(new_piece, (self.x, self.y))

    def move(self):
        if self.turn % 2 == 0:
            pass

        else:
            pass

    def update_current_pos(self):
        pass

    def update_board(self):
        pass


class Pawn(Piece):

    def __init__(self, screen, turn, img, row, col, x, y):
        super().__init__(turn, screen, img, row, col, x, y)


class King(Piece):

    def __init__(self, screen, turn, img, row, col, x, y):
        super().__init__(turn, screen, img, row, col, x, y)


class Bishop(Piece):

    def __init__(self, screen, turn, img, row, col, x, y):
        super().__init__(turn, screen, img, row, col, x, y)


class Knight(Piece):

    def __init__(self, screen, turn, img, row, col, x, y):
        super().__init__(turn, screen, img, row, col, x, y)


class Rook(Piece):

    def __init__(self, screen, turn, img, row, col, x, y):
        super().__init__(turn, screen, img, row, col, x, y)


class Queen(Piece):

    def __init__(self, screen, turn, img, row, col, x, y):
        super().__init__(turn, screen, img, row, col, x, y)


a_wp = Pawn(0, game.screen, 'wp.png', 2, 1, 45, 600)
b_wp = Pawn(0, game.screen, 'wp.png', 2, 2, 140, 600)
c_wp = Pawn(0, game.screen, 'wp.png', 2, 3, 235, 600)
d_wp = Pawn(0, game.screen, 'wp.png', 2, 4, 330, 600)
e_wp = Pawn(0, game.screen, 'wp.png', 2, 5, 425, 600)
f_wp = Pawn(0, game.screen, 'wp.png', 2, 6, 520, 600)
g_wp = Pawn(0, game.screen, 'wp.png', 2, 7, 615, 600)
h_wp = Pawn(0, game.screen, 'wp.png', 2, 8, 710, 600)

a_wr = Rook(0, game.screen, 'wr.png', 1, 1, 45, 695)
b_wb = Bishop(0, game.screen, 'wb.png', 1, 2, 140, 695)
c_wn = Knight(0, game.screen, 'wn.png', 1, 3, 235, 695)
wq = Queen(0, game.screen, 'wq.png', 1, 4, 330, 695)
wk = King(0, game.screen, 'wk.png', 1, 5, 425, 695)
f_wb = Bishop(0, game.screen, 'wb.png', 1, 6, 520, 695)
g_wn = Knight(0, game.screen, 'wn.png', 2, 7, 615, 695)
h_wr = Rook(0, game.screen, 'wr.png', 2, 8, 710, 695)


# a_bp = Pawn(0, 'bp.png', '7', '1')
# b_bp = Pawn(0, 'bp.png', '7', '2')
# c_bp = Pawn(0, 'bp.png', '7', '3')
# d_bp = Pawn(0, 'bp.png', '7', '4')
# e_bp = Pawn(0, 'bp.png', '7', '5')
# f_bp = Pawn(0, 'bp.png', '7', '6')
# g_bp = Pawn(0, 'bp.png', '7', '7')
# h_bp = Pawn(0, 'bp.png', '7', '8')
