import pygame
import time
import game_objects
pygame.font.init()

WIDTH = 800
HEIGHT = 750

PLAYER_WIDTH = 28
PLAYER_HEIGHT = 26 

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake and ladder")

player1 = game_objects.PLayer(pygame.Rect(0, HEIGHT-PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT))
player2 = game_objects.PLayer(pygame.Rect(0, HEIGHT-PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT))

BG = pygame.transform.scale(pygame.image.load("bgi.jpeg"), (WIDTH, HEIGHT-100))

FONT = pygame.font.SysFont(name="comicsans",size=50)

FONT1 = pygame.font.SysFont(name="comicsans",size=20)

clock = pygame.time.Clock()

def move(player, start, end):
    if player.position == 0:
        player.rect_obj.x = game_objects.BOARD_MAP[1][0] - PLAYER_WIDTH/2
        player.rect_obj.y = game_objects.BOARD_MAP[1][0] - PLAYER_WIDTH/2

        for i in range(start, end):
            player.rect_obj.x = game_objects.BOARD_MAP[i][0] - PLAYER_WIDTH/2
            player.rect_obj.y = game_objects.BOARD_MAP[i][1] - PLAYER_HEIGHT/2

            draw(player1, player2)
            pygame.time.delay(200)
        player.position += end - start

    else:
        for i in range(start, end):
            if(i>100):
                break

            player.rect_obj.x = game_objects.BOARD_MAP[i][0] - PLAYER_WIDTH/2
            player.rect_obj.y = game_objects.BOARD_MAP[i][1] - PLAYER_HEIGHT/2

            draw(player1, player2)
            pygame.time.delay(200)
        player.position += end - start

def play(player, num):
    
    move(player, player.position + 1, player.position + num + 1)

    if(game_objects.check_ladder(player.position)):
        a = game_objects.LADDERS[player.position].end
        player.change_pos(a)
        player.rect_obj.x = game_objects.BOARD_MAP[a][0] - PLAYER_WIDTH/2
        player.rect_obj.y = game_objects.BOARD_MAP[a][1] - PLAYER_HEIGHT/2
        draw(player1, player2)
        pygame.time.delay(200)

    if(game_objects.check_snake(player.position)):
        print("1")
        a = game_objects.SNAKES[player.position].end
        player.change_pos(a)
        player.rect_obj.x = game_objects.BOARD_MAP[a][0] - PLAYER_WIDTH/2
        player.rect_obj.y = game_objects.BOARD_MAP[a][1] - PLAYER_HEIGHT/2
        draw(player1, player2)
        pygame.time.delay(200)

def draw(player1, player2):
    WIN.blit(BG, (0,100))

    pygame.draw.rect(WIN, "yellow", player1.rect_obj)
    pygame.draw.rect(WIN, "blue", player2.rect_obj)

    pygame.display.update()

def main():
    run = True
    i = 0
    while run:
        WIN.fill(pygame.Color("black"))
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()

        draw(player1, player2)

        player1text = FONT.render("Player 1", 1, "Yellow")
        player2text = FONT.render("player 2", 1, "blue")
        playtext = FONT1.render("Play", 1, "white")
        win1text = FONT.render("Player 1", 1, "white")
        win2text = FONT.render("Player 2", 1, "white")
        
        WIN.blit(player1text, (10, 10))
        WIN.blit(player2text, (WIDTH-10-player2text.get_width(), 10))
        if(i%2==0):
            WIN.blit(playtext, (55, 75))
        else:
            WIN.blit(playtext, (700, 75))
        pygame.display.update()

        if(i%2 == 0):
            if(keys[pygame.K_r]):
                num = game_objects.roll_dice()

                Diceroll = FONT.render(f"{num}", 1, "white")
                WIN.blit(Diceroll, (WIDTH/2-Diceroll.get_width()/2, 10))
                pygame.display.update()
                
                play(player1, num) 

                if(player1.position >= 100):
                    WIN.fill(pygame.Color("black"))
                    WIN.blit(win1text, (WIDTH/2-win1text.get_width()/2, 10))
                    pygame.display.update()
                    pygame.time.delay(4000)
                    break
                i += 1
                continue
        
        else:
            if(keys[pygame.K_r] and i%2 != 0):
                num = game_objects.roll_dice()

                Diceroll = FONT.render(f"{num}", 1, "white")
                WIN.blit(Diceroll, (WIDTH/2-Diceroll.get_width()/2, 10))
                pygame.display.update()

                play(player2, num)

                if(player2.position >= 100):
                    WIN.fill(pygame.Color("black"))
                    WIN.blit(win2text, (WIDTH/2-win1text.get_width()/2, 10))
                    pygame.display.update()
                    pygame.time.delay(4000)
                    break
                i += 1
                continue
        
        


    pygame.display.quit()

if __name__ == "__main__":
    main()