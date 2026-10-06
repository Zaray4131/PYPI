from turtle import width
from typing import Any


(function) Actor: Any
(function) screen: Any
alien = Actor('alien')
alien.pos = 10, 10

def draw():
    screen.clear()
    alien.draw()

def update():
    alien.x += 1
    if alien.left > width:
        alien.right = 0