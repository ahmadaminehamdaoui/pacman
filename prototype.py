'''
PAR HAMDAOUI AHMAD-AMINE, 1G7
'''

import pygame, sys

dimensions = (15*32, 7*32)

pygame.init()
screen = pygame.display.set_mode(dimensions)
pygame.display.set_caption("Pacman")
font = pygame.font.Font('freesansbold.ttf', 20)
clock = pygame.time.Clock()

class Player:
    def __init__(self, position, velocity, sprite):
        self.position = position
        self.velocity = velocity
        self.sprite = sprite

        self.future_velocity = 'none'
        self.sprite_size = 26
        self.rotation = 0
        self.isColliding = False
player = Player((33,33), 'none', pygame.image.load('data/pacman.png'))

map = [
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
         [1,0,1,1,1,1,1,0,1,1,1,1,1,0,1],
         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
         [1,0,1,1,1,1,1,0,1,1,1,1,1,0,1],
         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ]
tiles = []
for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x]==1:
                tiles.append([x*32,y*32])

while True:
    # Position
    if player.velocity == 'up':
        player.position = (player.position[0], player.position[1]-4)
    elif player.velocity == 'down':
        player.position = (player.position[0], player.position[1]+4)
    elif player.velocity == 'right':
        player.position = (player.position[0]+4, player.position[1])
    elif player.velocity == 'left':
        player.position = (player.position[0]-4, player.position[1])

    for tile in tiles:
        if(player.position[0] >= tile[0] and player.position[0] <= tile[0]+32 and player.position[1] >= tile[1] and player.position[1] <= tile[1]+32) or (player.position[0]+player.sprite_size >= tile[0] and player.position[0]+player.sprite_size <= tile[0]+32 and player.position[1] >= tile[1] and player.position[1] <= tile[1]+32) or (player.position[0] >= tile[0] and player.position[0] <= tile[0]+32 and player.position[1]+player.sprite_size >= tile[1] and player.position[1]+player.sprite_size <= tile[1]+32) or (player.position[0]+player.sprite_size >= tile[0] and player.position[0]+player.sprite_size <= tile[0]+32 and player.position[1]+player.sprite_size >= tile[1] and player.position[1]+player.sprite_size <= tile[1]+32):
            player.isColliding = True
    while player.isColliding:
        if player.velocity == 'up':
            player.position = (player.position[0], player.position[1]+1)
        elif player.velocity == 'down':
            player.position = (player.position[0], player.position[1]-1)
        elif player.velocity == 'right':
            player.position = (player.position[0]-1, player.position[1])
        elif player.velocity == 'left':
            player.position = (player.position[0]+1, player.position[1])

        collide_counter = 0
        for tile in tiles:
            if(player.position[0] >= tile[0] and player.position[0] <= tile[0]+32 and player.position[1] >= tile[1] and player.position[1] <= tile[1]+32) or (player.position[0]+player.sprite_size >= tile[0] and player.position[0]+player.sprite_size <= tile[0]+32 and player.position[1] >= tile[1] and player.position[1] <= tile[1]+32) or (player.position[0] >= tile[0] and player.position[0] <= tile[0]+32 and player.position[1]+player.sprite_size >= tile[1] and player.position[1]+player.sprite_size <= tile[1]+32) or (player.position[0]+player.sprite_size >= tile[0] and player.position[0]+player.sprite_size <= tile[0]+32 and player.position[1]+player.sprite_size >= tile[1] and player.position[1]+player.sprite_size <= tile[1]+32):
                collide_counter += 1
        if collide_counter == 0:
            player.isColliding = False

    # Keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_UP:    #est-ce la touche UP
                player.velocity = 'up'
                player.rotation = 90
            elif event.key == pygame.K_DOWN:    #est-ce la touche UP
                player.velocity = 'down'
                player.rotation = 270
            elif event.key == pygame.K_RIGHT:    #est-ce la touche UP
                player.velocity = 'right'
                player.rotation = 0
            elif event.key == pygame.K_LEFT:    #est-ce la touche UP
                player.velocity = 'left'
                player.rotation = 180

    # DRAWING
    screen.fill((0,0,0))

    # map
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x]==1:
                pygame.draw.rect(screen, (0,0,255), pygame.Rect(x*32, y*32, 32, 32))

    # joueur
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(player.position[0], player.position[1], player.sprite_size, player.sprite_size))
    final_sprite = pygame.transform.rotate(player.sprite, player.rotation)
    screen.blit(final_sprite, player.position)
    print(player.position)
    # RAFRAICHISSEMENT
    pygame.display.update()
    clock.tick(60)

pygame.quit()

