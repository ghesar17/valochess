import pygame as p
import main
import os
from board import current_board


class Piece(p.sprite.Sprite):

    def __init__(self, board, display, turn, img, row, col, x, y):
        p.sprite.Sprite.__init__(self)
        self.img = img
        self.board = board
        self.display = display
        self.turn = turn
        self.img = img
        self.row = row
        self.col = col
        self.x = x
        self.y = y
        self.image = p.Surface((95, 95))
        self.image.blit()
        # self.image = p.image.load(os.path.join("chess pngs",self.img))
        self.rect = self.image.get_rect(topleft=[self.x, self.y])

    def draw_piece(self):
        self.display.blit(self.image, self.rect)
        # loaded_img = p.image.load(os.path.join("chess pngs", self.img))
        # rect = p.draw.rect(main.screen, [0], [self.x, self.y, 95, 95])
        # rect = loaded_img.get_rect(topleft=[self.x, self.y])
        # piece_group.draw(main.screen)

    def update(self):
        self.rect.right + 5

    def if_selected(self, rect):
        pass

    def move(self):
        if self.turn % 2 == 0:
            pass

        else:
            pass

    def update_current_pos(self):
        pass

    def update_board(self):
        pass

    def get_clicked_piece(self):
        pass


class Pawn(Piece):

    def __init__(self, board, display, turn, img, row, col, x, y):
        super().__init__(board, display, turn, img, row, col, x, y)


class King(Piece):

    def __init__(self, board, display, turn, img, row, col, x, y):
        super().__init__(board, display, turn, img, row, col, x, y)


class Bishop(Piece):

    def __init__(self, board, display, turn, img, row, col, x, y):
        super().__init__(board, display, turn, img, row, col, x, y)


class Knight(Piece):

    def __init__(self, board, display, turn, img, row, col, x, y):
        super().__init__(board, display, turn, img, row, col, x, y)


class Rook(Piece):

    def __init__(self, board, display, turn, img, row, col, x, y):
        super().__init__(board, display, turn, img, row, col, x, y)


class Queen(Piece):

    def __init__(self, screen, turn, img, row, col, x, y):
        super().__init__(turn, screen, img, row, col, x, y)


# instances of the piece classes
all_sprites = p.sprite.Group()

a_wp = Pawn(current_board, main.screen, 0, 'wp.png', 2, 1, 45, 600)

all_sprites.add(a_wp)
# b_wp = Pawn(current_board, main.screen, 0, 'wp.png', 2, 2, 140, 600)
# c_wp = Pawn(current_board, main.screen, 0, 'wp.png', 2, 3, 235, 600)
# d_wp = Pawn(current_board, main.screen, 0, 'wp.png', 2, 4, 330, 600)
# e_wp = Pawn(current_board, main.screen, 0, 'wp.png', 2, 5, 425, 600)
# f_wp = Pawn(current_board, main.screen, 0, 'wp.png', 2, 6, 520, 600)
# g_wp = Pawn(current_board, main.screen, 0, 'wp.png', 2, 7, 615, 600)
# h_wp = Pawn(current_board, main.screen, 0, 'wp.png', 2, 8, 710, 600)

# a_wr = Rook(current_board, main.screen, 0, 'wr.png', 1, 1, 45, 695)
# b_wn = Knight(current_board, main.screen, 0, 'wn.png', 1, 2, 140, 695)
# c_wb = Bishop(current_board, main.screen, 0, 'wb.png', 1, 3, 235, 695)
# wq = Queen(current_board, main.screen, 0, 'wq.png', 1, 4, 330, 695)
# wk = King(current_board, main.screen, 0, 'wk.png', 1, 5, 425, 695)
# f_wb = Bishop(current_board, main.screen, 0, 'wb.png', 1, 6, 520, 695)
# g_wn = Knight(current_board, main.screen, 0, 'wn.png', 1, 7, 615, 695)
# h_wr = Rook(current_board, main.screen, 0, 'wr.png', 1, 8, 710, 695)

# a_bp = Pawn(current_board, main.screen, 0, 'bp.png', 7, 1, 45, 125)
# b_bp = Pawn(current_board, main.screen, 0, 'bp.png', 7, 2, 140, 125)
# c_bp = Pawn(current_board, main.screen, 0, 'bp.png', 7, 3, 235, 125)
# d_bp = Pawn(current_board, main.screen, 0, 'bp.png', 7, 4, 330, 125)
# e_bp = Pawn(current_board, main.screen, 0, 'bp.png', 7, 5, 425, 125)
# f_bp = Pawn(current_board, main.screen, 0, 'bp.png', 7, 6, 520, 125)
# g_bp = Pawn(current_board, main.screen, 0, 'bp.png', 7, 7, 615, 125)
# h_bp = Pawn(current_board, main.screen, 0, 'bp.png', 7, 8, 710, 125)

# a_br = Rook(current_board, main.screen, 0, 'br.png', 8, 1, 45, 30)
# b_bn = Knight(current_board, main.screen, 0, 'bn.png', 8, 2, 140, 30)
# c_bb = Bishop(current_board, main.screen, 0, 'bb.png', 8, 3, 235, 30)
# bq = Queen(current_board, main.screen, 0, 'bq.png', 8, 4, 330, 30)
# bk = King(current_board, main.screen, 0, 'bk.png', 8, 5, 425, 30)
# f_bb = Bishop(current_board, main.screen, 0, 'bb.png', 8, 6, 520, 30)
# g_bn = Knight(current_board, main.screen, 0, 'bn.png', 8, 7, 615, 30)
# h_br = Rook(current_board, main.screen, 0, 'br.png', 8, 8, 710, 30)
