from turtle import *
from random import choice

colours = ['yellow', 'red', 'blue', 'green', 'orange', 'purple']
speed(6)
ht()

def penup_goto(x, y):
    pu()
    goto(x, y)
    pd()

#Constant variables
slant = 50
length = 150
breadth = 100
thickness = 48
startx = 50
starty = 20
page_height = 8
bookmark_breadth = 30
bookmark_length = 50

#Tests to ensure that the variables are suitable for drawing.
assert page_height % 2 == 0, "'page_height' must be an even number."
assert thickness % page_height == 0, "Thickness must be a multiple of 'page_height' for the book pages at the sides to be drawn correctly"
assert thickness % (page_height / 2) == 0, "Thickness must be a multiple of page_height / 2: " + str(page_height / 2) + " for the book pages at the bottom to be drawn correctly."

def book_cover():
    penup_goto(startx - slant, starty - breadth)
    goto(startx, starty)
    goto(startx + length + slant, starty)
    goto(startx + length, starty - breadth)
    goto(startx - slant, starty - breadth)
    
def book_stack():
    goto(startx - slant, starty - breadth - thickness)
    goto(startx + length, starty - breadth - thickness)
    goto(startx + length, starty - breadth)
    
def book_stack_pages():
    for i in range(thickness / (page_height / 2)):
        penup_goto(startx - slant, starty - breadth - (i * (page_height / 2)))
        fd(startx + length)
        
def book_sides():
    penup_goto(startx + length, starty - breadth - thickness)
    goto(startx + length + slant, starty - thickness)
    goto(startx + length + slant, starty)
    
def book_sides_pages():
    for i in range(thickness / page_height):
        penup_goto(startx + length, starty - breadth - (i * page_height))
        goto(startx + length + slant, starty - (i * page_height))
        
def bookmark():
    penup_goto(startx + 20, starty)
    goto(startx + slant, starty + bookmark_breadth)
    goto(startx + bookmark_length + slant, starty + bookmark_breadth)
    goto(startx + 20 + bookmark_length, starty)
    goto(startx + 20, starty)
    
def colour(perimeter_color, area_color, func):
    pensize(3)
    color(perimeter_color)
    func()
    pensize(1)
    color(area_color)
    begin_fill()
    func()
    end_fill()
    color('black')
    
def book():
    colour('black', choice(colours), bookmark)
    colour('black', choice(colours), book_cover)
    book_stack()
    book_stack_pages()
    book_sides()
    book_sides_pages()

book()
