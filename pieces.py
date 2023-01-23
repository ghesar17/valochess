from game import *
from load import *
import pygame as p
import os


class Piece:
    def __init__(self, color, turn, image):
        self.color = color
        self.turn = turn
        self.image = image

    def draw_piece(self):
        p.Surface.blit(self.image(dest=(0, 0)))


class pawn(piece):

    def move(self):
        if turn == 'w':
            pass


class king(piece):

    def move(self):
        if turn == 'w':
            pass


class bishop(piece):

    def move(self):
        if turn == 'w':
            pass


class knight(piece):

    def move(self):
        if turn == 'w':
            pass


class rook(piece):

    def move(self):
        if turn == 'w':
            pass


class queen(piece):

    def move(self):
        if turn == 'w':
            pass


b_bishop = bishop('b', 'w', p.image.load(
    os.path.join('chess pngs', 'black bishop.png')))
b_pawn = pawn('b', 'w', load.b_pawn)
b_king = king('b', 'w', load.b_king)
b_queen = queen('b', 'w', load.b_queen)
b_rook = rook('b', 'w', load.b_rook)
b_knight = knight('b', 'w', load.b_knight)

w_bishop = bishop('w', 'w', load.w_bishop)
w_pawn = pawn('w', 'w', load.w_pawn)
w_king = king('w', 'w', load.w_king)
w_queen = queen('w', 'w', load.w_queen)
w_rook = rook('w', 'w', load.w_rook)
w_knight = knight('w', 'w', load.w_knight)


b_knight = pygame.image.load(os.path.join('chess pngs', 'black knight.png'))
b_pawn = pygame.image.load(os.path.join('chess pngs', 'black pawn.png'))
b_king = pygame.image.load(os.path.join('chess pngs', 'black king.png'))
b_rook = pygame.image.load(os.path.join('chess pngs', 'black rook.png'))
b_queen = pygame.image.load(os.path.join('chess pngs', 'black queen.png'))


w_pawn = pygame.image.load(os.path.join('chess pngs', 'white pawn.png'))
w_knight = pygame.image.load(os.path.join('chess pngs', 'white knight.png'))
w_queen = pygame.image.load(os.path.join('chess pngs', 'white queen.png'))
w_king = pygame.image.load(os.path.join('chess pngs', 'white king.png'))
w_bishop = pygame.image.load(os.path.join('chess pngs', 'white bishop.png'))
w_rook = pygame.image.load(os.path.join('chess pngs', 'white rook.png'))

board_img = pygame.image.load(os.path.join('chess pngs', 'board.png'))
