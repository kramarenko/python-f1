import pygame
import player as player
import mob as mob
import explosion as explosion
import pow as pow
from os import path
import random

WIDTH = 480
HEIGHT = 600
FPS = 60
POWERUP_TIME = 5000

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter!")
clock = pygame.time.Clock()
font_name = pygame.font.match_font('arial')


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)


def newmob():
    m = mob.Mob(WIDTH, HEIGHT)
    all_sprites.add(m)
    mobs.add(m)


def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)


def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "SHMUP!", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Arrow keys move, Space to fire", 22,
              WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Press a key to begin", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                waiting = False


img_dir = path.join(path.dirname(__file__), 'img')
sound_dir = path.join(path.dirname(__file__), 'sound')
background = pygame.image.load(path.join(img_dir, 'starfield.jpg')).convert()
background_rect = background.get_rect()
pygame.mixer.music.load(path.join(sound_dir, 'theme.mp3'))
pygame.mixer.music.set_volume(0.4)

shield_sound = pygame.mixer.Sound(path.join(sound_dir, 'pow4.wav'))
power_sound = pygame.mixer.Sound(path.join(sound_dir, 'pow5.wav'))

player_img = pygame.image.load(path.join(img_dir, "playerShip1_orange.png")).convert()
player_mini_img = pygame.transform.scale(player_img, (25, 19))
player_mini_img.set_colorkey(BLACK)

powerup_images = {}
powerup_images['shield'] = pygame.image.load(path.join(img_dir, 'shield_gold.png')).convert()
powerup_images['gun'] = pygame.image.load(path.join(img_dir, 'bolt_gold.png')).convert()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
powerups = pygame.sprite.Group()

user = player.Player(WIDTH, HEIGHT, POWERUP_TIME)
all_sprites.add(user)

for i in range(8):
    newmob()

score = 0
pygame.mixer.music.play(loops=-1)
game_over = True
running = True
while running:
    if game_over:
        show_go_screen()
        game_over = False
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        powerups = pygame.sprite.Group()
        user = player.Player(WIDTH, HEIGHT, POWERUP_TIME)
        all_sprites.add(user)
        for i in range(8):
            newmob()
        score = 0

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()
    hits = pygame.sprite.spritecollide(user, mobs, True, pygame.sprite.collide_circle)
    for hit in hits:
        user.shield -= hit.radius * 2
        expl = explosion.Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        newmob()
        if user.shield <= 0:
            death_explosion = explosion.Explosion(user.rect.center, 'player')
            all_sprites.add(death_explosion)
            user.hide()
            user.lives -= 1
            user.shield = 100

    if user.lives == 0 and not death_explosion.alive():
        game_over = True

    hits = pygame.sprite.groupcollide(mobs, user.get_bullet(), True, True)
    for hit in hits:
        score += 50 - hit.radius
        expl = explosion.Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        hit.explode()
        if random.random() > 0.9:
            pw = pow.Pow(hit.rect.center, WIDTH, HEIGHT)
            all_sprites.add(pw)
            powerups.add(pw)
        newmob()

    hits = pygame.sprite.spritecollide(user, powerups, True)
    for hit in hits:
        if hit.type == 'shield':
            user.shield += random.randrange(10, 30)
            if user.shield >= 100:
                user.shield = 100
                shield_sound.play()
        if hit.type == 'gun':
            user.powerup()
            power_sound.play()

    # Рендеринг
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    user.get_bullet().draw(screen)
    draw_text(screen, str(score), 18, WIDTH / 2, 10)
    draw_shield_bar(screen, 5, 5, user.shield)
    draw_lives(screen, WIDTH - 100, 5, user.lives, player_mini_img)
    pygame.display.flip()

pygame.quit()
