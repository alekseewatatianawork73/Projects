import pygame
import random

from button import Button
pygame.init()
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
RED = (255, 0, 0)
w, h = 1200, 630
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Игра «Найди пару»')

size = (90, 90)

fon = pygame.image.load('images/fon1.png')
der = pygame.image.load('images/der.png')
res = pygame.image.load('images/but.png')
fons = pygame.transform.scale(fon, (1200, 630))
ders = pygame.transform.scale(der, size)



pygame.mixer.music.load('images/main.mp3')

pygame.mixer.music.play(-1)


f_end = pygame.font.SysFont('Candara',32, True, True)
f_end1 = pygame.font.SysFont('Candara',25, True, True)
f_end2 = pygame.font.SysFont('Candara',55, True, True)

start_text='Начать игру!'
restart_text='Заново!'




f_image = ['images/f1.png', 'images/f2.png', 'images/f3.png', 'images/f4.png', 'images/f5.png', 'images/f6.png','images/f7.png', 'images/f8.png', 'images/f9.png']

f = []
for link in f_image:
    im = pygame.image.load((link))
    im = pygame.transform.scale(im, size)
    f.append(im)

TIME = pygame.USEREVENT + 1
pygame.time.set_timer(TIME, 1000)


z = [(300, 200), (402, 200), (504, 200), (606, 200), (708, 200), (810, 200), (300, 300), (402, 300), (504, 300), (606, 300), (708, 300), (810, 300), (300, 400), (402, 400), (504, 400), (606, 400), (708, 400), (810, 400)]
random.shuffle(z)




sek, schet = 0, 0
run = True
close = False
nach=True
flag = 1
pl1, pl2 = 0, 0
hod = 0
draw = [True] * 18
im_pos = {}
for i in range(9):
    im_pos[f[i]] = set()
    im_pos[f[i]].add(z[i*2])
    im_pos[f[i]].add(z[i*2 + 1])

