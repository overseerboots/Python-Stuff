import pygame

def main():
    spritesize = 32
    mapwidth = 30
    mapheight = 30
    fps = 10

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_caption("Map")

    #Load the sprites
    grass = pygame.image.load("pygame/map_generator/assets/grass.png")
    water = pygame.image.load("pygame/map_generator/assets/water.png")
    cave = pygame.image.load("pygame/map_generator/assets/cave.png")
    sand = pygame.image.load("pygame/map_generator/assets/sand.png")
    dirt = pygame.image.load("pygame/map_generator/assets/dirt.png")
    tree = pygame.image.load("pygame/map_generator/assets/tree.png")

    #load map
    map = []
    with open("pygame/map_generator/map.txt","r") as f:
        data = f.readlines()

        for row in data:
            row_data = []
            for col in row:
                row_data.append(col)
            map.append(row_data)

    player_x = 0
    player_y = 0
    screen_size = 10

    screen = pygame.display.set_mode((screen_size*spritesize,screen_size*spritesize))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check arrow keys
            if event.type == pygame.KEYDOWN:
                # Right
                if event.key == pygame.K_RIGHT:
                    if player_x < mapwidth - screen_size:
                        player_x = player_x + 1
                # Left
                if event.key == pygame.K_LEFT:
                    if player_x > 0:
                        player_x = player_x - 1
                # Up
                if event.key == pygame.K_UP:
                    if player_y > 0:
                        player_y = player_y - 1
                # Down
                if event.key == pygame.K_DOWN:
                    if player_y < mapheight - screen_size:
                        player_y = player_y + 1

        
        # DRAWING ---------------------------
        for y in range(player_y,player_y + screen_size):
            for x in range(player_x, player_x + screen_size):
                if map[y][x + player_x] == "0":
                    screen.blit(dirt,(x* spritesize, y* spritesize))
                if map[y][x + player_x] == "1":
                    screen.blit(water,(x* spritesize, y* spritesize))
                if map[y][x + player_x] == "2":
                    screen.blit(sand, (x* spritesize, y* spritesize))
                if map[y][x + player_x] == "3":
                    screen.blit(grass, (x* spritesize, y* spritesize))
                if map[y][x + player_x] == "4":
                    screen.blit(tree, (x* spritesize, y* spritesize))
                if map[y][x + player_x] == "5":
                    screen.blit(cave, (x* spritesize, y* spritesize))

        pygame.display.flip()
    clock.tick(fps)
main()