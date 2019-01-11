import pygame
import numpy as np
import random
import math

black = (0,0,0)
white = (255,255,255)

pygame.init()

height = 600
width = 800
size = [width,height]
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 60)
clock = pygame.time.Clock()
pygame.display.set_caption("Hangman")
list = ["auto,","else","long","switch","break","enum","register","typedef","case","extern","return","union","char","float","short","unsigned","const","for","signed","void","continue","goto","sizeof","volatile","default","if","static","while","do","int","struct","Packed","double","abstract","assert","boolean","break","byte","case","catch","char","class","const","continue","default","do","double","else","enum","extends","finally","float","for","goto","if","implements","import","instanceof","int","interface","long","native","new","package","private","protected","public","return","short","static","super","synchronized","this","throw","throws","transient","try","void","volatile","while","and","exec","not","assert","finally","or","break","for","pass","class","from","print","continue","global","raise","def","if","return","del","import","try","elif","in","while","else","is","with","except","lambda","yield"]
print(len(list))
taken = []

def game_over(score):
    screen.fill(black)
    text = font.render("Game Over!", True, white)
    screen.blit(text, (width/2-150, height/2-50))
    string = "Score : " + str(score)
    text = font.render(string, True, white)
    screen.blit(text, (width/2-100, height/2))
    pygame.display.update()
    while True:
        pygame.time.delay(1000)


def display(keyword,selected,lives, score, time):
    string = ""
    correct_letters = 0
    for i in range(0,len(keyword)):
        if keyword[i] in selected:
            string += keyword[i] + " "
            correct_letters += 1
        else:
            string += "_ "
    text = font.render(string,True,white)
    screen.blit(text,(50,height/2-50))
    num = 10 - lives
    img_sel = "ha" + str(num)
    screen.blit(pygame.image.load("./img/"+ img_sel +".png"),(300,123))
    score_print = str(score)
    text = font.render(score_print, 1, white)
    text_pos = (700, 50)
    screen.blit(text, text_pos)
    min = math.floor(time/60)
    sec = int(time%60)
    rem_time = str(min) + ":" + str(sec)
    text = font.render(rem_time, 1, white)
    text_pos = (50, 50)
    screen.blit(text, text_pos)
    pygame.display.update()
    return correct_letters
        

def play(score, start_ticks):
    keyword = random.choice(list).lower()
    while keyword in taken:
        keyword = random.choice(list).lower()
    taken.append(keyword)
    selected = []
    lives = 10
    while True:
        elapsed_time = pygame.time.get_ticks() - start_ticks
        rem_time = (10*60*1000 - elapsed_time)/1000
        screen.fill(black)
        if rem_time <= 0:
            game_over(score)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pressed_key = pygame.key.name(event.key)        
                if pressed_key not in selected:
                    if pressed_key not in keyword:
                        lives -= 1
                    selected.append(pressed_key)
            
            if lives == 0:
                return score - 1
                    
        correct_letters = display(keyword,selected,lives, score, rem_time)
        if correct_letters == len(keyword):
            pygame.time.delay(1000)
            score += 1
            return score
            break
        clock.tick(100)


score = 0
time = 0
start_ticks = pygame.time.get_ticks()
while True:
    score = play(score, start_ticks)
    print(score)
#game_over(score)
#pygame.quit()
        
    