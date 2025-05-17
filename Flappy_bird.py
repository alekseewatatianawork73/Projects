import random
import pygame
from button import Button



pygame.init()
BLACK = (0, 0, 0)
greenbl = (0, 255, 0)


# создаём таймер для установки частоты смены кадров
clock = pygame.time.Clock()

# создаём игровое окно и задаём фон экрана
w, h = 800, 672
x, y = w/2 + 100, h/2
screen = pygame.display.set_mode((w, h))
bg = pygame.image.load('im/bg.png')

x_c, r = w - 30, random.randint(0, 250)
pygame.display.set_caption("Flappy Bird")

# основной игрок - птичка
class Bird(pygame.sprite.Sprite):
    def __init__(self, surf):
        super().__init__()
        self.image = surf
        self.rect = self.image.get_rect(center=(150, h / 2))
        self.add(all_players)

    def update(self):
        p = pygame.key.get_pressed()
        if p[pygame.K_UP]:
            self.rect.y -= 7
        else:
            self.rect.y += 10
class Bar1(pygame.sprite.Sprite):
    def __init__(self, r, surf, group):
        super().__init__()
        self.image = surf
        self.image = pygame.transform.scale(self.image, (130, r))
        self.rect = self.image.get_rect(topleft=(w, 0))
        self.add(group)
        self.add(all_players)

    def update(self):
        if self.rect.x > 0:
            self.rect.x -= 5
        else:
            self.kill()

class Bar2(pygame.sprite.Sprite):
    def __init__(self, r, surf, group):
        super().__init__()
        self.image = surf
        self.image = pygame.transform.scale(self.image, (130, 400 - r))
        self.rect = self.image.get_rect(bottomleft=(w, 672))
        self.add(group)
        self.add(all_players)

    def update(self):
        if self.rect.x > 0:
            self.rect.x -= 5
        else:
            self.kill()


#musik
circle_sound = pygame.mixer.Sound('sounds/circle.wav')
end_sound = pygame.mixer.Sound('sounds/game_over.wav')
pygame.mixer.music.load('sounds/main.mp3')
pygame.mixer.music.play(-1)

#картинки
bird = pygame.image.load('im/bird.png')
bird = pygame.transform.scale(bird, (50, 50))
bird2 = pygame.image.load('im/ird.png')
bird2 = pygame.transform.scale(bird2, (80, 80))

bird_new = pygame.image.load('im/bird.png')
immm = pygame.image.load('im/yel.png')
bor1 = pygame.transform.scale(immm, (130, 100))
bor2 = pygame.transform.scale(immm, (130, 100))

# создание групп спрайтов
cores = pygame.sprite.Group()
all_players = pygame.sprite.Group()

# создание объектов-игроков
player = Bird(bird)


#musik
circle_sound = pygame.mixer.Sound('sounds/circle.wav')
end_sound = pygame.mixer.Sound('sounds/game_over.wav')
pygame.mixer.music.load('sounds/main.mp3')
pygame.mixer.music.play(-1)


#text
f_end = pygame.font.SysFont(name='Pristina', size=50, bold=False, italic=True)
game_over = f_end.render('GAME OVER', True, (000, 000, 000))
new_start = f_end.render('ENTER - new game', True, (000, 000, 000))

count = 0

ADDAPPLE = pygame.USEREVENT + 1
GREENHTOTO = pygame.USEREVENT + 2

pygame.time.set_timer(ADDAPPLE, 1800)

