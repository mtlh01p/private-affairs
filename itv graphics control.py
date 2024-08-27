import time
import keyboard
import tkinter as tk
from tkinter import *
from tkinter import messagebox
window = tk.Tk()
window.title("ITV News Graphics Control")
logo_value = 0
name1_value = 0
name2_value = 0
name3_value = 0
name4_value = 0
live1_value = 0
live2_value = 0
cornerDOG_value = 0
head_value = 0
info1_value = 0
info2_value = 0
replabel_value = 0

def clear():
    if name1_value == 1:
        name1g_show()
    elif name2_value == 1:
        name2g_show()
    elif name3_value == 1:
        name3g_show()
    elif name4_value == 1:
        name4g_show()
    if live1_value == 1:
        live1_show()
    elif live2_value == 1:
        live2_show()
    elif info1_value == 1:
        info1()
    elif info2_value == 1:
        info2()
    elif replabel_value == 1:
        replabel_show()
    keyboard.press("shift" + "+" + "m")
    time.sleep(0.05)
    keyboard.release("shift" + "+" + "m")
    
def itv1dog_show():
    global logo_value
    if logo_value == 0:
        keyboard.press("shift" + "+" + "v")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "v")
        time.sleep(0.6)
        keyboard.press("ctrl" + "+" + "v")
        time.sleep(0.05)
        keyboard.release("ctrl" + "+" + "v")
        logo_value = 1
    else:
        keyboard.press("alt" + "+" + "v")
        time.sleep(0.05)
        keyboard.release("alt" + "+" + "v")
        time.sleep(0.15)
        keyboard.press("ctrl" + "+" + "alt" + "+" + "v")
        time.sleep(0.05)
        keyboard.release("ctrl" + "+" + "alt" + "+" + "v")
        logo_value = 0

def cornerlocker_show():
    global cornerDOG_value
    if cornerDOG_value == 1:
        headdog_show()
    keyboard.press("shift" + "+" + "g")
    time.sleep(0.05)
    keyboard.release("shift" + "+" + "g")
    time.sleep(0.55)

