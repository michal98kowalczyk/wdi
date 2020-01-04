#projekt wdi

import pygame, sys, math,random
import os
from os.path import join
from pygame.locals import *
from time import localtime



pygame.init() 
pygame.display.set_caption("Snake by Michal Kowalczyk") 
pygame.font.init() 
random.seed()


SNAKE_SIZE = 9
SNAKE_SPEED = 0.36
APPLE_SIZE=9

SEPARATION=10 
HIGHSCORE = 0
#Screen_Size
HEIGHT = 600
WIDTH = 800

FPS = 25
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

KEY = {"UP":1 , "DOWN":2, "LEFT":3, "RIGHT":4}

screen = pygame.display.set_mode((WIDTH,HEIGHT),pygame.FULLSCREEN)

score_font = pygame.font.Font(None,30)
score_numb_font = pygame.font.Font(None,30)
game_over_font = pygame.font.Font(None,60)
play_again_font = pygame.font.Font(None,40)

score_msg = score_font.render("SCORE:",1,pygame.Color("gold"))
score_msg_size = score_font.size("SCORE")

background = pygame.Color(30,30,30)

clock = pygame.time.Clock()

class apple: 
    def __init__(self,x,y,estate):
        self.x=x
        self.y=y
        self.estate = estate
        self.color = pygame.color.Color("red")

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,APPLE_SIZE,APPLE_SIZE),0)

def eat_apple(position_snake,size_snake,position_apple,size_apple):
    if(position_snake.x < position_apple.x + size_apple and position_snake.x + size_snake > position_apple.x and position_snake.y < position_apple.y +size_apple and position_snake.y + size_snake > position_apple.y) :
        return True
    return False
    

def walls(pos):
    if(pos.x>=WIDTH):
        pos.x = SNAKE_SIZE
    if(pos.x <= 0):
        pos.x = WIDTH - SNAKE_SIZE
    if(pos.y >= HEIGHT):
        pos.y = SNAKE_SIZE
    if(pos.y <= 0):
        pos.y = HEIGHT  - SNAKE_SIZE
    


class segment:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.direction = KEY["UP"]
        self.color = "white"
    
class Snake:
    def __init__(self,x,y):
        self.x = x 
        self.y = y
        self.direction = KEY["UP"]
        self.stack=[]

        self.stack.append(self)

        box = segment(self.x,self.y+SEPARATION)
        box.direction = KEY["UP"]
        box.color = "NULL"
        self.stack.append(box)

    def moving(self):
        tail = len(self.stack)-1 #ogon 
        while(tail != 0):
            self.stack[tail].direction = self.stack[tail-1].direction
            self.stack[tail].x = self.stack[tail-1].x
            self.stack[tail].y = self.stack[tail-1].y

            tail -= 1
        if(len(self.stack)<2):
            last_segment = self   
        else:
            last_segment = self.stack.pop(tail)
        last_segment.direction = self.stack[0].direction

        if(self.stack[0].direction == KEY["UP"]):
            last_segment.y = self.stack[0].y - (FPS * SNAKE_SPEED)
        elif(self.stack[0].direction == KEY["DOWN"]):
            last_segment.y = self.stack[0].y + (FPS * SNAKE_SPEED)
        elif(self.stack[0].direction == KEY["RIGHT"]):
            last_segment.x = self.stack[0].x + (FPS * SNAKE_SPEED)
        elif(self.stack[0].direction == KEY["LEFT"]):
            last_segment.x = self.stack[0].x - (FPS * SNAKE_SPEED)
        
        
        
        self.stack.insert(0,last_segment)

    def head(self):
        return (self.stack[0])

    def grow(self):
        tail = len(self.stack)-1
        self.stack[tail].direction = self.stack[tail].direction

        if(self.stack[tail].direction==KEY["UP"]):
            new_element = segment(self.stack[tail].x,self.stack[tail].y-SNAKE_SIZE)
            box = segment(new_element.x,new_element.y - SEPARATION)
        elif(self.stack[tail].direction==KEY["DOWN"]):
            new_element = segment(self.stack[tail].x,self.stack[tail].y+SNAKE_SIZE)
            box = segment(new_element.x,new_element.y + SEPARATION)      
        elif(self.stack[tail].direction==KEY["RIGHT"]):
            new_element = segment(self.stack[tail].x + SNAKE_SIZE,self.stack[tail].y)
            box = segment(new_element.x + SEPARATION ,new_element.y) 
        elif(self.stack[tail].direction==KEY["LEFT"]):
            new_element = segment(self.stack[tail].x - SNAKE_SIZE,self.stack[tail].y)
            box = segment(new_element.x - SEPARATION ,new_element.y) 

        box.color = "NULL"

        self.stack.append(new_element)
        self.stack.append(box)

    def set_direction(self,direction):
        if(self.direction == KEY["RIGHT"] and direction == KEY["LEFT"] or self.direction == KEY["LEFT"] and direction == KEY["RIGHT"] ):
            pass
        elif(self.direction == KEY["UP"] and direction == KEY["DOWN"] or self.direction == KEY["DOWN"] and direction == KEY["UP"] ):
            pass
        else:
            self.direction = direction

    def crash(self):
        tmp = 1
        while(tmp < len(self.stack)-1):
            if(eat_apple(self.stack[0],SNAKE_SIZE,self.stack[tmp],SNAKE_SIZE) and self.stack[tmp].color != "NULL"):
                return True
            tmp += 1
        return False

    def draw(self,screen):
        pygame.draw.rect(screen,pygame.color.Color("green"),(self.stack[0].x, self.stack[0].y,SNAKE_SIZE,SNAKE_SIZE),0)
        tmp = 1
        while(tmp < len(self.stack)):
            if(self.stack[tmp].color == "NULL" ):
                tmp += 1
                continue
            pygame.draw.rect(screen, pygame.color.Color("grey"),(self.stack[tmp].x,self.stack[tmp].y,SNAKE_SIZE,SNAKE_SIZE))
            tmp += 1

