import pygame as p
import os
import pieces


def main():
    running = True
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
        draw_board()
        draw_pieces()
        p.display.update()
    p.quit()


def draw_board():
    display.screen.blit(p.image.load(
        os.path.join("chess pngs", 'board.png')), (0, 0))


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
    pieces.a_wr.draw_piece()
    pieces.a_wr.draw_piece()
    pieces.a_wr.draw_piece()

    # b_wn.draw_piece()
    # c_wb.draw_piece()
    # wq.draw_piece()
    # wk.draw_piece()
    # f_wb.draw_piece()
    # g_wn.draw_piece()
    # h_wr.draw_piece()

    # a_bp.draw_piece()
    # b_bp.draw_piece()
    # c_bp.draw_piece()
    # d_bp.draw_piece()
    # e_bp.draw_piece()
    # f_bp.draw_piece()
    # g_bp.draw_piece()
    # h_bp.draw_piece()

    # a_br.draw_piece()
    # b_bn.draw_piece()
    # c_bb.draw_piece()
    # bq.draw_piece()
    # bk.draw_piece()
    # f_bb.draw_piece()
    # g_bn.draw_piece()
    # h_br.draw_piece()


if __name__ == '__main__':
    main()
