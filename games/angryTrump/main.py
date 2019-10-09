import pygame

WIN_WIDTH, WIN_HEIGHT = 500, 500
outline = 5

pygame.init()
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

pygame.display.set_caption('Angry Trump')

pygame.mixer.music.load('sound/music.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

bulletSound = pygame.mixer.Sound('sound/fire.wav')

walkRight = [
    pygame.image.load('images/right_1.png'), pygame.image.load('images/right_2.png'),
    pygame.image.load('images/right_3.png'), pygame.image.load('images/right_4.png'),
    pygame.image.load('images/right_5.png'), pygame.image.load('images/right_6.png')
]

walkLeft = [
    pygame.image.load('images/left_1.png'), pygame.image.load('images/left_2.png'),
    pygame.image.load('images/left_3.png'), pygame.image.load('images/left_4.png'),
    pygame.image.load('images/left_5.png'), pygame.image.load('images/left_6.png')
]
bg = pygame.image.load('images/bg.jpg')
playerStand = pygame.image.load('images/idle.png')

clock = pygame.time.Clock()

heroWidth, heroHeight = 60, 71
x, y = 50, WIN_HEIGHT - heroHeight - outline
speed = 5

isJump = False
jumpCount = 10

moveLeft = False
moveRight = False
animCount = 0
lastMove = 'right'

class Bullet():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def drawWindow():
    global animCount
    win.blit(bg, (0, 0))

    if animCount + 1 >= 30:
        animCount = 0

    if moveLeft:
         win.blit(walkLeft[animCount // 5], (x, y))
         animCount += 1
    elif moveRight:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount +=1
    else:
        win.blit(playerStand, (x, y))

    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()

bullets = []
run = True

while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if WIN_WIDTH > bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        if lastMove == 'right':
            facing = 1
        else:
            facing = -1

        if len(bullets) < 5:
            bullets.append(Bullet(x=round(x + heroWidth // 2), y=round(y + heroHeight // 2),
                                  radius=5, color=(255, 0, 0), facing=facing))
            bulletSound.play()

    if keys[pygame.K_LEFT] and x > outline:
        x -= speed
        moveLeft = True
        moveRight = False
        lastMove = 'left'
    elif keys[pygame.K_RIGHT] and x < WIN_WIDTH - heroWidth - outline:
        x += speed
        moveLeft = False
        moveRight = True
        lastMove = 'right'
    else:
        moveLeft = False
        moveRight = False
        animCount = 0

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    if keys[pygame.K_ESCAPE]:
        exit()

    drawWindow()

pygame.quit()