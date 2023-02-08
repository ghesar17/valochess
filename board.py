import pieces
import main
import os
import pygame as p


class Board():

    def __init__(self, rows, cols):
        # super().__init__()
        # self.image = p.Surface([800, 800])
        # board = p.image.load((os.path.join("chess pngs", 'board.png')))
        # self.rect = self.image.get_rect(topleft=[800,800]
        # self.rect.topleft = [0, 0]
        self.rows = rows
        self.cols = cols

        self.board = [
            ['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr'],
        ]

    # def draw_board(self):
    #     # main.screen
    #     # group.draw(main.screen)
    #     pass

    #     # main.screen.blit(p.image.load(os.path.join("chess pngs", 'board.png')),
    #     #                  (0, 0))

    #   def update_board(self, rows, cols):
    #       pass


current_board = Board(8, 8)

# group = p.sprite.Group()
# group.add(current_board)
