from libs.Snake import *
from libs.Food import *
import pygame


if __name__ == '__main__':
    pygame.init()
    size = (640, 320)
    loop = True
    game = 'Playing'

    display = pygame.display.set_mode(size)
    time = pygame.time.Clock()

    snake = Snake(display=display, size_x=20, size_y=20)
    snake.spawn()
    food = Food(display=display, pos_x=100, pos_y=100, size_x=20, size_y=20)

    while loop:

        if game == 'Playing':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F11:
                        display.toggle_fullscreen()

                    elif event.key == pygame.K_LEFT:
                        if snake.direction != DirectionSnake.RIGHT:
                            snake.set_direction(DirectionSnake.LEFT)
                    elif event.key == pygame.K_RIGHT:
                        if snake.direction != DirectionSnake.LEFT:
                            snake.set_direction(DirectionSnake.RIGHT)
                    elif event.key == pygame.K_UP:
                        if snake.direction != DirectionSnake.DOWN:
                            snake.set_direction(DirectionSnake.UP)
                    elif event.key == pygame.K_DOWN:
                        if snake.direction != DirectionSnake.UP:
                            snake.set_direction(DirectionSnake.DOWN)

            snake.update()
            snake.render()

            food.render()

            font = pygame.font.Font(None, 20)
            scoretext = font.render("SCORE: " + str(len(snake.length)), 1, (255, 255, 255))
            display.blit(scoretext, (0, 0))

            if snake.pos_y < 0 or snake.pos_y + snake.size_y > size[1] or snake.pos_x < 0 or snake.pos_x + snake.size_x > size[0]:
                game = 'Game over'

            if (snake.pos_x == food.pos_x and snake.pos_y == food.pos_y) or (snake.pos_x + snake.size_x == food.pos_x + food.size_x and snake.pos_y + snake.size_y == food.pos_y + food.size_y):
                snake.eat()
                food.update()

        elif game == 'Game over':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game = 'Playing'

            font = pygame.font.Font(None, 30)
            scoretext = font.render("GAME OVER", 1, (255, 255, 255))
            display.blit(scoretext, (540 / 2, 320 / 2))
            snake.spawn()

        pygame.display.update()
        display.fill((0, 0, 0))
        time.tick(10)

