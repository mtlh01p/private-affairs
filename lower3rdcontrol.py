import time
import keyboard
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
window = tk.Tk()
window.title("Lower 3rd Control")
breakingvalue = 0
standardvalue = 0
tickervalue = 0
shortnamevalue = 0
longnamevalue = 0
delay1 = 800/3/1000
delay2 = 800/1000
delay3 = 500/1000
determiner = "1"
inbriefmusic = False
trd = 0

def inbrieftrigger():
    global standardvalue
    global inbriefmusic
    if standardvalue == 0:
        inbriefmusic = True
        keyboard.press("shift" + "+" + "y")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "y")
        standardtrigger()
        time.sleep(0.5)
        keyboard.press("ctrl" + "+" + "t")
        time.sleep(0.05)
        keyboard.release("ctrl" + "+" + "t")
    else:
        if inbriefmusic == True:
            inbriefmusic = False
            keyboard.press("shift" + "+" + "y")
            time.sleep(0.05)
            keyboard.release("shift" + "+" + "y")
            keyboard.press("shift" + "+" + "j")
            time.sleep(0.05)
            keyboard.release("shift" + "+" + "j")
            standardtrigger()
            time.sleep(3)
            keyboard.press("shift" + "+" + "j")
            time.sleep(0.05)
            keyboard.release("shift" + "+" + "j")
        else:
            inbriefmusic = True
            keyboard.press("shift" + "+" + "y")
            time.sleep(0.05)
            keyboard.release("shift" + "+" + "y")
            keyboard.press("ctrl" + "+" + "t")
            time.sleep(0.05)
            keyboard.release("ctrl" + "+" + "t")

def switch(i):
    global determiner
    if i == 1:
        keyboard.press("alt" + "+" + "a")
        time.sleep(0.05)
        keyboard.release("alt" + "+" + "a")
    elif i == 2:
        keyboard.press("alt" + "+" + "b")
        time.sleep(0.05)
        keyboard.release("alt" + "+" + "b")
    elif i == 3:
        keyboard.press("alt" + "+" + "c")
        time.sleep(0.05)
        keyboard.release("alt" + "+" + "c")
    elif i == 4:
        keyboard.press("alt" + "+" + determiner)
        time.sleep(0.05)
        keyboard.release("alt" + "+" + determiner)

def switchdeterminer(x):
    global determiner
    determiner = str(x)
    keyboard.press("alt" + "+" + determiner)
    time.sleep(0.05)
    keyboard.release("alt" + "+" + determiner)
        
