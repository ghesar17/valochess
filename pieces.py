from game import *
from load import *
import pygame
import os

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


class Piece:
    def __init__(self, color, turn):
        self.color = color
        self.turn = turn

    def draw_piece(self):
        if self.color == 'w':

        p.Surface.blit(self.image(dest=(0, 0)))


class Pawn(Piece):

    def move(self):
        if turn == 'w':
            pass


class King(Piece):

    def move(self):
        if turn == 'w':
            pass


class Bishop(Piece):

    def move(self):
        if turn == 'w':
            pass


class Knight(Piece):

    def move(self):
        if turn == 'w':
            pass


class Rook(Piece):

    def move(self):
        if turn == 'w':
            pass


class Queen(Piece):

    def move(self):
        if turn == 'w':
            pass


b_bishop = Bishop('b', 'w', p.image.load(
    os.path.join('chess pngs', 'black bishop.png')))
b_pawn = Pawn('b', 'w', load.b_pawn)
b_king = ing('b', 'w', load.b_king)
b_queen = Queen('b', 'w', load.b_queen)
b_rook = Rook('b', 'w', load.b_rook)
b_knight = Knight('b', 'w', load.b_knight)

w_bishop = Bishop('w', 'w', load.w_bishop)
w_pawn = Pawn('w', 'w', load.w_pawn)
w_king = King('w', 'w', load.w_king)
w_queen = Queen('w', 'w', load.w_queen)
w_rook = Rook('w', 'w', load.w_rook)
w_knight = Knight('w', 'w', load.w_knight)
