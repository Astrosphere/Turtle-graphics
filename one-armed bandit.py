#One-armed bandit
#Coded in python3

from turtle import *
from time import *
import random
import sys
play_again = numinput('Again', 'Would you like to play again? If so write 1')

while play_again == 1:
    clear()
    reset()

    #Screen configurations
    tracer(25)
    pu()
    goto(85,200)
    amount = numinput('Cash', 'How much do you want to spend in USD?')
    first_win = amount * 2
    second_win = amount / 2
    write('Welcome to one-armed bandit', align='center', font=("arial",30,"bold"))
    ht()
    title('One-armed bandit')
    setup(1000,600)
    bgcolor('green')
    shape('turtle')
    pensize(2)
    speed(40)

    #Price box
    goto(-370,270)
    write('Won? check here!: ', align='center', font=("arial",20,"bold"))

    #Generate random colors

    colors = ['blue', 'red', 'green']
    x_one = random.choice(colors)
    x_two = random.choice(colors)
    x_three = random.choice(colors)

    #############----Game code----#############

    #box 1
    color('black',x_one)
    pu()
    goto(200,-150)
    pd()
    begin_fill()
    fd(200)
    goto(200,-150)
    pd()
    left(90)
    fd(200)
    right(90)
    fd(200)
    right(90)
    fd(200)
    pu()
    end_fill()
    sleep(0.5)

    #box2
    color('black',x_two)
    begin_fill()
    goto(180,-150)
    pd()
    right(90)
    fd(200)
    right(90)
    fd(200)
    right(90)
    fd(200)
    right(90)
    fd(200)
    pu()
    end_fill()
    sleep(0.5)
    50

    #box3
    color('black',x_three)
    begin_fill()
    goto(-40,-150)
    right(90)
    pd()
    fd(200)
    right(90)
    fd(200)
    right(90) 
    fd(200)
    right(90)
    fd(200)
    end_fill()
    sleep(0.5)

    #part of the border
    pu()
    goto(0,200)
    pd()
    right(90)
    fd(500)
    bk(1000)
    pu()
    goto(-200,200)
    right(90)
    pd()
    fd(100)
    left(90)
    fd(300)
    left(90)
    fd(600)
    left(90)
    fd(1000)
    left(90)
    fd(500)
    pu()


    #Price
    goto(-350,250)
    if x_one == x_two == x_three:
        write('You scored three of the same color, you win: ', align='center', font=("arial",10,"bold"))
        goto(-460,220)
        write(first_win, font=("arial",10,"bold"))
    elif x_one == x_two or x_three == x_one or x_two == x_three:
        write('You scored two of the same color, you win: ', align='center', font=("arial",10,"bold"))
        goto(-480,220)
        write(second_win, font=("arial",10,"bold"))
    else:
        write('Nope, you did not win.. noob', align='center', font=("arial",10,"bold"))

    #Finish game
    sleep(5)
