import time
import keyboard
import tkinter as tk
import threading
import os
from tkinter import *
from tkinter import messagebox
window = tk.Tk()
window.title("Ticker Control")
breaks = 0
heads = 0
sports = 0
business = 0
running = 0

headline_combinations = [
    ["ctrl", "3"],
    ["ctrl", "4"],
    ["ctrl", "5"],
]
breaking_combinations = [
    ["ctrl", "7"],
    ["ctrl", "8"],
    ["ctrl", "9"],
]
sports_combinations = [
    ["ctrl", "s"],
    ["ctrl", "d"],
]
business_combinations = [
    ["ctrl", "g"],
    ["ctrl", "h"],
]
followus_combinations = [
    ["ctrl", "k"],
    ["ctrl", "1"],
]

delay1 = 3
delay = 6
threadstatus = False

def start():
    global breaks
    global heads
    global sports
    global business
    global threadstatus
    global enter_heads
    global enter_breaking
    global enter_sports
    global enter_business
    if(str(enter_heads.get())).isdigit() and (str(enter_breaking.get())).isdigit() and (str(enter_sports.get())).isdigit() and (str(enter_business.get())):
        if (int(enter_breaking.get())) <= 3 and (int(enter_breaking.get())) >= 0 and (int(enter_heads.get())) <= 3 and (int(enter_heads.get())) >= 0 and (int(enter_sports.get())) <= 2 and (int(enter_sports.get())) >= 0 and (int(enter_business.get())) <= 2 and (int(enter_business.get())) >= 0:
            breaks = int(enter_breaking.get())
            heads = int(enter_heads.get())
            sports = int(enter_sports.get())
            business = int(enter_business.get())
            enter_breaking.config(state='disabled')
            enter_heads.config(state='disabled')
            enter_sports.config(state='disabled')
            enter_business.config(state='disabled')
            threadstatus = True
            action_thread = threading.Thread(target=eksekusi)
            action_thread.start()
        else:
            messagebox.showinfo("Perhatian", "Jumlah HEADLINES dan BREAKING maksimal 3 dan jumlah SPORTS dan BUSINESS maksimal 2.")
    else:
        messagebox.showinfo("Perhatian", "Masukkan angka dengan benar.")

def stop():
    keyboard.press("ctrl" + "+" + "0")
    time.sleep(0.02)
    keyboard.release("ctrl" + "+" + "0")
    keyboard.press("ctrl" + "+" + "1")
    time.sleep(0.02)
    keyboard.release("ctrl" + "+" + "1")
    global threadstatus
    threadstatus = False
    os._exit(0)

def pentotrigger():
    global threadstatus
    if threadstatus == False:
        start()
    else:
        stop()

def eksekusi():
    global breaks
    global heads
    global sports
    global business
    global threadstatus
    while threadstatus:
        keyboard.press("ctrl" + "+" + "1")
        time.sleep(0.05)
        keyboard.release("ctrl" + "+" + "1")
        time.sleep(delay1)
        if breaks != 0:
            keyboard.press("ctrl" + "+" + "6")
            time.sleep(0.05)
            keyboard.release("ctrl" + "+" + "6")
            time.sleep(delay1)
            for x in range(breaks):
                keyboard.press((breaking_combinations[x])[0] + "+" +(breaking_combinations[x])[1])
                time.sleep(0.05)
                keyboard.release((breaking_combinations[x])[0] + "+" +(breaking_combinations[x])[1])
                time.sleep(delay)
        if heads != 0:
            keyboard.press("ctrl" + "+" + "2")
            time.sleep(0.05)
            keyboard.release("ctrl" + "+" + "2")
            time.sleep(delay1)
            for x in range(heads):
                keyboard.press((headline_combinations[x])[0] + "+" +(headline_combinations[x])[1])
                time.sleep(0.05)
                keyboard.release((headline_combinations[x])[0] + "+" +(headline_combinations[x])[1])
                time.sleep(delay)
        if sports != 0:
            keyboard.press("ctrl" + "+" + "a")
            time.sleep(0.05)
            keyboard.release("ctrl" + "+" + "a")
            time.sleep(delay1)
            for x in range(sports):
                keyboard.press((sports_combinations[x])[0] + "+" +(sports_combinations[x])[1])
                time.sleep(0.05)
                keyboard.release((sports_combinations[x])[0] + "+" +(sports_combinations[x])[1])
                time.sleep(delay)
        if business != 0:
            keyboard.press("ctrl" + "+" + "f")
            time.sleep(0.05)
            keyboard.release("ctrl" + "+" + "f")
            time.sleep(delay1)
            for x in range(business):
                keyboard.press((business_combinations[x])[0] + "+" +(business_combinations[x])[1])
                time.sleep(0.05)
                keyboard.release((business_combinations[x])[0] + "+" +(business_combinations[x])[1])
                time.sleep(delay)
        keyboard.press("ctrl" + "+" + "j")
        time.sleep(0.05)
        keyboard.release("ctrl" + "+" + "j")
        time.sleep(delay1)
        for combination in followus_combinations:
            keyboard.press(combination[0] + "+" + combination[1])
            time.sleep(0.05)
            keyboard.release(combination[0] + "+" + combination[1])
            time.sleep(delay)

global label_heads
label_heads = tk.Label(text="Jumlah HEADLINES")
global enter_heads
enter_heads = tk.Entry(width=1)
global label_breaking
label_breaking = tk.Label(text="Jumlah BREAKING")
global enter_breaking
enter_breaking = tk.Entry(width=1)
global label_sports
label_sports = tk.Label(text="Jumlah SPORTS")
global enter_sports
enter_sports = tk.Entry(width=1)
global label_business
label_business = tk.Label(text="Jumlah BUSINESS")
global enter_business
enter_business = tk.Entry(width=1)
global startbutton
startbutton = tk.Button(text="Mulai/Berhenti", command=pentotrigger)
label_heads.pack()
enter_heads.pack()
label_breaking.pack()
enter_breaking.pack()
label_sports.pack()
enter_sports.pack()
label_business.pack()
enter_business.pack()
startbutton.pack()

window.mainloop()

