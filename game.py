from pieces import *
import pygame as p
import chess
import os
import load


WIDTH, HEIGHT = 800, 800
screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('VALOCHESS')
# p.display.set_icon(os.path.join('chess pngs', 'valornt.jpg'))


# board = p.transform.scale(board_img, (800, 800))


def main():
    running = True
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
        draw_board()
    p.quit()


def draw_board():
    screen.blit(load.board_img, (0, 0))
    b_bishop.draw_piece()
    p.display.update()


if __name__ == '__main__':
    main()
