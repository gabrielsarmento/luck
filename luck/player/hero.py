from pygame.image import load
from pygame.sprite import Sprite
from pygame.transform import scale

from luck.commons.constants import BLOCK_SIZE
from luck.commons.constants import GRAVITY
from luck.commons.constants import HEIGHT


class Hero(Sprite):
    def __init__(self, x: int = 0, y: int = 0) -> None:
        super().__init__()

        self.image = scale(load("luck/player/hero.png"), (40, 40))

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def update(self) -> None:
        self.fall()

    def fall(self):
        if self.rect.y < HEIGHT - BLOCK_SIZE - 40:
            self.rect.y += GRAVITY
