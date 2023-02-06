import pieces
import pygame as p
import os

WIDTH, HEIGHT = 800, 800

SQ_WIDTH = 95

screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('VALOCHESS')
p.display.flip()


def main():
    running = True
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
            # elif event.type == p.MOUSEBUTTONDOWN:
            #     mouse_pos = p.mouse.get_pos()
            #     x = mouse_pos[0]
            #     y = mouse_pos[1]
                
        draw_board()
        draw_pieces()
        p.display.update()
    p.quit()


def draw_board():
    screen.blit(p.image.load(os.path.join("chess pngs", 'board.png')), (0, 0))


def draw_pieces():
    pieces.a_wp.draw_piece()
    pieces.b_wp.draw_piece()
    pieces.c_wp.draw_piece()
    pieces.d_wp.draw_piece()
    pieces.e_wp.draw_piece()
    pieces.f_wp.draw_piece()
    pieces.g_wp.draw_piece()
    pieces.h_wp.draw_piece()

    pieces.a_wr.draw_piece()
    pieces.b_wn.draw_piece()
    pieces.c_wb.draw_piece()
    pieces.wq.draw_piece()
    pieces.wk.draw_piece()
    pieces.f_wb.draw_piece()
    pieces.g_wn.draw_piece()
    pieces.h_wr.draw_piece()

    pieces.a_bp.draw_piece()
    pieces.b_bp.draw_piece()
    pieces.c_bp.draw_piece()
    pieces.d_bp.draw_piece()
    pieces.e_bp.draw_piece()
    pieces.f_bp.draw_piece()
    pieces.g_bp.draw_piece()
    pieces.h_bp.draw_piece()

    pieces.a_br.draw_piece()
    pieces.b_bn.draw_piece()
    pieces.c_bb.draw_piece()
    pieces.bq.draw_piece()
    pieces.bk.draw_piece()
    pieces.f_bb.draw_piece()
    pieces.g_bn.draw_piece()
    pieces.h_br.draw_piece()


if __name__ == '__main__':
    main()
