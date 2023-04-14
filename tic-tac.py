import pygame
import random
height = 300
width = 300
blue = (66, 135, 245)
pink = (255, 3, 255)
black = (8, 5, 10)
grey = (66, 59, 71)
yellow = (255, 255, 0)
fps = 30
speed = 15
x = 80
y = 80
field = [["", "", ""], ["", "", ""], ["", "", ""]]
gameover = False
pygame.init()
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("крестики нолики")
run = True
clock = pygame.time.Clock()
def grid():
    pygame.draw.line(screen, pink, (100, 0), (100,300), 3)
    pygame.draw.line(screen, pink, (200, 0), (200, 300), 3)
    pygame.draw.line(screen, pink, (0, 100), (300, 100), 3)
    pygame.draw.line(screen, pink, (0, 200), (300, 200), 3)
def tic_tac():
    for i in range(3):
        for j in range(3):
            if field[i][j] == "0":
                pygame.draw.circle(screen, blue, (j *100+50, i *100+50),45, 3)
            elif field[i][j] == "x":
                pygame.draw.line(screen, yellow, (j*100+5, i*100+5), (j*100+95, i*100+95), 3)
                pygame.draw.line(screen,yellow, (j*100+95, i *100+5), (j*100+5, i*100+95), 3)
def win_check(symbol):
    flag_win = False
    global win
    for line in field:
        if line.count(symbol)==3:
            flag_win = True
            win = [[0, field.index(line)], [1, field.index(line)], [2, field.index(line)]]
    for i in range(3):
        if field[0][i]== field[1][i] == field [2][i] == symbol:
            flag_win= True
            win = [[i, 0], [i, 1], [i,2]]
    if field[0][0]==field[1][1] == field[2][2] == symbol:
        flag_win = True
        win = [[0, 0], [1, 1], [2,2]]
    if field[2][0]==field[1][1] == field[0][2] == symbol:
        flag_win = True
        win = [[0, 2], [1, 1], [2,0]]
    return flag_win
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if field[pos[1]// 100][pos[0]//100]=="":
                field[pos[1]// 100][pos[0]//100]="x"
                x, y = random.randint(0, 2), random.randint(0,2)
                while field[x][y] != "":
                    x, y = random.randint(0, 2), random.randint(0,2)
                field[x][y]="0"
            player_win = win_check("x")
            comp_win = win_check("0")
            result = field[0].count("x")+field[0].count("0")+field[1].count("x")+field[1].count("0")+field[2].count("x")+field[2].count("0")
            if player_win or comp_win:
                gameover = True
                if player_win:
                    pygame.display.set_caption("вы выиграли")
                elif comp_win:
                    pygame.display.set_caption("вы проигали")
            if result == 8:
                pygame.display.set_caption("ничья")


    screen.fill(black)
    if gameover:
        pygame.draw.rect(screen, grey, (win[0][0]*100, win[0][1]*100, 100, 100))
        pygame.draw.rect(screen, grey, (win[1][0]*100, win[1][1]*100, 100, 100))
        pygame.draw.rect(screen, grey, (win[2][0]*100, win[2][1]*100, 100, 100))
    tic_tac()
    grid()
    pygame.display.flip()
pygame.quit()