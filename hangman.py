import pygame
import numpy as np
import random

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
list = ["Mihir","Rohan","Nigga","Gautam","Nadya"]

def display(keyword,selected,lives):
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
    pygame.display.update()
    return correct_letters
        

def play(score):
    gameover = False
    keyword = random.choice(list).lower()
    selected = []
    lives = 10
    while True:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pressed_key = pygame.key.name(event.key)        
                if pressed_key not in selected:
                    if pressed_key not in keyword:
                        lives -= 1
                    selected.append(pressed_key)
            
            if lives == 0:
                return score
                    
        correct_letters = display(keyword,selected,lives)
        if correct_letters == len(keyword):
            pygame.time.delay(3000)
            score+=1
            return score
            break
        clock.tick(60)
        
score = 0
while True:
    score = play(score)
    print(score)
pygame.quit()
        
    