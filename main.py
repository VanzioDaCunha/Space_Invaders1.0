"""
Created by Skydiver_xv
Last modified 23/11/2021
"""
import turtle
import time
import random
import winsound
import pygame

# turtle declaration
turtle.register_shape("spaceship3.gif")
turtle.register_shape("spaceship3left.gif")
turtle.register_shape("spaceship3right.gif")
turtle.register_shape("spaceship3back.gif")
turtle.register_shape("spaceship3crash.gif")
turtle.register_shape("enemy1.gif")
turtle.register_shape("laser_beam.gif")
turtle.register_shape("background1.gif")
turtle.register_shape("enemy2.gif")
turtle.register_shape("enemy3.gif")
turtle.register_shape("temp2.gif")
turtle.register_shape("Heart.gif")
turtle.delay(0)
turtle.tracer(0, 0)
window = turtle.Screen()
window.title("Invaders of Space")
window.setup(width=1000, height=700)
window.bgcolor("black")
window.tracer()

# using pygame for multi channel music
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
pygame.mixer.set_num_channels(2)

temp = turtle.Turtle()
temp.penup()
temp.speed(0)
temp.shape("temp2.gif")
time.sleep(1)
temp.hideturtle()
temp.clear()

back = turtle.Turtle()
back.penup()
back.speed(0)
back.shape("background1.gif")
back.goto(0, 1800)

ship = turtle.Turtle()
ship.speed(0)
ship.shape("spaceship3.gif")
ship.penup()
ship.goto(0, -200)
ship.direction = "stop"
ship.shoot = 5
ship.score = 0

# hearts
hrt1 = turtle.Turtle()
hrt1.penup()
hrt1.speed(0)
hrt1.shape("Heart.gif")
hrt1.goto(200, 300)
hrt2 = turtle.Turtle()
hrt2.penup()
hrt2.speed(0)
hrt2.shape("Heart.gif")
hrt2.goto(230, 300)
hrt3 = turtle.Turtle()
hrt3.penup()
hrt3.speed(0)
hrt3.shape("Heart.gif")
hrt3.goto(260, 300)

aliens_list = []
bullet_list = []

# game constants
spawn = 10
lives = 3


def go_left():
    ship.direction = "left"
    ship.shape("spaceship3right.gif")


def go_right():
    ship.direction = "right"
    ship.shape("spaceship3left.gif")


def go_up():
    ship.direction = "up"
    ship.shape("spaceship3.gif")


def go_down():
    ship.direction = "down"
    ship.shape("spaceship3back.gif")


def move():
    if ship.direction == "up":
        y2 = ship.ycor()
        ship.sety(y2+1.2)
    if ship.direction == "down":
        y2 = ship.ycor()
        ship.sety(y2-1.2)
    if ship.direction == "left":
        x2 = ship.xcor()
        ship.setx(x2-1.2)
    if ship.direction == "right":
        x2 = ship.xcor()
        ship.setx(x2+1.2)


def shoot():
    if ship.shoot >= 15:
        ship.shoot = 0
        x3 = ship.xcor()
        y3 = ship.ycor()
        bul = turtle.Turtle()
        bul.penup()
        bul.speed(0)
        bul.goto(x3, y3 + 10)
        bul.shape("laser_beam.gif")
        bullet_list.append(bul)
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('lasers.wav'))


def collision(liv):
    i = 0
    x1 = ship.xcor()
    y1 = ship.ycor()
    if x1 > 390:
        ship.setx(-380)
    if x1 < -390:
        ship.setx(380)
    if y1 > 300 or y1 < -300:
        liv -= 1
    for aliens in aliens_list:

        if ship.distance(aliens) < 40 or aliens.ycor() < -290:
            aliens.goto(1000, 1000)
            aliens.hideturtle()
            aliens.clear()
            aliens_list.pop(i)
            liv -= 1
        j = 0
        for bullet in bullet_list:
            if bullet.distance(aliens) < 20:
                aliens.goto(1000, 1000)
                aliens.hideturtle()
                aliens.clear()
                aliens_list.pop(i)
                bullet.goto(1000, 1000)
                bullet.hideturtle()
                bullet.clear()
                bullet_list.pop(j)
                ship.score += 100
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('explosions.wav'))

            elif bullet.ycor() > 290:
                bullet.goto(1000, 1000)
                bullet.hideturtle()
                bullet.clear()
                bullet_list.pop(j)
            j += 1
        i += 1

    return liv


