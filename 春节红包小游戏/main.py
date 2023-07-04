# -*- coding: utf-8 -*-
# time:2023/1/2 23:58
# file main.py
# outhor:czy
# email:1060324818@qq.com

'''

'''

import pygame
import os

WIN = pygame.display.set_mode((900,500))
pygame.display.set_caption("春节抢红包")

bg_color = (255,255,255)
FPS = 60
VEL = 5

hongbao_width,hongbao_height = 40,65
hongbao_X,hongbao_Y = 100,200
hongbao = pygame.image.load(os.path.join('','红包打开.png'))
hongbao_ship = pygame.transform.scale(hongbao,(hongbao_width,hongbao_height))
hongbao_station = pygame.transform.rotate(hongbao_ship,0)

#3.在窗口绘制图形
def draw_window(number):
    WIN.fill(bg_color)
    WIN.blit(hongbao_station,(number.x,number.y))
    pygame.display.update()

#2.获取键盘输入并对目标位置进行改变
def get_pressed(keys_pressed,number):
    if keys_pressed[pygame.K_a]:
        number.x -= VEL
    if keys_pressed[pygame.K_d]:
        number.x += VEL
    if keys_pressed[pygame.K_w]:
        number.y -= VEL
    if keys_pressed[pygame.K_s]:
        number.y += VEL

#1.主函数，程序在死循环中运行
def main():
    clock = pygame.time.Clock()
    number = pygame.Rect(hongbao_X,hongbao_Y,hongbao_width,hongbao_height)
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        get_pressed(keys_pressed,number)


        draw_window(number)

    pygame.QUIT()


if __name__ == '__main__':
    main()