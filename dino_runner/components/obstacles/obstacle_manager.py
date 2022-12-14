import pygame

from dino_runner.utils.constants import SMALL_CACTUS, BIRD, LARGE_CACTUS
from dino_runner.components.obstacles.cactus import SmallCactus, LargeCactus
from dino_runner.components.obstacles.bird import Bird


class OsbtacleManager:
  def __init__(self):
    self.obstacles = []

  def update(self, game):
    if len(self.obstacles) == 0:
      cactus = SmallCactus(SMALL_CACTUS)
      cactus = LargeCactus(LARGE_CACTUS)
      self.obstacles.append(cactus)
      bird = Bird(BIRD)
      self.obstacles.append(bird)

    for obstacle in self.obstacles:
      obstacle.update(game.game_speed, self.obstacles)
      if game.player.dino_rect.colliderect(obstacle.rect):
        pygame.time.delay(1000)
        game.playing = False
        break

  def draw(self, screen):
    for obstacle in self.obstacles:
      obstacle.draw(screen)