def getButton():
    for event in pygame.event.get():
        if( event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_UP):
                return KEY["UP"]
            elif(event.key == pygame.K_DOWN):
                return KEY["DOWN"]
            elif(event.key == pygame.K_LEFT):
                return KEY["LEFT"]
            elif(event.key == pygame.K_RIGHT):
                return KEY["RIGHT"]
            elif(event.key == pygame.K_ESCAPE):
                return "exit"
            elif(event.key == pygame.K_y):
                return "yes"
            elif(event.key == pygame.K_n):
                return "no"
            elif(event.key == pygame.K_F1):
                return "+"
            elif(event.key == pygame.K_F2):
                return "-"
            elif(event.key == pygame.K_RETURN or event.key==pygame.K_KP_ENTER):
                return game()
        if(event.type == pygame.QUIT):
            sys.exit()

def regenerateApple(apples,index,posX,posY):
    rad = math.sqrt((WIDTH/2*WIDTH/2 + HEIGHT/2*HEIGHT/2))/2
    corner = 999

    while(corner>rad):
        corner  = random.uniform(0,800)*math.pi*2
        x = WIDTH/2 + rad*math.cos(corner)
        y = HEIGHT/2 + rad*math.sin(corner)

        if(x == posX and y == posY):
            continue
    new_apple = apple(x,y,1)
    apples[index] = new_apple

def regenerateApples(apples,amount,posX,posY):
    tmp = 0
    del apples[:]
    rad = math.sqrt((WIDTH/2*WIDTH/2 + HEIGHT/2*HEIGHT/2))/2
    corner = 999

    while(tmp< amount):
        while(corner>rad):
            corner = random.uniform(0,800)*math.pi*2 
            x = WIDTH/2 + rad*math.cos(corner)
            y = HEIGHT/2 + rad*math.sin(corner)

            if((x - APPLE_SIZE == posX or x + APPLE_SIZE == posX) and (y-APPLE_SIZE==posY or y+APPLE_SIZE==posY) or rad-corner <=10):
                continue
            
        apples.append(apple(x,y,1))
        corner=999
        tmp +=1

def terminate():
    sound_terminate()
    writing = game_over_font.render("GAME OVER",1,pygame.Color("red"))
    writing_restart = play_again_font.render("PLAY AGAIN? Y/N",1,pygame.Color("red"))
    screen.blit(writing,(320,240))
    screen.blit(writing_restart,(320+12,240+40))

    pygame.display.flip()
    pygame.display.update()

    button = getButton()
    write_highscore()
    while(button != "exit"):
        if(button == "yes"):
                
                game()
        elif(button=="no"):
            menu()
        button=getButton()
        clock.tick(FPS)

    #sys.exit()    

def scores(score):
    global HIGHSCORE
    if(score>HIGHSCORE):
        HIGHSCORE=score

    score_numb = score_numb_font.render(str(score),1,pygame.Color("gold"))
    screen.blit(score_msg,(WIDTH-score_msg_size[0]-60,10))
    screen.blit(score_numb,(WIDTH-45,14))

