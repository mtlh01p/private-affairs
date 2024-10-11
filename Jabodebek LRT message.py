import tkinter as tkt
from tkinter import *
from tkinter import messagebox
window = tkt.Tk()
window.title("Announcements")
window.geometry("900x220")
CB_status = 0
BK_status = 0
BB_status = 0
BN_status = 0
otw_index = 0
stn_index = 0
CB_code = ["CB-01", "CB-02", "CB-03", "CB-04", "CB-05", "CB-06", "CB-07", "CB-08", "CB-09", "CB-10", "CB-11", "CB-12"]
BK_code = ["BK-01", "BK-02", "BK-03", "BK-04", "BK-05", "BK-06", "BK-07", "BK-08", "BK-09", "BK-10", "BK-11", "BK-12", "BK-13", "BK-14"]
BB_code = ["B-01", "B-02", "B-03", "B-04", "B-05", "B-07", "B-08", "B-09", "B-10", "B-11", "B-12", "B-13", "B-14", "B-15", "B-16", "B-17", "B-18", "B-19", "B-20", "B-21", "B-22", "B-23", "B-24", "B-26"]
BN_code = ["B-01", "B-02", "B-03", "B-04", "B-05", "B-07", "B-08", "B-09", "B-10", "B-11", "B-12", "B-13", "B-14", "B-15", "B-16", "B-17", "B-18", "B-19", "B-20", "B-21", "B-22", "b-24", "b-26"]
CB_stn = ["DUKUH ATAS BNI", "SETIABUDI", "RASUNA SAID", "KUNINGAN", "PANCORAN BANK BJB", "CIKOKO", "CILIWUNG", "CAWANG", "TMII", "KAMPUNG RAMBUTAN", "CIRACAS", "HARJAMUKTI"]
BK_stn = ["DUKUH ATAS BNI", "SETIABUDI", "RASUNA SAID", "KUNINGAN", "PANCORAN BANK BJB", "CIKOKO", "CILIWUNG", "CAWANG", "HALIM", "JATIBENING BARU", "CIKUNIR 1", "CIKUNIR 2", "BEKASI BARAT", "JATI MULYA"]
BB_stn = ["JAKARTA KOTA", "JAYAKARTA", "MANGGA BESAR", "SAWAH BESAR", "JUANDA", "GONDANGDIA", "CIKINI", "MANGGARAI", "TEBET", "CAWANG", "DUREN KALIBATA", "PASAR MINGGU BARU", "PASAR MINGGU", "TANJUNG BARAT", "LENTENG AGUNG", "UNIVERSITAS INDONESIA", "UNIVERSITAS PANCASILA", "PONDOK CINA", "DEPOK BARU", "DEPOK", "CITAYAM", "BOJONGGEDE", "CILEBUT", "BOGOR"]
BN_stn = ["JAKARTA KOTA", "JAYAKARTA", "MANGGA BESAR", "SAWAH BESAR", "JUANDA", "GONDANGDIA", "CIKINI", "MANGGARAI", "TEBET", "CAWANG", "DUREN KALIBATA", "PASAR MINGGU BARU", "PASAR MINGGU", "TANJUNG BARAT", "LENTENG AGUNG", "UNIVERSITAS INDONESIA", "UNIVERSITAS PANCASILA", "PONDOK CINA", "DEPOK BARU", "DEPOK", "CITAYAM", "CIBINONG", "NAMBO"]
CB_type = ["Terminus", "", "", "", "", "Interchange", "", "Interchange", "", "", "", "Terminus"]
BK_type = ["Terminus", "", "", "", "", "Interchange", "", "Interchange", "Interchange", "", "", "", "", "Terminus"]
BB_type = ["Terminus", "", "", "", "", "", "", "Interchange", "", "Interchange", "", "", "", "", "", "", "", "", "", "", "Interchange", "", "", "Terminus"]
BN_type = ["Terminus", "", "", "", "", "", "", "Interchange", "", "Interchange", "", "", "", "", "", "", "", "", "", "", "Interchange", "", "Terminus"]
CB_meg0 = ["Silakan turun di stasiun berikutnya untuk ke KRL Cikarang Loop Line, KA Bandara Soekarno-Hatta, atau MRT North-South Line.", "", "", "", "", "Silakan turun di stasiun berikutnya untuk ke KRL Bogor Line.", "", "Silakan turun di stasiun berikutnya untuk ke LRT Bekasi Line.", "", "", "", ""]
BK_meg0 = ["Silakan turun di stasiun berikutnya untuk ke KRL Cikarang Loop Line, KA Bandara Soekarno-Hatta, atau MRT North-South Line.", "", "", "", "", "Silakan turun di stasiun berikutnya untuk ke KRL Bogor Line.", "", "Silakan turun di stasiun berikutnya untuk ke LRT Cibubur Line.", "Silakan turun di stasiun berikutnya untuk ke Kereta Api Cepat Jakarta-Bandung.", "", "", "", "", ""]
BB_meg0 = ["Periksa dan teliti kembali barang bawaan Anda sebelum turun. Silakan turun di stasiun berikutnya untuk ke Commuter Line Tanjung Priok.", "", "", "", "", "", "", "Silakan turun di stasiun berikutnya untuk ke Commuter Line Cikarang atau Commuter Line Bandara Soekarno-Hatta.", "", "Silakan turun di stasiun berikutnya untuk berpindah moda ke LRT Jabodebek.", "", "", "", "", "", "", "", "", "", "", "Silakan turun di stasiun berikutnya untuk transit ke kereta tujuan Cibinong dan Nambo.", "", "", "Periksa dan teliti kembali barang bawaan Anda sebelum turun."]
BN_meg0 = ["Periksa dan teliti kembali barang bawaan Anda sebelum turun. Silakan turun di stasiun berikutnya untuk ke Commuter Line Tanjung Priok.", "", "", "", "", "", "", "Silakan turun di stasiun berikutnya untuk ke Commuter Line Cikarang atau Commuter Line Bandara Soekarno-Hatta.", "", "Silakan turun di stasiun berikutnya untuk berpindah moda ke LRT Jabodebek.", "", "", "", "", "", "", "", "", "", "", "Silakan turun di stasiun berikutnya untuk transit ke kereta tujuan Bojonggede, Cilebut, dan Bogor.", "", "", "Periksa dan teliti kembali barang bawaan Anda sebelum turun."]
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
    global Next, Slide, Prev, CB_status, BK_status, BB_status, BN_status, stn_index, otw_index, texttoshow, stn_name, CB_stn, BK_stn, BB_stn, BN_stn, Line1, Line2, Line3, Line4, Line5
    if lin == "cb":
        CB_status = 1
        otw_index = 2
        CB_start.pack_forget()
        BK_start.pack_forget()
        BB_start.pack_forget()
        BN_start.pack_forget()
        Next.pack()
        Slide.pack()
        Prev.pack()
        Exit.pack()
    elif lin == "bk":
        BK_status = 1
        otw_index = 2
        CB_start.pack_forget()
        BK_start.pack_forget()
        BB_start.pack_forget()
        BN_start.pack_forget()
        Next.pack()
        Slide.pack()
        Prev.pack()
        Exit.pack()
    elif lin == "bb":
        BB_status = 1
        otw_index = 1
        CB_start.pack_forget()
        BK_start.pack_forget()
        BB_start.pack_forget()
        BN_start.pack_forget()
        Next.pack()
        Slide.pack()
        Prev.pack()
        Exit.pack()
    elif lin == "bn":
        BN_status = 1
        otw_index = 1
        CB_start.pack_forget()
        BK_start.pack_forget()
        BB_start.pack_forget()
        BN_start.pack_forget()
        Next.pack()
        Slide.pack()
        Prev.pack()
        Exit.pack()
    else:
        CB_status = 0
        BK_status = 0
        BB_status = 0
        BN_status = 0
        stn_index = 0
        otw_index = 0
        texttoshow = ""
        stn_name = ""
        CB_start.pack()
        BK_start.pack()
        BB_start.pack()
        BN_start.pack()
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
    global CB_status, BK_status, BB_status, BN_status, stn_index, stn_name, CB_stn, BK_stn, Line1, Line2, Line3, Line4, Line5
    if CB_status == 1:
        intc_index = -1
        for a in range(len(BK_stn)):
            if BK_stn[a] == CB_stn[stn_index]:
                intc_index = a
        if intc_index == -1:
            stn_name = CB_code[stn_index] + " " + CB_stn[stn_index]
        else:
            stn_name = CB_code[stn_index] + " " + BK_code[intc_index] + " " + CB_stn[stn_index]
    elif BK_status == 1:
        intc_index = -1
        for a in range(len(CB_stn)):
            if CB_stn[a] == BK_stn[stn_index]:
                intc_index = a
        if intc_index == -1:
            stn_name = BK_code[stn_index] + " " + BK_stn[stn_index]
        else:
            stn_name = BK_code[stn_index] + " " + CB_code[intc_index] + " " + BK_stn[stn_index]
    elif BB_status == 1:
        stn_name = BB_code[stn_index] + " " + BB_stn[stn_index]
    elif BN_status == 1:
        stn_name = BN_code[stn_index] + " " + BN_stn[stn_index]

