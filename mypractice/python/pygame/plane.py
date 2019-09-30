# -*- coding: utf-8 -*-
import pygame
import random
import sys

class Bullet:
    def __init__(self):
        self.x = 0
        self.y = -1
        self.image = pygame.image.load('bullet.png').convert_alpha()
        self.active = False

    def move(self):
        if self.active:
            self.y -= 3
        if self.y < 0:
            self.active = False

    def restart(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        self.x = mouseX - self.image.get_width() / 2
        self.y = mouseY - self.image.get_height() / 2
        self.active = True 

class Plane:
    def __init__(self):
        self.x = 200
        self.y = 600
        self.image = pygame.image.load('plane.png').convert_alpha()        

    def move(self):
        plane_x = self.image.get_width() / 2
        plane_y = self.image.get_height() / 2
        return plane_x, plane_y

    def restart(self):
        self.x = 200
        self.y = 600

class Enemy:
    def __init__(self):
        self.x = 200
        self.y = -50
        self.image = pygame.image.load('enemy.png').convert_alpha()
        self.speed = random.random() + 0.1

    def move(self):
        if self.y < 800:
            self.y += self.speed
        else:
            self.restart()

    def restart(self):
        self.x = random.randint(50, 400)
        self.y = -50 

def checkhit(bullet, enemy):
    if (bullet.x > enemy.x and bullet.x < enemy.x + enemy.image.get_width()) and (bullet.y > enemy.y and bullet.y < enemy.y + enemy.image.get_height()):
            enemy.restart() 
            bullet.active = False
            return True
    return False

def checkcrash(plane, enemy):
    if (plane.x + plane.image.get_width() > enemy.x) and (plane.x + plane.image.get_width() < enemy.x + enemy.image.get_width()) and (plane.y + plane.image.get_height() > enemy.y) and (plane.y + plane.image.get_height() < enemy.y + enemy.image.get_height()):
        return True
    return False

pygame.init()
screen = pygame.display.set_mode((450, 800), 0, 32)
pygame.display.set_caption("Hello, World!")
background = pygame.image.load('back.jpg').convert()
font = pygame.font.Font(None, 32)
bullets = []
for i in range(5):
    bullets.append(Bullet())
bullets_count = len(bullets)
index_b = 0
interval_b = 0
plane = Plane()
enemies = [Enemy() for i in range(5)]
gameover = False
score = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if gameover and event.type == pygame.MOUSEBUTTONUP:
            plane.restart()
            for e in enemies:
                e.restart()
            for b in bullets:
                b.active = False
            score = 0
            gameover = False
    if not gameover:
        x, y = pygame.mouse.get_pos()
        screen.blit(background, (0,0))
        interval_b -= 1
        if interval_b < 0:
            bullets[index_b].restart()
            interval_b = 100
            index_b = (index_b + 1) % bullets_count 
        for b in bullets:
            if b.active:
                for es in enemies:
                    if checkhit(b, es):
                        score += 1
                b.move()
                screen.blit(b.image, (b.x, b.y))
        for e in enemies:
            if checkcrash(plane, e):
                gameover = True
            e.move()
            screen.blit(e.image, (e.x, e.y))
        p_x, p_y = plane.move()    
        x-= p_x / 2
        y-= p_y / 2
        screen.blit(plane.image, (x, y))
        text = font.render("Socre: %d" % score, 1, (0, 0, 0))
        screen.blit(text, (0, 0))
    else:
        text = font.render("Socre: %d" % score, 1, (0, 0, 0))
        screen.blit(text, (300, 400))
    pygame.display.update()


