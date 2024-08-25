import random

import pygame


class EnemyTank:
    def __init__(self, x, y):
        self.direction = None
        self.original_image = pygame.image.load('Enemy_tank.png').convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.vel = 3
        self.angle = 0
        self.target = None
        self.change_interval = 500
        self.last_change_time = pygame.time.get_ticks()

    def draw(self, window):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        window.blit(rotated_image, rotated_rect)

    def move(self):
        directions = ["up", "down", "left", "right"]
        current_time = pygame.time.get_ticks()

        if current_time - self.last_change_time > self.change_interval:
            self.direction = random.choice(directions)
            self.last_change_time = current_time  # Обновляем время последнего изменения

        if self.direction == "up":
            self.rect.y -= self.vel
            self.angle = 90
        elif self.direction == "down":
            self.rect.y += self.vel
            self.angle = 270
        elif self.direction == "left":
            self.rect.x -= self.vel
            self.angle = 180
        elif self.direction == "right":
            self.rect.x += self.vel
            self.angle = 0

    def check_collision(self, obstacles):
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                return True
        return False