def stnmsg():
    global CB_status, BK_status, BB_status, BN_status, stn_index, otw_index, CB_type, BK_type, BB_type, BN_type, msg_label_top, msg_label_bottom, msg_label_temp, msg_label_dest, Line1, Line2, Line3, Line4, Line5
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
    elif BK_status == 1:
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
    elif BB_status == 1:
        if BB_type[stn_index] == "Interchange":
            if otw_index == 0:
                msg_label_top = "Stasiun berikutnya, stasiun transit"
                msg_label_bottom = BB_meg0[stn_index]
            else:
                msg_label_top = "Stasiun transit"
                msg_label_bottom = "Hati-hati melangkah. Perhatikan celah peron."
        elif BB_type[stn_index] == "Terminus":
            if otw_index == 0:
                msg_label_top = "Sesaat lagi, Anda akan tiba di stasiun tujuan akhir"
                msg_label_bottom = BB_meg0[stn_index]
            else:
                msg_label_top = "Stasiun tujuan akhir"
                msg_label_bottom = "Seluruh penumpang dimohon turun. Terima kasih telah menggunakan layanan KAI Commuter."
        else:
            if otw_index == 0:
                msg_label_top = "Stasiun berikutnya"
                msg_label_bottom = BB_meg0[stn_index]
            else:
                msg_label_top = "Stasiun"
                msg_label_bottom = "Hati-hati melangkah. Perhatikan celah peron."
    elif BN_status == 1:
        if BN_type[stn_index] == "Interchange":
            if otw_index == 0:
                msg_label_top = "Stasiun berikutnya, stasiun transit"
                msg_label_bottom = BN_meg0[stn_index]
            else:
                msg_label_top = "Stasiun transit"
                msg_label_bottom = "Hati-hati melangkah. Perhatikan celah peron."
        elif BN_type[stn_index] == "Terminus":
            if otw_index == 0:
                msg_label_top = "Sesaat lagi, Anda akan tiba di stasiun tujuan akhir"
                msg_label_bottom = BN_meg0[stn_index]
            else:
                msg_label_top = "Stasiun tujuan akhir"
                msg_label_bottom = "Seluruh penumpang dimohon turun. Terima kasih telah menggunakan layanan KAI Commuter."
        else:
            if otw_index == 0:
                msg_label_top = "Stasiun berikutnya"
                msg_label_bottom = BN_meg0[stn_index]
            else:
                msg_label_top = "Stasiun"
                msg_label_bottom = "Hati-hati melangkah. Perhatikan celah peron."

