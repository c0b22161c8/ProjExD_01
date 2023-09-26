import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg1_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg2_img = pg.transform.flip(bg1_img, True, False)
    ko1_img = pg.image.load("ex01/fig/3.png")
    ko1_img = pg.transform.flip(ko1_img, True, False)
    ko2_img = pg.transform.rotozoom(ko1_img, 2, 1.0)
    ko3_img = pg.transform.rotozoom(ko1_img, 4, 1.0)
    ko4_img = pg.transform.rotozoom(ko1_img, 6, 1.0)
    ko5_img = pg.transform.rotozoom(ko1_img, 8, 1.0)
    ko6_img = pg.transform.rotozoom(ko1_img, 10, 1.0)
    ko_li = [ko1_img, ko2_img, ko3_img, ko4_img, ko5_img, ko6_img, ko5_img, ko4_img, ko3_img, ko2_img]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg1_img, [1600-((tmr+1600)%3200), 0])
        screen.blit(bg2_img, [1600-(tmr%3200), 0])
        screen.blit(ko_li[tmr%10], [300, 200])
        pg.display.update()
        tmr += 1
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()