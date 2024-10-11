import tkinter as tkt
from tkinter import *
from tkinter import messagebox
window = tkt.Tk()
window.title("Announcements")
window.geometry("900x220")
CB_status = 0
BK_status = 0
stn_index = 0
otw_index = 2
CB_code = ["CB-01", "CB-02", "CB-03", "CB-04", "CB-05", "CB-06", "CB-07", "CB-08", "CB-09", "CB-10", "CB-11", "CB-12"]
BK_code = ["BK-01", "BK-02", "BK-03", "BK-04", "BK-05", "BK-06", "BK-07", "BK-08", "BK-09", "BK-10", "BK-11", "BK-12", "BK-13", "BK-14"]
CB_stn = ["DUKUH ATAS BNI", "SETIABUDI", "RASUNA SAID", "KUNINGAN", "PANCORAN BANK BJB", "CIKOKO", "CILIWUNG", "CAWANG", "TMII", "KAMPUNG RAMBUTAN", "CIRACAS", "HARJAMUKTI"]
BK_stn = ["DUKUH ATAS BNI", "SETIABUDI", "RASUNA SAID", "KUNINGAN", "PANCORAN BANK BJB", "CIKOKO", "CILIWUNG", "CAWANG", "HALIM", "JATIBENING BARU", "CIKUNIR 1", "CIKUNIR 2", "BEKASI BARAT", "JATI MULYA"]
CB_type = ["Terminus", "", "", "", "", "Interchange", "", "Interchange", "", "", "", "Terminus"]
BK_type = ["Terminus", "", "", "", "", "Interchange", "", "Interchange", "Interchange", "", "", "", "", "Terminus"]
CB_meg0 = ["Silakan turun di stasiun berikutnya untuk ke KRL Cikarang Loop Line, KA Bandara Soekarno-Hatta, atau MRT North-South Line.", "", "", "", "", "Silakan turun di stasiun berikutnya untuk ke KRL Bogor Line.", "", "Silakan turun di stasiun berikutnya untuk ke LRT Bekasi Line.", "", "", "", ""]
BK_meg0 = ["Silakan turun di stasiun berikutnya untuk ke KRL Cikarang Loop Line, KA Bandara Soekarno-Hatta, atau MRT North-South Line.", "", "", "", "", "Silakan turun di stasiun berikutnya untuk ke KRL Bogor Line.", "", "Silakan turun di stasiun berikutnya untuk ke LRT Cibubur Line.", "Silakan turun di stasiun berikutnya untuk ke Kereta Api Cepat Jakarta-Bandung.", "", "", "", "", ""]
CB_meg1 = ["Stasiun transit ke KRL Cikarang Loop Line, KA Bandara Soekarno-Hatta, atau MRT North-South Line.", "", "", "", "", "Stasiun transit ke KRL Bogor Line.", "", "Stasiun transit ke LRT Bekasi Line.", "", "", "", ""]
BK_meg1 = ["Stasiun transit ke KRL Cikarang Loop Line, KA Bandara Soekarno-Hatta, atau MRT North-South Line.", "", "", "", "", "Stasiun transit ke KRL Bogor Line.", "", "Stasiun transit ke LRT Cibubur Line.", "Stasiun transit ke Kereta Api Cepat Jakarta-Bandung.", "", "", "", "", ""]
msg_label_temp = ""
msg_label_dest = ""
msg_label_top = ""
stn_name = ""
msg_label_bottom = ""
msg_label_door = ""
DirCity = False

def lineswitch(lin):
    global Next, Slide, Prev, CB_status, BK_status, stn_index, otw_index, texttoshow, stn_name, CB_stn, BK_stn, Line1, Line2, Line3, Line4, Line5
    if lin == "cb":
        CB_status = 1
        CB_start.pack_forget()
        BK_start.pack_forget()
        Next.pack()
        Slide.pack()
        Prev.pack()
        Exit.pack()
    elif lin == "bk":
        BK_status = 1
        CB_start.pack_forget()
        BK_start.pack_forget()
        Next.pack()
        Slide.pack()
        Prev.pack()
        Exit.pack()
    else:
        CB_status = 0
        BK_status = 0
        stn_index = 0
        otw_index = 0
        texttoshow = ""
        stn_name = ""
        CB_start.pack()
        BK_start.pack()
        Next.pack_forget()
        Slide.pack_forget()
        Prev.pack_forget()
        Exit.pack_forget()
        Next["state"] = "normal"
        Prev["state"] = "normal"
        Slide["state"] = "normal"
        Screen1["text"] = ""
        Screen2["text"] = ""
        Screen3["text"] = ""
        Screen4["text"] = ""
        Screen5["text"] = ""