def breaktrigger(n):
    global trd
    global tickervalue
    global breakingvalue
    global standardvalue
    global longnamevalue
    global shortnamevalue
    global determiner
    global inbriefmusic
    if inbriefmusic == True:
        inbriefmusic = False
        keyboard.press("shift" + "+" + "y")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "y")
    if tickervalue == 1:
        if breakingvalue == 0:
            breakingvalue = 1
            if standardvalue == 1:
                standardtrigger()
                time.sleep(0.05)
            if longnamevalue == 1:
                longnametrigger()
                time.sleep(0.05)
            if shortnamevalue == 1:
                shortnametrigger()
                time.sleep(0.05)
            switch(1)
            if trd == 0:
                keyboard.press("alt" + "+" + "j")
                time.sleep(0.05)
                keyboard.release("alt" + "+" + "j")
            else:
                trd = 0
            keyboard.press("shift" + "+" + "r")
            time.sleep(0.05)
            keyboard.release("shift" + "+" + "r")
            time.sleep(delay1)
            keyboard.press("alt" + "+" + "j")
            time.sleep(0.05)
            keyboard.release("alt" + "+" + "j")
            time.sleep(delay2)
            time.sleep(5)
            if n == 1:
                switch(2)
            elif n == 2:
                if determiner == "1" or determiner == "2" or determiner == "3":
                    switch(4)
                else:
                    keyboard.press("alt" + "+" + "1")
                    time.sleep(0.05)
                    keyboard.release("alt" + "+" + "1")
        else:
            if standardvalue == 1:
                trd = 1
            if n == 1:
                switch(2)
            elif n == 2:
                switch(4)
            breakingvalue = 0
            keyboard.press("shift" + "+" + "r")
            time.sleep(0.05)
            keyboard.release("shift" + "+" + "r")
            time.sleep(1.5*delay1)
            keyboard.press("alt" + "+" + "j")
            time.sleep(0.05)
            keyboard.release("alt" + "+" + "j")
            time.sleep(delay3)
            if longnamevalue == 0 and shortnamevalue == 0 and trd == 0:
                keyboard.press("alt" + "+" + "j")
                time.sleep(0.05)
                keyboard.release("alt" + "+" + "j")
    else:
        nsx = 0
        nsv = 0
        if breakingvalue == 0:
            breakingvalue = 1
            if standardvalue == 1:
                nsv = 1
                standardtrigger()
                time.sleep(0.8*delay3)
                keyboard.press("alt" + "+" + "j")
                time.sleep(0.05)
                keyboard.release("alt" + "+" + "j")
            if longnamevalue == 1:
                nsx = 1
                keyboard.press("alt" + "+" + "j")
                time.sleep(0.05)
                keyboard.release("alt" + "+" + "j")
                longnametrigger()
                time.sleep(0.05)
            if shortnamevalue == 1:
                nsx = 1
                keyboard.press("alt" + "+" + "j")
                time.sleep(0.05)
                keyboard.release("alt" + "+" + "j")
                shortnametrigger()
                time.sleep(0.05)
            switch(1)
            keyboard.press("shift" + "+" + "r")
            time.sleep(0.05)
            keyboard.release("shift" + "+" + "r")
            if nsx == 1 or nsv == 1:
                time.sleep(0.55*delay3)
                keyboard.press("alt" + "+" + "j")
                time.sleep(0.05)
                keyboard.release("alt" + "+" + "j")
            time.sleep(5)
            if n == 1:
                switch(2)
            elif n == 2:
                if determiner == "1" or determiner == "2" or determiner == "3":
                    switch(4)
                else:
                    keyboard.press("alt" + "+" + "1")
                    time.sleep(0.05)
                    keyboard.release("alt" + "+" + "1")
        else:
            if n == 1:
                switch(2)
            elif n == 2:
                switch(4)
            breakingvalue = 0
            keyboard.press("shift" + "+" + "r")
            time.sleep(0.05)
            keyboard.release("shift" + "+" + "r")

def longnametrigger():
    global standardvalue
    global breakingvalue
    global shortnamevalue
    global longnamevalue
    global inbriefmusic
    global tickervalue
    nsx = 0
    nsv = 0
    if inbriefmusic == True:
        inbriefmusic = False
        keyboard.press("shift" + "+" + "y")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "y")
    if longnamevalue == 0:
        longnamevalue = 1
        if standardvalue == 1:
            nsv = 1
            standardtrigger()
            time.sleep(0.8*delay3)
            if tickervalue == 0:
                keyboard.press("alt" + "+" + "j")
                time.sleep(0.05)
                keyboard.release("alt" + "+" + "j")
        if breakingvalue == 1:
            nsv = 1
            breaktrigger(1)
            time.sleep(0.8*delay3)
            if tickervalue == 0:
                keyboard.press("alt" + "+" + "j")
                time.sleep(0.05)
                keyboard.release("alt" + "+" + "j")
        if shortnamevalue == 1:
            nsx = 1
            shortnametrigger()
            time.sleep(0.1*delay3)
            keyboard.press("alt" + "+" + "j")
            time.sleep(0.05)
            keyboard.release("alt" + "+" + "j")
    else:
        longnamevalue = 0
    keyboard.press("shift" + "+" + "0")
    time.sleep(0.05)
    keyboard.release("shift" + "+" + "0")
    if nsx == 1 or nsv == 1:
        time.sleep(1.5*delay3)
        keyboard.press("alt" + "+" + "j")
        time.sleep(0.05)
        keyboard.release("alt" + "+" + "j")
    