start = True
menu = False
close = False
run = True
while run:
    clock.tick(60)
    while start:
        screen.blit(bg, (0, 0))
        # перекрываем основной экран синим полупрозрачным фоном
        area = pygame.Surface((w, h))
        area.fill((100, 200, 255))
        area.set_alpha(100)
        # отображаем надпись ПАУЗА
        pause = f_end.render('Flappy Bird', True, (0, 0, 0))
        r1 = pause.get_rect(center=(w / 2, h / 2 - 200))
        screen.blit(area, (0, 0))
        screen.blit(pause, r1)

        # кнопка для продолжения игры
        button_continue = Button((w / 2, h / 2), 300, 125, 'im/button.png', 'START')
        button_continue.draw(screen)

        #INSTRUKTIONS
        f_st = pygame.font.SysFont(name='Pristina ', size=45, bold=False, italic=False)

        sh = f_st.render('Menu/Pause - shift', True, (000, 000, 000))
        screen.blit(sh, (250, 450))

        pygame.display.update()
        button_continue.press_button()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                start = False
            if event.type == pygame.USEREVENT:
                if event.button == button_continue:
                    start = False

#################
    while menu:
        screen.blit(bg, (0, 0))
        # перекрываем основной экран синим полупрозрачным фоном
        area = pygame.Surface((w, h))
        area.fill((100, 200, 255))
        area.set_alpha(100)
        # отображаем надпись ПАУЗА
        pause = f_end.render('PAUSE', True, (0, 0, 0))
        r1 = pause.get_rect(center=(w / 2, h / 2 - 200))
        screen.blit(area, (0, 0))
        screen.blit(pause, r1)

        # кнопка для продолжения игры
        button_continue = Button((w / 2, h / 2), 300, 125, 'im/button.png', 'CONTINUE')
        button_continue.draw(screen)

        # кнопка для замены автомобиля
        button_change = Button((w / 2, h / 2 + 100), 300, 125, 'im/button.png', 'CHANGE BIRD')
        button_change.draw(screen)

        # кнопка для того, чтобы начать игру заново
        button_restart = Button((w / 2, h / 2 + 200), 300, 125, 'im/button.png', 'END')
        button_restart.draw(screen)

        pygame.display.update()
        button_continue.press_button()
        button_restart.press_button()
        button_change.press_button()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                menu = False
            if event.type == pygame.USEREVENT:
                if event.button == button_continue:
                    menu = False
                if event.button == button_change:
                    menu = False
                    player.kill()
                    bird, bird2 = bird2, bird
                    player = Bird(bird)
                    for core in cores:
                        core.kill()
                if event.button == button_restart:
                    menu = False
                    close = True

    # обработка завершения игры при проигрыше
    while close:
        screen.blit(bg, (0, 0))
        r = game_over.get_rect(center=(w / 2, h / 2 - 100))
        rct2 = new_start.get_rect(center=(w / 2, h / 2 + 100))
        rct3 = score.get_rect(center=(w / 2, h / 2))
        screen.blit(game_over, r)
        screen.blit(new_start, rct2)
        screen.blit(score, rct3)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = False
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER:
                close = False
                count = 0
                x_c = w
                y = h / 2
                player.kill()
                for core in cores:
                    core.kill()
                player = Bird(bird)
    if not run:
        break



    # отображение на экране счёта и количества жизней
    screen.blit(bg, (0, 0))
    score = f_end.render(f'Score: {count}', True, BLACK)
    sc = score.get_rect(topleft=(0, 0))





    if player.rect.y > 672 or player.rect.y < 0:
        close = True
        end_sound.play()

    for event in pygame.event.get():
        # обработка появления на экране новых яблок и ракет
        if event.type == ADDAPPLE:
            new_core = True
            r = random.randint(0, 250)
            Bar1(r, bor1, cores)
            Bar2(r, bor2, cores)

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RSHIFT:
            menu = True

    # обновляем положение спрайтов на экране и отображаем их
    all_players.update()
    all_players.draw(screen)
    screen.blit(score, sc)
    pygame.display.flip()
        # обработка столкновений
    spr_circle = pygame.sprite.spritecollide(player, cores, True)
    if spr_circle:
        close = True
        end_sound.play()
    for x in cores:
        if x.rect.x == player.rect.x:
            count += 1
            circle_sound.play()
            break

pygame.quit()
