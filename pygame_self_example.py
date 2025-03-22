"""     This is a pygame example of self. For more information about pygame, visit pygame.org or pypi.org.     """

#imports the pygame module
import pygame

#inits pygame
pygame.init()

#creates a class named Player with pygame's sprite
class Player(pygame.sprite.Sprite):
    #inits the class
    def __init__(self, x, y, image_path, new_width, new_height):
        super().__init__()
        original_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(original_image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3
        self.screen_width = width
        self.screen_height = height

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

        self.check_bounds()

    def check_bounds(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height

    def draw(self, screen):
        screen.blit(self.image, self.rect)

width, height = 1890, 980
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("\"Self\" Project")

player = Player(100, 100, "purple_sprite.png", 200, 250)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill((128, 128, 255))
    all_sprites.draw(screen)

    pygame.display.update()

pygame.quit()