restart = Button((w//2, h//2+200), 190, 50, 'images/but.png', restart_text)
nachat = Button((w//2, h//2+200), 190, 50, 'images/but.png', start_text)
while run:

    #меню для начала
    while nach:
        screen.blit(fons, (0, 0))
        area = pygame.Surface((w, h))
        area.fill((0, 0, 0))
        area.set_alpha(20)
        screen.blit(area, (0, 0))
        nachat.draw(screen)
        ex = f_end2.render(f'Найди пару', True, BLACK)
        r1 = ex.get_rect(center=(w // 2, h // 2 - 100))
        screen.blit(ex, r1)
        pygame.display.update()
        nachat.press_button()
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT and event.button == nachat:
                screen.blit(fons, (0, 0))
                for i in range(9):
                    screen.blit(f[i], z[2 * i])
                    screen.blit(f[i], z[2 * i + 1])
                ex = f_end.render(f'Найди пару', True, BLACK)
                r1 = ex.get_rect(center=(w // 2, h // 2 - 200))
                screen.blit(ex, r1)
                pygame.display.flip()
                pygame.time.delay(2000)
                nach=False
            if event.type == pygame.QUIT:
                nach=False
                run = False

    #меню для конца
    while close:
        screen.blit(fons, (0, 0))
        area = pygame.Surface((w, h))
        area.fill((0, 0, 0))
        area.set_alpha(20)
        screen.blit(area, (0, 0))
        restart.draw(screen)
        ex = f_end.render(f'Отлично!', True, BLACK)
        r1 = ex.get_rect(center=(w//2, h//2-100))
        vrs = f_end.render(f'Ты сделал это за {sek} секунд', True, BLACK)
        r2 = vrs.get_rect(center=(w//2, h//2))
        PL1 = f_end.render(f'Игрок1 победил!', True, RED)
        r3 = PL1.get_rect(center=(w // 2, h //2+100))
        PL2 = f_end.render(f'Игрок2 победил!', True, RED)
        if pl1 > pl2:
            screen.blit(PL1, r3)
        if pl2 > pl1:
            screen.blit(PL2, r3)
        screen.blit(ex, r1)
        screen.blit(vrs, r2)
        pygame.display.update()
        restart.press_button()
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT and event.button == restart:
                random.shuffle(z)
                sek, schet = 0, 0
                run = True
                close = False
                flag = 1
                pl1, pl2 = 0, 0
                q = 0
                draw = [True] * 18
                d = {}
                for i in range(9):
                    d[f[i]] = set()
                    d[f[i]].add(z[i*2])
                    d[f[i]].add(z[i*2 + 1])

                screen.blit(fons, (0, 0))
                for i in range(9):
                    screen.blit(f[i], z[2 * i])
                    screen.blit(f[i], z[2 * i + 1])
                ex = f_end.render(f'Найди пару', True, BLACK)
                r1 = ex.get_rect(center=(w // 2, h // 2 - 200))
                screen.blit(ex, r1)
                pygame.display.flip()
                pygame.time.delay(2000)
            if event.type == pygame.QUIT:
                close = False
                run = False

    #отрисовка названия, квадратиков, картинок и карточек
    screen.blit(fons, (0, 0))
    ex = f_end.render(f'Найди пару', True, BLACK)
    r1 = ex.get_rect(center=(w // 2, h // 2 - 200))
    screen.blit(ex, r1)


    for pos in range(300, 811, 102):
        pygame.draw.rect(screen, BLACK, (pos, 200, 90, 90), 1)
        pygame.draw.rect(screen, BLACK, (pos, 300, 90, 90), 1)
        pygame.draw.rect(screen, BLACK, (pos, 400, 90, 90), 1)

    for i in range(9):
        screen.blit(f[i], z[2 * i])
        screen.blit(f[i], z[2 * i + 1])

    s = -1
    rct = []
    for x in draw:
        s += 1
        if x and x != 5:
            screen.blit(ders, z[s])
        r = ders.get_rect(topleft=z[s])
        rct.append(r.topleft)





    #нажатие на карточку, проверка совпадения картинок
    p = pygame.mouse.get_pressed()
    if p[0]:
        pos = pygame.mouse.get_pos()
        for i in range(len(rct)):
            rt = pygame.rect.Rect(rct[i][0], rct[i][1], 90, 90)
            if rt.collidepoint(pos) and draw[i] != 5:
                draw[i] = False


    if draw.count(False) == 2:
        z_true = set()
        k = []
        for i in range(len(draw)):
            if not draw[i]:
                k.append(i)
                z_true.add(rct[i])
        if hod % 2 == 0:
            for foto, z_set in im_pos.items():
                if z_set == z_true:
                    schet += 1
                    draw[k[0]] = 5
                    draw[k[1]] = 5
                    flag = 0
                    pl1 += 1
                    break
        if hod % 2 != 0:
            for foto, z_set in im_pos.items():
                if z_set == z_true:
                    schet += 1
                    draw[k[0]] = 5
                    draw[k[1]] = 5
                    flag = 0
                    pl2 += 1
                    break

    if draw.count(False) == 3:
        if flag:
            hod += 1
            draw[k[0]] = True
            draw[k[1]] = True
        flag = 1


    #отрисовка других надписей
    vr = f_end1.render(f'Время:{sek}',True, BLACK)
    sch = f_end1.render(f'Количество оставшихся карточек: {schet}/9', True, BLACK)
    r2 = sch.get_rect(topright=(w-10, 0))
    pl11 = f_end.render(f'Игрок1={pl1}', True, BLACK)
    r3 = pl11.get_rect(topleft=(10, 30))
    pl22 = f_end.render(f'Игрок2={pl2}', True, BLACK)
    r4 = pl22.get_rect(topleft=(10, 70))

    screen.blit(vr, (10, 0))
    screen.blit(sch, r2)
    screen.blit(pl11, r3)
    screen.blit(pl22, r4)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == TIME:
            sek += 1
        if event.type == pygame.QUIT:
            run = False
    if schet == 9:
        close = True

pygame.quit()
