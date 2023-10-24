import pygame

FPS=1000
WHITE=(245,245,245)
WIDTH=1000
HEIGHT=645

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("BOOOOM!")
clock=pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.image=pygame.Surface((60,50))
      self.image.fill(0,0,245)
      self.rect=self.image.get_rect()
      self.rect.x =200
      self.rect.y =200
      
running=True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    screen.fill((WHITE))
    pygame.display.update()

# pygame git step 1 

pygame.quit()