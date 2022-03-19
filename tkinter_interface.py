from tkinter import *


dastur=Tk()
dastur.title("Sotuvchi")
dastur.geometry("810x400")
dastur.resizable(False, False)
dastur.configure(bg="#72ba59")

qidirish = Button(text="Qidirish", bg="#c2beb4", font=("Helvetica", 10))
qidirish.place(x=40, y=15, width=90, height=60)
hisobot = Button(text="Hisobot", bg="#c2beb4", font=("Helvetica", 10))
hisobot.place(x=140, y=15, width=90, height=60)
saralash = Button(text="Saralash", bg="#c2beb4", font=("Helvetica", 10))
saralash.place(x=240, y=15, width=90, height=60)
kalkulyator = Button(text="Kalkulyator", bg="#c2beb4", font=("Helvetica", 10))
kalkulyator.place(x=340, y=15, width=90, height=60) 

shaxsi = Label(text="Rahmatullayev Jasur", width=18, bg="#c2beb4", font=("Helvetica", 10))
shaxsi.place(x=635, y=20)
lavozim = Label(text="Sotuvchi", width=18, bg="#c2beb4", font=("Helvetica", 10))
lavozim.place(x=635, y=45)

malumot_kiritish = Text(width=49, height=3, font=("Helvetica", 12))
malumot_kiritish.place(x=40, y=100)

malumot = Label(text="", width=40, height=14, bg="#d6d1c5")
malumot.place(x=500, y=100)
natija = Label(text="", width=40, height=4)
natija.place(x=500, y=317)

kop_sotiladigan_tovar1 = Button(text="Ko'p\n sotiladigan\n tovar", bg="#c2beb4", font=("Helvetica", 10))
kop_sotiladigan_tovar1.place(x=40, y=180, width=90, height=60)
kop_sotiladigan_tovar2 = Button(text="Ko'p\n sotiladigan\n tovar", bg="#c2beb4", font=("Helvetica", 10))
kop_sotiladigan_tovar2.place(x=140, y=180, width=90, height=60)
kop_sotiladigan_tovar3 = Button(text="Ko'p\n sotiladigan\n tovar", bg="#c2beb4", font=("Helvetica", 10))
kop_sotiladigan_tovar3.place(x=40, y=252, width=90, height=60)
kop_sotiladigan_tovar4 = Button(text="Ko'p\n sotiladigan\n tovar", bg="#c2beb4", font=("Helvetica", 10))
kop_sotiladigan_tovar4.place(x=140, y=252, width=90, height=60)
kop_sotiladigan_tovar5 = Button(text="Ko'p\n sotiladigan\n tovar", bg="#c2beb4", font=("Helvetica", 10))
kop_sotiladigan_tovar5.place(x=40, y=324, width=90, height=60)
kop_sotiladigan_tovar6 = Button(text="Ko'p\n sotiladigan\n tovar", bg="#c2beb4", font=("Helvetica", 10))
kop_sotiladigan_tovar6.place(x=140, y=324, width=90, height=60)


qaytarib_olish = Button(text="Qaytarib olish", bg="#c2beb4", font=("Helvetica", 16))
qaytarib_olish.place(x=240, y=180, width=245, height=40)
ochirish = Button(text="O'chirish", bg="#c2beb4", font=("Helvetica", 16))
ochirish.place(x=240, y=224, width=245, height=40)
nomsiz = Button(text="", bg="#c2beb4")
nomsiz.place(x=240, y=268, width=245, height=50)
sotish = Button(text="Sotish", bg="#c2beb4", font=("Helvetica", 20))
sotish.place(x=240, y=324, width=245, height=60)





dastur.mainloop()