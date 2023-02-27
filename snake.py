import pygame


if __name__ == "__main__":
    pygame.init()
    dis = pygame.display.set_mode((800,600))
    pygame.display.update()
    pygame.display.set_caption("GAME BY GLORIA")
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                game_over = True
        
    
    pygame.quit()
    quit()

