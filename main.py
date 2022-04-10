import sys
import pygame
import db_tools

TITLE = "SQLITE PYGAME"
WIDTH = 1280
HEIGHT = 768
FPS = 60


class Player(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.image = pygame.Surface((50, 50))
        self.image.fill("yellow")
        self.rect = self.image.get_rect(topleft=pos)

        # data
        self.id = "1"
        self.hp = db_tools.query_data_one(f"select HP from NPC where ID = {self.id}")
        self.mp = db_tools.query_data_one(f"select MP from NPC where ID = {self.id}")

        self.show_info()

    def show_info(self):
        print(self.hp)
        print(self.mp)


pygame.init()
pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

player = Player(all_sprites, (300, 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        screen.fill("blue")

        all_sprites.update()
        all_sprites.draw(screen)

        pygame.display.update()
        clock.tick(FPS)