def counterTime(game_time):
    t1 = score_font.render("TIME:",1,pygame.Color("purple"))
    t2 = score_numb_font.render(str(game_time/1000),1,pygame.Color("purple"))

    screen.blit(t1,(30,10))
    screen.blit(t2,(105,14))

def music_play():
    try:
        musics = os.listdir('musics')
        music = random.choice(musics)
        pygame.mixer.music.load(join('musics', music))
        pygame.mixer.music.play(0, 0.0)
    except pygame.error:
        print('Pygame Error in read the sound: %s' % (music))
        return music_play()


def write_highscore():
    with open('highscore.txt', '+r') as results:
        t = localtime()
        day, month, year = t.tm_mday, t.tm_mon, t.tm_year
        hour, minute, second = t.tm_hour, t.tm_min, t.tm_sec
        time = " | %s:%s:%s %s/%s/%s" \
               % (hour, minute, second, day, month, year)

        data = results.read()
        before_data = data
        data = data.split('\n')
        scores = []

        for line in data:
            for score in line.split('|'):
                score = score.strip()
                if score.isdigit():
                    score = int(score)
                    scores.append(score)

        print("HIGHSCORES:")
        print(before_data, end='')
        write = True
        if len(scores) > 0:
            if HIGHSCORE > max(scores):
                write = True
            else:
                write = False
        if write:
            string = "%4d %s\n" % (HIGHSCORE, time)
            results.write(string)
            print("New HIGHSCORE! %d" % HIGHSCORE)

def sound_score():
    sound = pygame.mixer.Sound('pickup.wav')
    sound.play()

def sound_terminate():
    sound = pygame.mixer.Sound('sarcastic.wav')
    sound.play()




def menu():
    size=HEIGHT//15
    line=HEIGHT//15
    screen.fill(background)
    messages = ['ENTER: START', 'ESC: QUIT']
    # TitleGame
    title = pygame.font.Font('freesansbold.ttf', size+2)
    title_surf = title.render("SnakeGame", True, WHITE)
    title_rect = title_surf.get_rect()
    title_rect.midright = (WIDTH//2, size)
    screen.blit(title_surf, title_rect)

    y = HEIGHT // 2
    for mess in messages:
        message = pygame.font.Font('freesansbold.ttf', size)
        message_surf = message.render(mess, True, WHITE)
        message_rect = message_surf.get_rect()
        message_rect.midleft = (int(WIDTH * 1/5), y)
        screen.blit(message_surf, message_rect)
        y += line

    
    while True:
        
        button = getButton()
        if(button=="exit"):
            pygame.quit()
            exit()


        pygame.display.update()
        




def game():
    global SNAKE_SPEED, HIGHSCORE
    score = 0

    music_play()
    #making a snake
    new_snake = Snake(WIDTH/2,HEIGHT/2)
    new_snake.set_direction(KEY["UP"])
    new_snake.moving()
    first_segment = 3
    while(first_segment > 0):
        new_snake.grow()
        new_snake.moving()
        first_segment -=1

    
    maximum_apple = 1
    eating_apple = False
    apples = [apple(random.randint(60,WIDTH),random.randint(60,HEIGHT),1)]
    regenerateApples(apples,maximum_apple,new_snake.x,new_snake.y)

    timezero = pygame.time.get_ticks()
    end = 1
    
    
    while(end!=0):
        clock.tick(FPS)
        

        button = getButton()
        if(button=="exit"):
            
            terminate()
            end = 0
       
        if(button=="+"):
            if(SNAKE_SPEED<0.5):
                SNAKE_SPEED+=0.01
        if(button=="-"):
            if(SNAKE_SPEED>0.36):
                SNAKE_SPEED -=0.01
        
        
        #collision with walls
        walls(new_snake)
        #self killer
        if(new_snake.crash()==True):
            terminate()
        
        for app in apples:
            if(app.estate == 1):
                if(eat_apple(new_snake.head(),SNAKE_SIZE,app,APPLE_SIZE)==True):
                    sound_score()
                    new_snake.grow()
                    app.estate = 0
                    score += 1
                    eating_apple = True

        #update place
        if(button):
            new_snake.set_direction(button)
        new_snake.moving()

        if(eating_apple==True):
            eating_apple=False
            regenerateApple(apples,0,new_snake.head().x,new_snake.head().y)

        screen.fill(background)
        for app in apples:
            if(app.estate==1):
                app.draw(screen)

        new_snake.draw(screen)
        scores(score)
        game_time = pygame.time.get_ticks() - timezero

        counterTime(game_time)
        if not pygame.mixer.music.get_busy():
            music_play()
        
        pygame.display.flip()
        pygame.display.update()



if __name__=='__main__':
    menu()






            

        