def level1(siv):
    if siv >= 120:
        siv = 0
        a = random.randint(-280, 280)
        nw = turtle.Turtle()
        nw.penup()
        nw.speed(0)
        nw.goto(a, 290)
        nw.shape("enemy1.gif")
        nw.level = 1
        aliens_list.append(nw)
    return siv


def level2(siv):
    if siv >= 110:
        siv = 0
        a = random.randint(-280, 280)
        nw = turtle.Turtle()
        nw.penup()
        nw.speed(0)
        nw.goto(a, 290)
        nw.shape("enemy2.gif")
        direct = ["left", "right"]
        nw.level = 2
        nw.direction = random.choice(direct)
        aliens_list.append(nw)
    return siv


def level3(siv):
    if siv >= 100:
        siv = 0
        a = random.randint(-280, 280)
        nw = turtle.Turtle()
        nw.penup()
        nw.speed(0)
        nw.goto(a, 290)
        nw.shape("enemy3.gif")
        direct = ["left", "right"]
        nw.level = 3
        nw.direction = random.choice(direct)
        aliens_list.append(nw)
    return siv


def heart(liv):
    if liv == 2:
        hrt3.hideturtle()
    if liv == 1:
        hrt2.hideturtle()
    if liv == 0:
        hrt1.hideturtle()
    return


window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")
window.onkeypress(shoot, " ")

time.sleep(1)
while True:
    window.update()
    move()
    lives = collision(lives)
    heart(lives)

    for bull in bullet_list:
        x = bull.xcor()
        y = bull.ycor()
        bull.goto(x, y+2)

    if ship.score < 3500:
        spawn = level1(spawn)
        bg_move = 1
    elif ship.score <= 6000:
        spawn = level2(spawn)
        bg_move = 1.25
    elif ship.score <= 10000:
        spawn = level3(spawn)
        bg_move = 1.5
    else:
        bg_move = 0
        break

    for alien in aliens_list:
        x = alien.xcor()
        y = alien.ycor()
        if alien.level == 1:
            c = random.randint(-2, 2)
            d = random.randint(0, 2)
        elif alien.level == 2:
            if random.randint(0, 5) == 2:
                c = random.randint(-7, 7)
            else:
                c = 0
            d = random.randint(0, 2)
        elif alien.level == 3:
            if alien.direction == "left":
                c = -0.5
            else:
                c = 0.5
            d = random.randint(0, 2)
        else:
            c = 0
            d = 1
        if x <= -400:
            if alien.level == 3:
                alien.direction = "right"
            c = 5
        elif x >= 400:
            if alien.level == 3:
                alien.direction = "left"
            c = -5
        alien.goto(x + c, y - d)

    if lives == 0:
        ship.shape("spaceship3crash.gif")
        break

    y7 = back.ycor()
    back.goto(0, y7 - bg_move)

    if y7-1 < -1750:
        back.goto(0, 1750)

    ship.shoot += 0.5
    spawn += 0.5

if lives == 0:
    back.hideturtle()
    window.bgpic('gameover.gif')
    ship.goto(0, -100)
    window.update()
if lives != 0:
    win = turtle.Turtle()
    win.speed(0)
    win.penup()
    win.color("white")
    win.hideturtle()
    win.write(" Congrats You Win ", align="center", font=("ds-digital", 36, "normal"))
sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("white")
sc.penup()
sc.hideturtle()
sc.goto(0, 260)
sc.write("score: {} ".format(ship.score), align="center", font=("ds-digital", 24, "normal"))
winsound.PlaySound('gameover.wav', winsound.SND_ASYNC)
time.sleep(5)
