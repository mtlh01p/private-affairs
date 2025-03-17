stat = ["Chinese Garden", "Lakeside", "Boon Lay", "Pioneer", "Joo Koon", "Gul Circle", "Tuas Crescent", "Tuas West Road", "Tuas Link"]
curr = 0
templ = ["Next station, ", "This train service will end at "]

while True:
    shower = input("Enter stn code to show: EW")
    termini = input("Enter stn termini to show: EW")
    if shower.isnumeric() and termini.isnumeric() and 25 <= int(shower) <= 33 and 25 <= int(termini) <= 33:
        s = [templ[0], "EW", str(shower), " ", stat[int(shower)-25]]
        t = [templ[1], "EW", str(termini), " ", stat[int(termini)-25]]
        print(''.join(s))
        print(''.join(t))
        print("DOORS OPENING >>>")