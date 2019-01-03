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
font = pygame.font.Font(None, 100)
clock = pygame.time.Clock()

pygame.display.set_caption("Hangman")
list = ["Mihir","Rohan","Nigga","Gautam","Nadya"]

def display(keyword,selected):
    string = ""
    for i in range(0,len(keyword)):
        if keyword[i] in selected:
            string += keyword[i] + " "
        else:
            string += "_ "
    text = font.render(string,True,white)
    screen.blit(text,(50,height/2-50))
    pygame.display.update()
        

def play():
    gameover = False
    keyword = random.choice(list).lower()
    selected = []
    while not gameover:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
        if event.type == pygame.KEYDOWN:
            pressed_key = pygame.key.name(event.key)        
            if pressed_key not in selected:
                selected.append(pressed_key)
        
        display(keyword,selected)
        clock.tick(60)
        
        
play()
pygame.quit()
        
    