import random
import sys

import pygame

from bullet import Bullet
from enemy_tank import EnemyTank
from obstacle import Obstacle
from tank import Tank

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tanks")

WHITE = (255, 255, 255)
GREEN = (51, 102, 0)
BROWN = (240, 230, 140)
BLUE = (85, 170, 255)
BLACK = (0, 0, 0)

BACKGROUND_IMAGE = pygame.image.load('фонтрава10.png').convert()
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (800, 800))


def draw_landscape(window):
    window.blit(BACKGROUND_IMAGE, (0, 0))


def create_enemies(num_enemies, obstacles):
    enemies = []
    for _ in range(num_enemies):
        while True:
            x = random.randint(50, WIDTH - 50)
            y = random.randint(50, HEIGHT - 50)
            enemy = EnemyTank(x, y)
            if not any(enemy.rect.colliderect(obstacle.rect) for obstacle in obstacles):
                enemies.append(enemy)
                break
    return enemies


def main():
    clock = pygame.time.Clock()
    run = True

    tank = Tank(50, 50)
    bullets = []

    obstacles = [
        Obstacle(0, 0, 800, 5, BLACK),
        Obstacle(0, 0, 5, 800, BLACK),
        Obstacle(795, 0, 5, 800, BLACK),
        Obstacle(0, 795, 800, 5, BLACK),
        Obstacle(100, 100, 150, 20, BROWN),
        Obstacle(350, 100, 100, 20, BROWN),
        Obstacle(550, 100, 150, 20, BROWN),
        Obstacle(100, 100, 20, 150, BROWN),
        Obstacle(100, 350, 20, 100, BROWN),
        Obstacle(100, 550, 20, 150, BROWN),
        Obstacle(100, 680, 150, 20, BROWN),
        Obstacle(350, 680, 100, 20, BROWN),
        Obstacle(550, 680, 150, 20, BROWN),
        Obstacle(680, 100, 20, 150, BROWN),
        Obstacle(680, 350, 20, 100, BROWN),
        Obstacle(680, 550, 20, 150, BROWN),
        Obstacle(200, 200, 150, 20, BROWN),
        Obstacle(450, 200, 150, 20, BROWN),
        Obstacle(200, 200, 20, 150, BROWN),
        Obstacle(200, 450, 20, 150, BROWN),
        Obstacle(200, 580, 150, 20, BROWN),
        Obstacle(450, 580, 150, 20, BROWN),
        Obstacle(580, 200, 20, 150, BROWN),
        Obstacle(580, 450, 20, 150, BROWN),
        Obstacle(300, 300, 200, 200, BLUE)
    ]

    enemies = create_enemies(10, obstacles)

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            tank.process_key_event(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    new_bullet = Bullet(tank.rect.centerx, tank.rect.centery, tank.get_angle())
                    bullets.append(new_bullet)

        tank.move()

        if tank.check_collision(obstacles):
            if tank.direction == "up":
                tank.rect.y += tank.vel
            elif tank.direction == "down":
                tank.rect.y -= tank.vel
            elif tank.direction == "left":
                tank.rect.x += tank.vel
            elif tank.direction == "right":
                tank.rect.x -= tank.vel

        for enemy in enemies:
            enemy.move()
            if enemy.check_collision(obstacles):
                if enemy.direction == "up":
                    enemy.rect.y += enemy.vel
                elif enemy.direction == "down":
                    enemy.rect.y -= enemy.vel
                elif enemy.direction == "left":
                    enemy.rect.x += enemy.vel
                elif enemy.direction == "right":
                    enemy.rect.x -= enemy.vel

        for bullet in bullets:
            if bullet.check_collision(obstacles, enemies):
                bullets.remove(bullet)

        draw_landscape(WIN)

        bullets = [bullet for bullet in bullets if
                   bullet.rect.right > 0 and bullet.rect.left < WIDTH and bullet.rect.bottom > 0 and bullet.rect.top < HEIGHT]

        for obstacle in obstacles:
            obstacle.draw(WIN)

        for enemy in enemies:
            enemy.draw(WIN)

        tank.draw(WIN)

        for bullet in bullets:
            bullet.draw(WIN)
            bullet.move()

        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
