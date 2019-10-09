import pygame
import games.breakout.paddle as paddle
import games.breakout.block as block

WIN_WIDTH, WIN_HEIGHT = 1280, 720
backgroundColor = [123, 126, 130]

offset = 30
paddleWidth, paddleHeight = 200, 30
paddleX = WIN_WIDTH / 2 - paddleWidth / 2
paddleY = WIN_HEIGHT - paddleHeight - offset

n = 10
blockW = WIN_WIDTH / n
blockH = blockW / 2


pygame.init()

pygame.display.set_caption('Breakout Game')
display = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
display.fill(backgroundColor)

player = paddle.Paddle(paddleX, paddleY, paddleWidth, paddleHeight)

blocks = []
m = 3
for y in range(3):
    for x in range(0, WIN_WIDTH, int(blockW)):
        blocks.append(block.Block(x + 2, blockH * (y + 1), blockW - 2, blockH - 2))

FPSClock = pygame.time.Clock()
FPS = 60
gameOver = False

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        display.fill(backgroundColor)
        mouseX = pygame.mouse.get_pos()[0]
        player.draw(display)
        player.move(mouseX)
        for b in range(len(blocks)):
            blocks[b].draw(display)

        pygame.display.flip()
        pygame.display.update()
        FPSClock.tick(FPS)

pygame.quit()