def name1g_show():
    global cornerDOG_value
    if cornerDOG_value == 1:
        headdog_show()
    global head_value
    if head_value != 0:
        clear()
        headdog_show()
        head_value = 0
        keyboard.press("shift" + "+" + "b")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "b")
        time.sleep(0.05)
        keyboard.press("shift" + "+" + "b")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "b")
    global name1_value
    global name2_value
    global name3_value
    global name4_value
    ur = [["ctrl", "1"], ["ctrl", "2"], ["ctrl", "3"], ["ctrl", "4"]]
    if name1_value == 0:
        if name2_value == 1:
            name2g_show()
        elif name3_value == 1:
            name3g_show()
        elif name4_value == 1:
            name4g_show()
        cornerlocker_show()
        for x in range(len(ur)):
            keyboard.press((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.05)
            keyboard.release((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.05)
        name1_value = 1
    else:
        for x in range((len(ur)-1), (-1), (-1)):
            keyboard.press((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.05)
            keyboard.release((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.05)
        cornerlocker_show()
        name1_value = 0

def name2g_show():
    global cornerDOG_value
    if cornerDOG_value == 1:
        headdog_show()
    global head_value
    if head_value != 0:
        clear()
        headdog_show()
        head_value = 0
        keyboard.press("shift" + "+" + "b")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "b")
        time.sleep(0.05)
        keyboard.press("shift" + "+" + "b")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "b")
    global name1_value
    global name2_value
    global name3_value
    global name4_value
    ur = [["ctrl", "5"], ["ctrl", "6"], ["ctrl", "7"], ["ctrl", "8"]]
    if name2_value == 0:
        if name1_value == 1:
            name1g_show()
        elif name3_value == 1:
            name3g_show()
        elif name4_value == 1:
            name4g_show()
        cornerlocker_show()
        for x in range(len(ur)):
            keyboard.press((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.05)
            keyboard.release((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.05)
        name2_value = 1
    else:
        for x in range((len(ur)-1), (-1), (-1)):
            keyboard.press((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.05)
            keyboard.release((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.05)
        cornerlocker_show()
        name2_value = 0

def name3g_show():
    global cornerDOG_value
    if cornerDOG_value == 1:
        headdog_show()
    global head_value
    if head_value != 0:
        clear()
        headdog_show()
        head_value = 0
        keyboard.press("shift" + "+" + "b")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "b")
        time.sleep(0.05)
        keyboard.press("shift" + "+" + "b")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "b")
    global name1_value
    global name2_value
    global name3_value
    global name4_value
    ur = [["alt", "1"], ["alt", "2"], ["alt", "3"], ["alt", "4"]]
    if name3_value == 0:
        if name1_value == 1:
            name1g_show()
        elif name2_value == 1:
            name2g_show()
        elif name4_value == 1:
            name4g_show()
        cornerlocker_show()
        for x in range(len(ur)):
            keyboard.press((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.05)
            keyboard.release((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.05)
        name3_value = 1
    else:
        for x in range((len(ur)-1), (-1), (-1)):
            keyboard.press((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.05)
            keyboard.release((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.05)
        cornerlocker_show()
        name3_value = 0

def name4g_show():
    global cornerDOG_value
    if cornerDOG_value == 1:
        headdog_show()
    global head_value
    if head_value != 0:
        clear()
        headdog_show()
        head_value = 0
        keyboard.press("shift" + "+" + "b")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "b")
        time.sleep(0.05)
        keyboard.press("shift" + "+" + "b")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "b")
    global name1_value
    global name2_value
    global name3_value
    global name4_value
    ur = [["alt", "5"], ["alt", "6"], ["alt", "7"], ["alt", "8"]]
    if name4_value == 0:
        if name1_value == 1:
            name1g_show()
        elif name2_value == 1:
            name2g_show()
        elif name3_value == 1:
            name3g_show()
        cornerlocker_show()
        for x in range(len(ur)):
            keyboard.press((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.05)
            keyboard.release((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.05)
        name4_value = 1
    else:
        for x in range((len(ur)-1), (-1), (-1)):
            keyboard.press((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.05)
            keyboard.release((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.05)
        cornerlocker_show()
        name4_value = 0

def live1_show():
    global live1_value
    global live2_value
    global info1_value
    global info2_value
    global replabel_value
    if info1_value == 1:
        info1()
    elif info2_value == 1:
        info2()
    elif replabel_value == 1:
        replabel_show()
    ur = [["shift", "q"], ["ctrl", "q"], ["alt", "q"]]
    if live1_value == 0:
        if live2_value == 1:
            live2_show()
        for x in range(len(ur)):
            keyboard.press((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.05)
            keyboard.release((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.4)
        live1_value = 1
    else:
        for x in range((len(ur)-1), (-1), (-1)):
            keyboard.press((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.05)
            keyboard.release((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.15)
        live1_value = 0

def live2_show():
    global live1_value
    global live2_value
    global info1_value
    global info2_value
    global replabel_value 
    if info1_value == 1:
        info1()
    elif info2_value == 1:
        info2()
    elif replabel_value == 1:
        replabel_show()
    ur = [["shift", "w"], ["ctrl", "w"], ["alt", "w"]]
    if live2_value == 0:
        if live1_value == 1:
            live1_show()
        for x in range(len(ur)):
            keyboard.press((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.05)
            keyboard.release((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.4)
        live2_value = 1
    else:
        for x in range((len(ur)-1), (-1), (-1)):
            keyboard.press((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.05)
            keyboard.release((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.15)
        live2_value = 0

def start():
    keyboard.press("shift" + "+" + "y")
    time.sleep(0.05)
    keyboard.release("shift" + "+" + "y")
    global cornerDOG_value
    if cornerDOG_value == 0:
        headdog_show()

def headdog_show():
    global cornerDOG_value
    keyboard.press("shift" + "+" + "n")
    time.sleep(0.05)
    keyboard.release("shift" + "+" + "n")
    if cornerDOG_value == 0:
        cornerDOG_value = 1
    else:
        cornerDOG_value = 0

def titlestart():
    global name1_value
    global name2_value
    global name3_value
    global name4_value
    global replabel_value
    keyboard.press("shift" + "+" + "b")
    time.sleep(0.05)
    keyboard.release("shift" + "+" + "b")
    time.sleep(2)
    if name1_value == 1:
        name1g_show()
    elif name2_value == 1:
        name2g_show()
    elif name3_value == 1:
        name3g_show()
    elif name4_value == 1:
        name4g_show()
    elif replabel_value == 1:
        replabel_show()
    clear()
    global cornerDOG_value
    global live1_value
    global live2_value
    global info1_value
    global info2_value
    if cornerDOG_value == 1:
        headdog_show()
    if live1_value == 1:
        live1_show()
    elif live2_value == 1:
        live2_show()
    elif info1_value == 1:
        info1()
    elif info2_value == 1:
        info2()

def head(i):
    global live1_value
    global live2_value
    global info1_value
    global info2_value
    global replabel_value
    global cornerDOG_value
    if cornerDOG_value == 0:
        headdog_show()
    if live1_value == 1:
        live1_show()
    elif live2_value == 1:
        live2_show()
    elif info1_value == 1:
        info1()
    elif info2_value == 1:
        info2()
    elif replabel_value == 1:
        replabel_show()
    global name1_value
    global name2_value
    global name3_value
    global name4_value
    if name1_value == 1:
        name1g_show()
    elif name2_value == 1:
        name2g_show()
    elif name2_value == 1:
        name2g_show()
    elif name3_value == 1:
        name3g_show()
    elif name4_value == 1:
        name4g_show()
    global head_value
    if i == 1:
        keyboard.press("shift" + "+" + "1")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "1")
        head_value == 1
    elif i == 2:
        keyboard.press("shift" + "+" + "2")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "2")
        head_value == 2
    elif i == 3:
        keyboard.press("shift" + "+" + "3")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "3")
        head_value == 3
    elif i == 4:
        keyboard.press("shift" + "+" + "4")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "4")
        head_value == 4
    else:
        keyboard.press("shift" + "+" + "5")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "5")
        head_value == 5

def info1():
    global info1_value
    global info2_value
    global live1_value
    global live2_value
    global replabel_value
    if info1_value == 0:
        if info2_value == 1:
            info2()
        elif live1_value == 1:
            live1_show()
        elif live2_value == 1:
            live2_show()
        elif replabel_value == 1:
            replabel_show()
        keyboard.press("shift" + "+" + "u")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "u")
        time.sleep(0.05)
        keyboard.press("ctrl" + "+" + "u")
        time.sleep(0.05)
        keyboard.release("ctrl" + "+" + "u")
        time.sleep(0.05)
        keyboard.press("alt" + "+" + "u")
        time.sleep(0.05)
        keyboard.release("alt" + "+" + "u")
        time.sleep(0.05)
        keyboard.press("ctrl" + "+" + "alt" + "+" + "u")
        time.sleep(0.05)
        keyboard.release("ctrl" + "+" + "alt" + "+" + "u")
        time.sleep(0.05)
        info1_value = 1
    else:
        keyboard.press("ctrl" + "+" + "alt" + "+" + "u")
        time.sleep(0.05)
        keyboard.release("ctrl" + "+" + "alt" + "+" + "u")
        time.sleep(0.05)
        keyboard.press("alt" + "+" + "u")
        time.sleep(0.05)
        keyboard.release("alt" + "+" + "u")
        time.sleep(0.05)
        keyboard.press("ctrl" + "+" + "u")
        time.sleep(0.05)
        keyboard.release("ctrl" + "+" + "u")
        time.sleep(0.05)
        keyboard.press("shift" + "+" + "u")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "u")
        time.sleep(0.05)
        info1_value = 0

def info2():
    global info1_value
    global info2_value
    global live1_value
    global live2_value
    global replabel_value
    if info2_value == 0:
        if info1_value == 1:
            info1()
        elif live1_value == 1:
            live1_show()
        elif live2_value == 1:
            live2_show()
        elif replabel_value == 1:
            replabel_show()
        keyboard.press("shift" + "+" + "i")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "i")
        time.sleep(0.05)
        keyboard.press("ctrl" + "+" + "i")
        time.sleep(0.05)
        keyboard.release("ctrl" + "+" + "i")
        time.sleep(0.05)
        keyboard.press("alt" + "+" + "i")
        time.sleep(0.05)
        keyboard.release("alt" + "+" + "u")
        time.sleep(0.05)
        keyboard.press("ctrl" + "+" + "alt" + "+" + "i")
        time.sleep(0.05)
        keyboard.release("ctrl" + "+" + "alt" + "+" + "i")
        time.sleep(0.05)
        info2_value = 1
    else:
        keyboard.press("ctrl" + "+" + "alt" + "+" + "i")
        time.sleep(0.05)
        keyboard.release("ctrl" + "+" + "alt" + "+" + "i")
        time.sleep(0.05)
        keyboard.press("alt" + "+" + "i")
        time.sleep(0.05)
        keyboard.release("alt" + "+" + "i")
        time.sleep(0.05)
        keyboard.press("ctrl" + "+" + "i")
        time.sleep(0.05)
        keyboard.release("ctrl" + "+" + "i")
        time.sleep(0.05)
        keyboard.press("shift" + "+" + "i")
        time.sleep(0.05)
        keyboard.release("shift" + "+" + "i")
        time.sleep(0.05)
        info2_value = 0

def replabel_show():
    global info1_value
    global info2_value
    global live1_value
    global live2_value
    global replabel_value
    ur = [["shift", "r"], ["ctrl", "r"], ["alt", "r"], ["shift", "t"], ["ctrl", "t"]]
    if replabel_value == 0:
        if info1_value == 1:
            info1()
        elif info2_value == 1:
            info2()
        elif live1_value == 1:
            live1_show()
        elif live2_value == 1:
            live2_show()
        keyboard.press((ur[0])[0] + "+" + (ur[0])[1])
        time.sleep(0.05)
        keyboard.release((ur[0])[0] + "+" + (ur[0])[1])
        time.sleep(0.5)
        for x in range(1, len(ur)):
            keyboard.press((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.05)
            keyboard.release((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.05)
        replabel_value = 1
    else:
        for x in range((len(ur)-1), (-1), (-1)):
            keyboard.press((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.05)
            keyboard.release((ur[x])[0] + "+" + (ur[x])[1])
            time.sleep(0.05)
        replabel_value = 0

def sub_show():
    keyboard.press("shift" + "+" + "z")
    time.sleep(0.05)
    keyboard.release("shift" + "+" + "z")
    time.sleep(5)
    keyboard.press("shift" + "+" + "z")
    time.sleep(0.05)
    keyboard.release("shift" + "+" + "z")
    time.sleep(0.15)
    if logo_value == 0:
        itv1dog_show()
    
itv1dog = tk.Button(text="ITV1 DOG", command=itv1dog_show)
itv1dogsub = tk.Button(text="ITV1 DOG with subtitles", command=sub_show)
name1 = tk.Button(text="Nama 1", command=name1g_show)
name2 = tk.Button(text="Nama 2", command=name2g_show)
name3 = tk.Button(text="Nama 3", command=name3g_show)
name4 = tk.Button(text="Nama 4", command=name4g_show)
livebottom = tk.Button(text="Live 1", command=live1_show)
livebottom2 = tk.Button(text="Live 2", command=live2_show)
starthead = tk.Button(text="Start", command=start)
cornerDOG = tk.Button(text="Headline DOG", command=headdog_show)
headscreenclear = tk.Button(text="Clear screen", command=clear)
head1 = tk.Button(text="Headline 1", command=lambda:[head(1)])
head2 = tk.Button(text="Headline 2", command=lambda:[head(2)])
head3 = tk.Button(text="Headline 3", command=lambda:[head(3)])
head4 = tk.Button(text="Headline 4", command=lambda:[head(4)])
head5 = tk.Button(text="Headline 5", command=lambda:[head(5)])
titles = tk.Button(text="Titles", command=titlestart)
infobot1 = tk.Button(text="Info Bottom 1", command=info1)
infobot2 = tk.Button(text="Info Bottom 2", command=info2)
reporterbox = tk.Button(text="Reporter Label", command=replabel_show)
itv1dog.pack()
itv1dogsub.pack()
name1.pack()
name2.pack()
name3.pack()
name4.pack()
livebottom.pack()
livebottom2.pack()
starthead.pack()
cornerDOG.pack()
headscreenclear.pack()
head1.pack()
head2.pack()
head3.pack()
head4.pack()
head5.pack()
titles.pack()
infobot1.pack()
infobot2.pack()
reporterbox.pack()
