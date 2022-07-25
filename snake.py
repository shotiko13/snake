import random

import pygame
import time


class Food:
    def __init__(self, screen):
        self.food_img = pygame.image.load('resources/bird.png')
        self.food_img = pygame.transform.scale(self.food_img, (40, 40))
        self.x = 120
        self.y = 120
        self.screen = screen

    def make_food(self):
        self.screen.blit(self.food_img, (self.x, self.y))   
        pygame.display.flip()

    def appear(self):
        self.x = random.randint(1, 25) * 40
        self.y = random.randint(1, 15) * 40


class Snake:
    def __init__(self, screen, how_long):
        self.screen = screen
        self.block = pygame.image.load('resources/blockoo.png')
        self.block = pygame.transform.scale(self.block, (40, 40))
        self.how_long = how_long
        self.x = [40] * how_long
        self.y = [40] * how_long
        self.initial_direction = 'r'
    img = pygame.image.load('resources/soze.jpg')
    img = pygame.transform.scale(img,(1200,700))
    def make_block(self):

        self.screen.blit(self.img,(0,0))

        for i in range(self.how_long):
            self.screen.blit(self.block, (self.x[i], self.y[i]))

        pygame.display.flip()

    def move_left(self):
        if not self.initial_direction == 'r':
            self.initial_direction = 'l'

    def move_right(self):
        if not self.initial_direction == 'l':
            self.initial_direction = 'r'

    def move_up(self):
        if not self.initial_direction == 'd':
            self.initial_direction = 'u'

    def move_down(self):
        if not self.initial_direction == 'u':
            self.initial_direction = 'd'

    def jog(self):

        for i in range(self.how_long - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.initial_direction == 'l':
            self.x[0] -= 40
        if self.initial_direction == 'r':
            self.x[0] += 40
        if self.initial_direction == 'u':
            self.y[0] -= 40
        if self.initial_direction == 'd':
            self.y[0] += 40
        self.make_block()

    def eat(self):
        self.how_long += 1
        self.x.append(-1)
        self.y.append(-1)


class App:
    def __init__(self):
        self.running = False
        self.clock = None
        self.screen = pygame.display.set_mode((1200, 700))
        self.snake = Snake(self.screen, 5)
        self.snake.make_block()
        self.food = Food(self.screen)

    def has_eatten(self, x, y, a, b):
        if x == a:
            if y == b:
                return True
        return False

    def has_hit_wall(self, x, y, a, b):
        if x > a and x < a - 100:
            if y > b - 100 and y < b + 40:
                return True
        return False

    def run(self):
        self.init()
        while self.running:
            self.update()
            self.clock.tick(20)

    def init(self):

        pygame.display.set_caption("The Usual Snake")

        self.clock = pygame.time.Clock()
        self.running = True

    def update(self):
        pygame.display.update()
        self.events()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            self.snake.move_left()
        if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            self.snake.move_right()
        if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
            self.snake.move_up()
        if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
            self.snake.move_down()

        if not self.lost():
            self.snake.jog()
            self.food.make_food()
            pygame.display.flip()
        else:
            self.end_game()
            if keys_pressed[pygame.K_DOWN]:
                self.cleanUp()
                self.events()
            if keys_pressed[pygame.K_ESCAPE]:
                self.running = False

        if self.has_eatten(self.snake.x[0], self.snake.y[0], self.food.x, self.food.y):
            self.snake.eat()
            self.food.appear()

            # end_img = pygame.transform.scale(self.end_img, (1200, 700))
            # self.screen.blit(end_img, (0, 0))

    def lost(self):
        for i in range(5, self.snake.how_long):
            if self.has_eatten(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                return True
        if not (0 <= self.snake.x[0] <= 1160 and 0 <= self.snake.y[0] <= 640):
            return True
        return False

    end_img = pygame.image.load('resources/kutaisi-int-university-ready-cov.jpg')

    def end_game(self):
        self.end_img = pygame.transform.scale(self.end_img, (1200, 700))
        self.screen.blit(self.end_img, (0, 0))
        pygame.display.flip()

    def cleanUp(self):
        self.snake = Snake(self.screen, 5)
        self.food = Food(self.screen)


if __name__ == "__main__":
    app = App()
    app.run()