def shortnametrigger():
    global standardvalue
    global breakingvalue
    global shortnamevalue
    global longnamevalue
    global inbriefmusic
    nsx = 0
    nsv = 0
    if inbriefmusic == True:
        inbriefmusic = False
        keyboard.press("shift" + "+" + "y")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "y")
    if shortnamevalue == 0:
        shortnamevalue = 1
        if standardvalue == 1:
            nsv = 1
            standardtrigger()
            time.sleep(0.8*delay3)
            if tickervalue == 0:
                keyboard.press("alt" + "+" + "j")
                time.sleep(0.05)
                keyboard.release("alt" + "+" + "j")
        if breakingvalue == 1:
            nsv = 1
            breaktrigger(1)
            time.sleep(0.8*delay3)
            if tickervalue == 0:
                keyboard.press("alt" + "+" + "j")
                time.sleep(0.05)
                keyboard.release("alt" + "+" + "j")
        if longnamevalue == 1:
            nsx = 1
            longnametrigger()
            time.sleep(0.1*delay3)
            keyboard.press("alt" + "+" + "j")
            time.sleep(0.05)
            keyboard.release("alt" + "+" + "j")
    else:
        shortnamevalue = 0
    keyboard.press("shift" + "+" + "9")
    time.sleep(0.05)
    keyboard.release("shift" + "+" + "9")
    if nsx == 1 or nsv == 1:
        time.sleep(1.5*delay3)
        keyboard.press("alt" + "+" + "j")
        time.sleep(0.05)
        keyboard.release("alt" + "+" + "j")
        
def standardtrigger():
    global tickervalue
    global standardvalue
    global breakingvalue
    global longnamevalue
    global shortnamevalue
    global inbriefmusic
    global trd 
    if tickervalue == 1:
        if standardvalue == 0:
            standardvalue = 1
            if breakingvalue == 1:
                breaktrigger(1)
                time.sleep(0.05)
            if longnamevalue == 1:
                longnametrigger()
                time.sleep(0.05)
            if shortnamevalue == 1:
                shortnametrigger()
                time.sleep(0.05)
            if trd == 0:
                keyboard.press("alt" + "+" + "j")
                time.sleep(0.05)
                keyboard.release("alt" + "+" + "j")
            else:
                trd = 0
            keyboard.press("shift" + "+" + "g")
            time.sleep(0.05)
            keyboard.release("shift" + "+" + "g")
            time.sleep(delay1)
            keyboard.press("alt" + "+" + "j")
            time.sleep(0.05)
            keyboard.release("alt" + "+" + "j")
        else:
            if inbriefmusic == True:
                inbriefmusic = False
                keyboard.press("shift" + "+" + "y")
                time.sleep(0.05)
                keyboard.release("shift" + "+" + "y")
            standardvalue = 0
            if breakingvalue == 1:
                trd = 1
            keyboard.press("shift" + "+" + "g")
            time.sleep(0.05)
            keyboard.release("shift" + "+" + "g")
            time.sleep(1.5*delay1)
            keyboard.press("alt" + "+" + "j")
            time.sleep(0.05)
            keyboard.release("alt" + "+" + "j")
            time.sleep(delay3)
            if longnamevalue == 0 and shortnamevalue == 0 and trd == 0:
                keyboard.press("alt" + "+" + "j")
                time.sleep(0.05)
                keyboard.release("alt" + "+" + "j")
    else:
        nsx = 0
        nsv = 0
        if standardvalue == 0:
            standardvalue = 1
            if breakingvalue == 1:
                nsv = 1
                breaktrigger(1)
                time.sleep(0.8*delay3)
                keyboard.press("alt" + "+" + "j")
                time.sleep(0.05)
                keyboard.release("alt" + "+" + "j")
            if longnamevalue == 1:
                nsx = 1
                keyboard.press("alt" + "+" + "j")
                time.sleep(0.05)
                keyboard.release("alt" + "+" + "j")
                longnametrigger()
                time.sleep(0.05)
            if shortnamevalue == 1:
                nsx = 1
                keyboard.press("alt" + "+" + "j")
                time.sleep(0.05)
                keyboard.release("alt" + "+" + "j")
                shortnametrigger()
                time.sleep(0.05)
        else:
            if inbriefmusic == True:
                inbriefmusic = False
                keyboard.press("shift" + "+" + "y")
                time.sleep(0.05)
                keyboard.release("shift" + "+" + "y")
            standardvalue = 0
        keyboard.press("shift" + "+" + "g")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "g")
        if nsx == 1 or nsv == 1:
            time.sleep(0.55*delay3)
            keyboard.press("alt" + "+" + "j")
            time.sleep(0.05)
            keyboard.release("alt" + "+" + "j")

def tickertrigger():
    global tickervalue
    if tickervalue == 0:
        tickervalue = 1
    else:
        tickervalue = 0
    keyboard.press("shift" + "+" + "k")
    time.sleep(0.05)
    keyboard.release("shift" + "+" + "k")

