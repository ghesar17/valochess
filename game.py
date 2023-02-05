from pieces import a_wp
import pygame as p
import os


class Piece:

    def __init__(self, screen, turn, img, row, col, x, y):
        self.turn = turn
        self.screen = screen
        self.img = img
        self.row = row
        self.col = col
        self.x = x
        self.y = y

    def draw_piece(self):

        self.screen.blit(p.image.load(os.path.join(
            "chess pngs", self.img)), (self.x, self.y))

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

    def __init__(self, turn, img, row, col, x, y):
        super().__init__(turn, img, row, col, x, y)


class Bishop(Piece):

    def __init__(self, turn, img, row, col, x, y):
        super().__init__(turn, img, row, col, x, y)


class Knight(Piece):

    def __init__(self, turn, img, row, col, x, y):
        super().__init__(turn, img, row, col, x, y)


class Rook(Piece):

    def __init__(self, turn, img, row, col, x, y):
        super().__init__(turn, img, row, col, x, y)


class Queen(Piece):

    def __init__(self, turn, img, row, col, x, y):
        super().__init__(turn, img, row, col, x, y)


# b_wp = Pawn(0, 'wp.png', '2', '2')
# c_wp = Pawn(0, 'wp.png', '2', '3')
# d_wp = Pawn(0, 'wp.png', '2', '4')
# e_wp = Pawn(0, 'wp.png', '2', '5')
# f_wp = Pawn(0, 'wp.png', '2', '6')
# g_wp = Pawn(0, 'wp.png', '2', '7')
# h_wp = Pawn(0, 'wp.png', '2', '8')


# a_bp = Pawn(0, 'bp.png', '7', '1')
# b_bp = Pawn(0, 'bp.png', '7', '2')
# c_bp = Pawn(0, 'bp.png', '7', '3')
# d_bp = Pawn(0, 'bp.png', '7', '4')
# e_bp = Pawn(0, 'bp.png', '7', '5')
# f_bp = Pawn(0, 'bp.png', '7', '6')
# g_bp = Pawn(0, 'bp.png', '7', '7')
# h_bp = Pawn(0, 'bp.png', '7', '8')


# turn, img, row, col, x, y

WIDTH, HEIGHT = 800, 800

# SQ_WIDTH =


screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('VALOCHESS')
p.display.flip()


def main():
    running = True
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
        draw_board()
        a_wp.draw_piece()
        # pieces.a_wp.draw_piece()
        p.display.update()
    p.quit()


def draw_board():
    screen.blit(p.image.load(os.path.join("chess pngs", 'board.png')), (0, 0))


# def draw_pieces():
#     pieces.a_wp.draw_piece()
    # screen.blit(p.image.load(os.path.join("chess pngs", 'wp.png')), (45, 590))


a_wp = Pawn(0, screen, 'wp.png', 2, 1, 45, 490)

if __name__ == '__main__':
    main()
