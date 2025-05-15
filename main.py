import pygame
from Rectangle import Rectangle

pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello Pygame")

player1 = Rectangle(
    [50, 50, 100, 50], #[x, y, width, height]
    (0,0,255),
    0,
    screen
)

enemy = Rectangle(
    [250, 50, 100, 50], #[x, y, width, height]
    (255,0,0),
    0,
    screen
)

#consider touch interaction!
#enemy touching player damages player

def collisionDetect():
    while True:
        if player1.colliderect(enemy):
            print("the player has been damaged!")
            yield

detectCollide = collisionDetect()
clock = pygame.time.Clock()


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    next(detectCollide)
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 FPS

# Quit Pygame
pygame.quit()