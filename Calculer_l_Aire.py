# coding: utf8
from __future__ import unicode_literals

import sys

from grove_rgb_lcd import *


def Message(msg):
    setText("")
    text = msg
    length = len(msg)
    if length < 32: setText(text)
    else:
        for i in range(0, 32):
            text = " " + text
            setText_norefresh(text)
            time.sleep(.1)

def MyPrint(msg, r, g, b):
        setRGB(r,g,b)
        Message(msg)

def Demo():
    text = "Bonjour"
    while True:
        text = " " + text
        setText(text)
        time.sleep(.5)

def AireCarre():
    MyPrint("Veuillez taper la longueur d'un côté de votre carré : ", 255, 0, 0)
    input = raw_input()
    print(input)
    x = int(input)
    MyPrint("%d²" % (x*x),255, 0, 0)
    time.sleep(2)

def AireTriangle():
    MyPrint("Veuillez taper la longueur de la base de votre triangle quelconque : ", 0, 0, 255),
    input = raw_input()
    print(input)
    x = int(input)
    MyPrint("Veuillez taper la longueur de la hauteur de votre triangle quelconque : ", 0, 0, 255),
    input2 = raw_input()
    print(input2)
    y = int(input2)
    MyPrint("%d²" % (x*y/2), 0, 0, 255)
    time.sleep(2)

def Fin():
     MyPrint("Non, ne me quitte pas..", 0, 0, 0)
     sys.exit()

while True:
    MyPrint("Le Calculateur d'aire", 0, 200, 100)
    print("Bonjour et bienvenue dans le calculateur d'aire")
    print("1 : L'aire du Carré")
    print("2 : L'aire du Triangle quelconque")
    print("d : Démo")
    print("q : quitter")
    ans=raw_input("Que veux-tu calculer ? ")
    if ans=="1":AireCarre()
    if ans=="2":AireTriangle()
    if ans=="q":Fin()
    if ans=="d":Demo()