def stnnameformat():
    global CB_status, BK_status, stn_index, stn_name, CB_stn, BK_stn, Line1, Line2, Line3, Line4, Line5
    if CB_status == 1:
        intc_index = -1
        for a in range(len(BK_stn)):
            if BK_stn[a] == CB_stn[stn_index]:
                intc_index = a
        if intc_index == -1:
            stn_name = CB_code[stn_index] + " " + CB_stn[stn_index]
        else:
            stn_name = CB_code[stn_index] + " " + BK_code[intc_index] + " " + CB_stn[stn_index]
    else:
        intc_index = -1
        for a in range(len(CB_stn)):
            if CB_stn[a] == BK_stn[stn_index]:
                intc_index = a
        if intc_index == -1:
            stn_name = BK_code[stn_index] + " " + BK_stn[stn_index]
        else:
            stn_name = BK_code[stn_index] + " " + CB_code[intc_index] + " " + BK_stn[stn_index]

def stnmsg():
    global CB_status, BK_status, stn_index, otw_index, CB_type, BK_type, msg_label_top, msg_label_bottom, msg_label_temp, msg_label_dest, Line1, Line2, Line3, Line4, Line5
    if CB_status == 1:
        if CB_type[stn_index] == "Interchange":
            if otw_index == 0:
                msg_label_top = "Stasiun transit berikutnya"
                msg_label_bottom = CB_meg0[stn_index]
            elif otw_index == 1:
                msg_label_top = "Kereta akan tiba di"
                msg_label_bottom = CB_meg1[stn_index]
            else:
                msg_label_top = "Stasiun transit"
                msg_label_bottom = ""
        elif CB_type[stn_index] == "Terminus":
            if otw_index == 0:
                msg_label_top = "Stasiun berikutnya, stasiun tujuan akhir"
                msg_label_bottom = CB_meg0[stn_index]
            elif otw_index == 1:
                msg_label_top = "Kereta akan tiba di"
                msg_label_bottom = CB_meg1[stn_index]
            else:
                msg_label_top = "Stasiun tujuan akhir"
                msg_label_bottom = "Seluruh penumpang dimohon turun."
        else:
            if otw_index == 0:
                msg_label_top = "Stasiun berikutnya"
                msg_label_bottom = CB_meg0[stn_index]
            elif otw_index == 1:
                msg_label_top = "Kereta akan tiba di"
                msg_label_bottom = CB_meg1[stn_index]
            else:
                msg_label_top = ""
                msg_label_bottom = ""
    else:
        if BK_type[stn_index] == "Interchange":
            if otw_index == 0:
                msg_label_top = "Stasiun transit berikutnya"
                msg_label_bottom = BK_meg0[stn_index]
            elif otw_index == 1:
                msg_label_top = "Kereta akan tiba di"
                msg_label_bottom = BK_meg1[stn_index]
            else:
                msg_label_top = "Stasiun transit"
                msg_label_bottom = ""
        elif BK_type[stn_index] == "Terminus":
            if otw_index == 0:
                msg_label_top = "Stasiun berikutnya, stasiun tujuan akhir"
                msg_label_bottom = BK_meg0[stn_index]
            elif otw_index == 1:
                msg_label_top = "Kereta akan tiba di"
                msg_label_bottom = BK_meg1[stn_index]
            else:
                msg_label_top = "Stasiun tujuan akhir"
                msg_label_bottom = "Seluruh penumpang dimohon turun."
        else:
            if otw_index == 0:
                msg_label_top = "Stasiun berikutnya"
                msg_label_bottom = BK_meg0[stn_index]
            elif otw_index == 1:
                msg_label_top = "Kereta akan tiba di"
                msg_label_bottom = BK_meg1[stn_index]
            else:
                msg_label_top = ""
                msg_label_bottom = ""

