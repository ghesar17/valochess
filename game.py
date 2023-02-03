from pieces import *
import pygame as p
import chess
import os


WIDTH, HEIGHT = 800, 800

# SQ_WIDTH =


screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('VALOCHESS')
p.display.flip()
# p.display.set_icon(os.path.join('chess pngs', 'valornt.jpg'))


# board = p.transform.scale(board_img, (800, 800))


def main():
    running = True
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
        draw_board()
        draw_piece()
        p.display.update()
    p.quit()


def draw_board():
    screen.blit(p.image.load(os.path.join("chess pngs", 'board.png')), (0, 0))


def draw_piece():
    a_w.dra
    screen.blit(p.image.load(os.path.join("chess pngs", 'wp.png')), (45, 590))


if __name__ == '__main__':
    main()
