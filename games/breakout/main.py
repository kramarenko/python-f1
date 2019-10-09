import pygame
import paddle

WIN_WIDTH, WIN_HEIGHT = 1280, 720
backgroundColor = [123, 126, 130]

offset = 30
paddleWidth, paddleHeight = 200, 50
paddleX = WIN_WIDTH / 2 - paddleWidth / 2
paddleY = WIN_HEIGHT - paddleHeight - offset

pygame.init()

pygame.display.set_caption('Breakout Game')
display = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
display.fill(backgroundColor)

player = paddle.Paddle

gameOver = False

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

        mouseX = pygame.mouse.get_pos()[0]
        print(mouseX)
        pygame.display.flip()
        pygame.display.update()

pygame.quit()