import pygame
import random
from button import Button
pygame.init()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
w, h = 1200, 630
square_size = (90, 90)

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Игра «Найди пару»')

fon_image = pygame.image.load('images/fon1.png')
der_image = pygame.image.load('images/der.png')
fon = pygame.transform.scale(fon_image, (1200, 630))
der = pygame.transform.scale(der_image, square_size)

clock = pygame.time.Clock()
pygame.mixer.music.load('images/main.mp3')
pygame.mixer.music.play(-1)

my_font = pygame.font.SysFont('Candara',32, True, True)
mini_font = pygame.font.SysFont('Candara',25, True, True)
maxi_font = pygame.font.SysFont('Candara',55, True, True)

f_images = ['images/f1.png', 'images/f2.png', 'images/f3.png', 'images/f4.png', 'images/f5.png',
            'images/f6.png','images/f7.png', 'images/f8.png', 'images/f9.png']
f = list()
for link in f_images:
    im = pygame.image.load((link))
    im = pygame.transform.scale(im, square_size)
    f.append(im)

TIME = pygame.USEREVENT + 1
pygame.time.set_timer(TIME, 1000)

z = list()
for pos in range(300, 811, 102):
    z.append((pos, 200))
    z.append((pos, 300))
    z.append((pos, 400))
draw = [True] * 18
im_pos = {}

restart = Button((w//2, h//2+200), 190, 50, 'images/but.png', 'Заново!')
start_game = Button((w//2, h//2+200), 190, 50, 'images/but.png', 'Начать игру!')


def show():
    random.shuffle(z)
    for i in range(9):
        im_pos[f[i]] = set()
        im_pos[f[i]].add(z[i * 2])
        im_pos[f[i]].add(z[i * 2 + 1])
    screen.blit(fon, (0, 0))
    for i in range(9):
        screen.blit(f[i], z[2 * i])
        screen.blit(f[i], z[2 * i + 1])
    ex = my_font.render(f'Найди пару', True, BLACK)
    r1 = ex.get_rect(center=(w // 2, h // 2 - 200))
    screen.blit(ex, r1)
    pygame.display.flip()
    pygame.time.delay(2000)


sek, schet = 0, 0
flag, hod = 1, 0
pl1, pl2 = 0, 0
run = True
close = False
start = True
while run:
    #меню для начала игры
    while start:
        screen.blit(fon, (0, 0))
        area = pygame.Surface((w, h))
        area.fill((0, 0, 0))
        area.set_alpha(20)
        screen.blit(area, (0, 0))
        start_game.draw(screen)
        name = maxi_font.render(f'Найди пару', True, BLACK)
        r1 = name.get_rect(center=(w // 2, h // 2 - 100))
        screen.blit(name, r1)
        pygame.display.update()
        start_game.press_button()
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT and event.button == start_game:
                show()
                start = False
            if event.type == pygame.QUIT:
                start = False
                run = False

    #меню для конца игры
    while close:
        screen.blit(fon, (0, 0))
        area = pygame.Surface((w, h))
        area.fill((0, 0, 0))
        area.set_alpha(20)
        screen.blit(area, (0, 0))
        restart.draw(screen)
        ex = my_font.render(f'Отлично!', True, BLACK)
        r1 = ex.get_rect(center=(w // 2, h // 2 - 100))
        vrs = my_font.render(f'Ты сделал это за {sek} секунд', True, BLACK)
        r2 = vrs.get_rect(center=(w // 2, h // 2))
        PL1 = my_font.render(f'Игрок1 победил!', True, BLACK)
        r3 = PL1.get_rect(center=(w // 2, h // 2 + 100))
        if pl1 > pl2:
            screen.blit(PL1, r3)
        if pl2 > pl1:
            PL2 = my_font.render(f'Игрок2 победил!', True, BLACK)
            screen.blit(PL2, r3)
        screen.blit(ex, r1)
        screen.blit(vrs, r2)
        pygame.display.update()
        restart.press_button()
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT and event.button == restart:
                draw = [True] * 18
                im_pos = {}
                sek, schet = 0, 0
                flag, hod = 1, 0
                pl1, pl2 = 0, 0
                show()
                run = True
                close = False
            if event.type == pygame.QUIT:
                close = False
                run = False

    #отрисовка названия, квадратиков, картинок и карточек
    screen.blit(fon, (0, 0))
    ex = my_font.render(f'Найди пару', True, BLACK)
    r1 = ex.get_rect(center=(w // 2, h // 2 - 200))
    screen.blit(ex, r1)

    for pos in range(300, 811, 102):
        pygame.draw.rect(screen, BLACK, (pos, 200, 90, 90), 1)
        pygame.draw.rect(screen, BLACK, (pos, 300, 90, 90), 1)
        pygame.draw.rect(screen, BLACK, (pos, 400, 90, 90), 1)

    for i in range(9):
        screen.blit(f[i], z[2 * i])
        screen.blit(f[i], z[2 * i + 1])

    s = 0
    rct = []
    for x in draw:
        if x and x != 'guessed':
            screen.blit(der, z[s])
        r = der.get_rect(topleft=z[s])
        rct.append(r.topleft)
        s += 1

    #нажатие на карточку, проверка совпадения картинок
    p = pygame.mouse.get_pressed()
    if p[0]:
        pos = pygame.mouse.get_pos()
        for i in range(len(rct)):
            rt = pygame.rect.Rect(rct[i][0], rct[i][1], 90, 90)
            if rt.collidepoint(pos) and draw[i] != 'guessed':
                draw[i] = False

    if draw.count(False) == 2:
        z_true = set()
        k = []
        for i in range(len(draw)):
            if not draw[i]:
                k.append(i)
                z_true.add(rct[i])
        for foto, z_set in im_pos.items():
            if z_set == z_true:
                schet += 1
                draw[k[0]] = 'guessed'
                draw[k[1]] = 'guessed'
                flag = 0
                if hod % 2 == 0:
                    pl1 += 1
                else:
                    pl2 += 1
                break

    if draw.count(False) == 3:
        if flag:
            hod += 1
            draw[k[0]] = True
            draw[k[1]] = True
        flag = 1

    #отрисовка других надписей
    pl_queue = 'Текущий игрок: Игрок1' if hod % 2 == 0 else 'Текущий игрок: Игрок2'
    cur_pl = mini_font.render(pl_queue, True, BLACK)
    r_cur = cur_pl.get_rect(center=(w // 2, 30))
    vr = mini_font.render(f'Время:{sek}',True, BLACK)
    sch = mini_font.render(f'Количество оставшихся карточек: {schet}/9', True, BLACK)
    r2 = sch.get_rect(topright=(w-10, 0))
    pl11 = my_font.render(f'Игрок1={pl1}', True, BLACK)
    r3 = pl11.get_rect(topleft=(10, 30))
    pl22 = my_font.render(f'Игрок2={pl2}', True, BLACK)
    r4 = pl22.get_rect(topleft=(10, 70))
    screen.blit(vr, (10, 0))
    screen.blit(cur_pl, r_cur)
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