def stnswitch(com):
    global Next, Slide, Prev, DirCity, CB_status, BK_status, stn_index, otw_index, texttoshow, stn_name, msg_label_top, msg_label_bottom, msg_label_temp, msg_label_dest, Line1, Line2, Line3, Line4, Line5
    if com == "Next":
        if CB_status == 1:
            msg_label_temp = "Selamat datang di LRT Jabodebek Cibubur Line."
            msg_label_dest = "Tujuan akhir, " + (CB_code[len(CB_code)-1] + " " + CB_stn[len(CB_code)-1])
            if stn_index == (len(CB_code)-1) and otw_index == 2:
                messagebox.showinfo("Attention", "This is terminus station of this line.")
            else:
                stn_index += 1
                otw_index = 0
                stnnameformat()
                stnmsg()
                DirCity = False
                if stn_index == len(CB_code)-1:
                    DirCity = True
        else:
            msg_label_temp = "Selamat datang di LRT Jabodebek Bekasi Line."
            msg_label_dest = "Tujuan akhir, " + (BK_code[len(BK_code)-1] + " " + BK_stn[len(BK_code)-1])
            if stn_index == (len(BK_code)-1) and otw_index == 2:
                messagebox.showinfo("Attention", "This is terminus station of this line.")
            else:
                stn_index += 1
                otw_index = 0
                stnnameformat()
                stnmsg()
                DirCity = False
                if stn_index == len(BK_code)-1:
                    DirCity = True
    elif com == "Prev":
        if stn_index == 0:
            messagebox.showinfo("Attention", "This is terminus station of this line.")
        else:
            otw_index = 0
            stn_index -= 1
            stnnameformat()
            stnmsg()
            if CB_status == 1:
                msg_label_temp = "Selamat datang di LRT Jabodebek Cibubur Line."
                msg_label_dest = "Tujuan akhir, " + (CB_code[0] + " " + CB_stn[0])
                if CB_stn[stn_index] == "CAWANG":
                    msg_label_bottom += " Untuk penumpang yang akan melanjutkan ke KRL Bogor Line, mohon turun di Stasiun Transit CIKOKO."
            else:
                msg_label_temp = "Selamat datang di LRT Jabodebek Bekasi Line."
                msg_label_dest = "Tujuan akhir, " + (BK_code[0] + " " + BK_stn[0])
                if BK_stn[stn_index] == "CAWANG":
                    msg_label_bottom += " Untuk penumpang yang akan melanjutkan ke KRL Bogor Line, mohon turun di Stasiun Transit CIKOKO."
            DirCity = True
            if stn_index == 0:
                DirCity = False
    else:
        if otw_index == 2:
            messagebox.showinfo("Attention", "Move to the next station by selecting Towards Suburbs or City depending on direction.")
        else:
            otw_index += 1
            stnnameformat()
            stnmsg()
    if otw_index == 0:
        Screen1["text"]= msg_label_temp
        Screen2["text"]= msg_label_dest
    else:
        Screen1["text"]=""
        Screen2["text"]=""
    Screen3["text"]= msg_label_top
    Screen4["text"]= stn_name
    Screen5["text"]= msg_label_bottom
    if otw_index == 2:
        Slide["state"] = "disabled"
        if DirCity == False:
            Next["state"] = "normal"
            Prev["state"] = "disabled"
        else:
            Next["state"] = "disabled"
            Prev["state"] = "normal"
    else:
        Slide["state"] = "normal"
        Next["state"] = "disabled"
        Prev["state"] = "disabled"

CB_start = tkt.Button(text="Cibubur Line", command=lambda:[lineswitch("cb")])
BK_start = tkt.Button(text="Bekasi Line", command=lambda:[lineswitch("bk")])
Exit = tkt.Button(text="Back to Home", command=lambda:[lineswitch("stahp")])
Next = tkt.Button(text="Towards Suburbs", command=lambda:[stnswitch("Next")], state="normal")
Slide = tkt.Button(text="Sliding", command=lambda:[stnswitch("Slide")], state="normal")
Prev = tkt.Button(text="Towards City", command=lambda:[stnswitch("Prev")], state="disabled")
Screen1 = tkt.Label(anchor=tkt.CENTER, text="")
Screen2 = tkt.Label(anchor=tkt.CENTER, text="")
Screen3 = tkt.Label(anchor=tkt.CENTER, text="")
Screen4 = tkt.Label(anchor=tkt.CENTER, text="")
Screen5 = tkt.Label(anchor=tkt.CENTER, text="")
Screen1.pack()
Screen2.pack()
Screen3.pack()
Screen4.pack()
Screen5.pack()
CB_start.pack()
BK_start.pack()
