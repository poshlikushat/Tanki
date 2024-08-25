import pygame


class Tank:
    def __init__(self, x, y):
        self.original_image = pygame.image.load('tank.png').convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.vel = 5
        self.angle = 0
        self.direction = None

    def draw(self, window):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        window.blit(rotated_image, rotated_rect)

    def move(self):
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

    def process_key_event(self, event):
        if event.type == pygame.KEYDOWN:
            if not self.direction:
                if event.key == pygame.K_UP:
                    self.direction = "up"
                elif event.key == pygame.K_DOWN:
                    self.direction = "down"
                elif event.key == pygame.K_LEFT:
                    self.direction = "left"
                elif event.key == pygame.K_RIGHT:
                    self.direction = "right"
            else:
                if event.key == pygame.K_UP:
                    self.direction = "up"
                elif event.key == pygame.K_DOWN:
                    self.direction = "down"
                elif event.key == pygame.K_LEFT:
                    self.direction = "left"
                elif event.key == pygame.K_RIGHT:
                    self.direction = "right"
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and self.direction == "up":
                self.direction = None
            elif event.key == pygame.K_DOWN and self.direction == "down":
                self.direction = None
            elif event.key == pygame.K_LEFT and self.direction == "left":
                self.direction = None
            elif event.key == pygame.K_RIGHT and self.direction == "right":
                self.direction = None

    def get_angle(self):
        return self.angle

    def check_collision(self, obstacles):
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                return True
        return False