def stnswitch(com):
    global Next, Slide, Prev, DirCity, CB_status, BK_status, BB_status, BN_status, stn_index, otw_index, texttoshow, stn_name, msg_label_top, msg_label_bottom, msg_label_temp, msg_label_dest, Line1, Line2, Line3, Line4, Line5
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
        elif BK_status == 1:
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
        elif BB_status == 1:
            msg_label_temp = "Anda berada di Commuter Line Bogor."
            msg_label_dest = "Tujuan akhir, " + (BB_code[len(BB_code)-1] + " " + BB_stn[len(BB_code)-1])
            if stn_index == (len(BB_code)-1) and otw_index == 1:
                messagebox.showinfo("Attention", "This is terminus station of this line.")
            else:
                stn_index += 1
                otw_index = 0
                stnnameformat()
                stnmsg()
                DirCity = False
                if stn_index == len(BB_code)-1:
                    DirCity = True
        elif BN_status == 1:
            msg_label_temp = "Anda berada di Commuter Line Bogor."
            msg_label_dest = "Tujuan akhir, " + (BN_code[len(BN_code)-1] + " " + BN_stn[len(BN_code)-1])
            if stn_index == (len(BN_code)-1) and otw_index == 1:
                messagebox.showinfo("Attention", "This is terminus station of this line.")
            else:
                stn_index += 1
                otw_index = 0
                stnnameformat()
                stnmsg()
                DirCity = False
                if stn_index == len(BN_code)-1:
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
            elif BK_status == 1:
                msg_label_temp = "Selamat datang di LRT Jabodebek Bekasi Line."
                msg_label_dest = "Tujuan akhir, " + (BK_code[0] + " " + BK_stn[0])
                if BK_stn[stn_index] == "CAWANG":
                    msg_label_bottom += " Untuk penumpang yang akan melanjutkan ke KRL Bogor Line, mohon turun di Stasiun Transit CIKOKO."
            elif BB_status == 1:
                msg_label_temp = "Anda berada di Commuter Line Bogor."
                msg_label_dest = "Tujuan akhir, " + (BB_code[0] + " " + BB_stn[0])
            elif BN_status == 1:
                msg_label_temp = "Anda berada di Commuter Line Bogor."
                msg_label_dest = "Tujuan akhir, " + (BN_code[0] + " " + BN_stn[0])
            DirCity = True
            if stn_index == 0:
                DirCity = False
    else:
        if (otw_index == 2 and (CB_status == 1 or BK_status == 1)) or (otw_index == 1 and (BB_status == 1 or BN_status == 1)):
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
    if (otw_index == 2 and (CB_status == 1 or BK_status == 1)) or (otw_index == 1 and (BB_status == 1 or BN_status == 1)):
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

CB_start = tkt.Button(text="LRT Cibubur Line", command=lambda:[lineswitch("cb")])
BK_start = tkt.Button(text="LRT Bekasi Line", command=lambda:[lineswitch("bk")])
BB_start = tkt.Button(text="KRL Bogor Line (Bogor)", command=lambda:[lineswitch("bb")])
BN_start = tkt.Button(text="KRL Bogor Line (Nambo)", command=lambda:[lineswitch("bn")])
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
BB_start.pack()
BN_start.pack()