def liveloc(val):
    if val == 1:
        keyboard.press("shift" + "+" + "q")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "q")
    elif val == 2:
        keyboard.press("ctrl" + "+" + "q")
        time.sleep(0.05)
        keyboard.release("ctrl" + "+" + "q")
    elif val == 3:
        keyboard.press("shift" + "+" + "w")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "w")
    elif val == 4:
        keyboard.press("ctrl" + "+" + "w")
        time.sleep(0.05)
        keyboard.release("ctrl" + "+" + "w")

def infosecf(hr):
    if hr == 1:
        keyboard.press("shift" + "+" + "u")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "u")
    elif hr == 2:
        keyboard.press("shift" + "+" + "i")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "i")

global breakingbutton
breakingbutton = tk.Button(text="LOWER 3RD Breaking (Title)", command=lambda:[breaktrigger(1)])
global breaking2button
breaking2button = tk.Button(text="LOWER 3RD Breaking (Title+Details)", command=lambda:[breaktrigger(2)])
global standardbutton
standardbutton = tk.Button(text="LOWER 3RD Standard", command=standardtrigger)
global switch1button
switch1button = tk.Button(text="Title 1", command=lambda:[switch(1)])
global switch2button
switch2button = tk.Button(text="Title 2", command=lambda:[switch(2)])
global switch3button
switch3button = tk.Button(text="Title 3", command=lambda:[switch(3)])
global determinerswitch1
determinerswitch1 = tk.Button(text="Title+Detail 1", command=lambda:[switchdeterminer(1)])
global determinerswitch2
determinerswitch2 = tk.Button(text="Title+Detail 2", command=lambda:[switchdeterminer(2)])
global determinerswitch3
determinerswitch3 = tk.Button(text="Title+Detail 3", command=lambda:[switchdeterminer(3)])
global determinerswitch4
determinerswitch4 = tk.Button(text="Title+Detail 4", command=lambda:[switchdeterminer(4)])
global determinerswitch5
determinerswitch5 = tk.Button(text="Title+Detail 5", command=lambda:[switchdeterminer(5)])
global determinerswitch6
determinerswitch6 = tk.Button(text="Title+Detail 6", command=lambda:[switchdeterminer(6)])
global determinerswitch7
determinerswitch7 = tk.Button(text="Title+Detail 7", command=lambda:[switchdeterminer(7)])
global determinerswitch8
determinerswitch8 = tk.Button(text="Title+Detail 8", command=lambda:[switchdeterminer(8)])
global determinerswitch9
determinerswitch9 = tk.Button(text="Title+Detail 9", command=lambda:[switchdeterminer(9)])
global tickerbutton
tickerbutton = tk.Button(text="TICKER", command=tickertrigger)
global shortnamebutton
shortnamebutton = tk.Button(text="SHORT NAME", command=shortnametrigger)
global longnamebutton
longnamebutton = tk.Button(text="LONG NAME", command=longnametrigger)
global livelocleft1
livelocleft1 = tk.Button(text="LIVE LEFT 1", command=lambda:[liveloc(1)])
global livelocleft2
livelocleft2 = tk.Button(text="LIVE LEFT 2", command=lambda:[liveloc(2)])
global livelocright1
livelocright1 = tk.Button(text="LIVE RIGHT 1", command=lambda:[liveloc(3)])
global livelocright2
livelocright2 = tk.Button(text="LIVE RIGHT 2", command=lambda:[liveloc(4)])
global infosec1
infosec1 = tk.Button(text="INFOBOX 1", command=lambda:[infosecf(1)])
global infosec2
infosec2 = tk.Button(text="INFOBOX 2/USERNAME", command=lambda:[infosecf(2)])
global inbriefbutton
inbriefbutton = tk.Button(text="LOWER 3RD Standard in Brief", command=inbrieftrigger)
breakingbutton.pack()
breaking2button.pack()
standardbutton.pack()
inbriefbutton.pack()
switch1button.pack()
switch2button.pack()
switch3button.pack()
determinerswitch1.pack()
determinerswitch2.pack()
determinerswitch3.pack()
determinerswitch4.pack()
determinerswitch5.pack()
determinerswitch6.pack()
determinerswitch7.pack()
determinerswitch8.pack()
determinerswitch9.pack()
tickerbutton.pack()
shortnamebutton.pack()
longnamebutton.pack()
livelocleft1.pack()
livelocleft2.pack()
livelocright1.pack()
livelocright2.pack()
infosec1.pack()
infosec2.pack()
