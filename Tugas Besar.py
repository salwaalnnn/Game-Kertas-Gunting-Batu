from tkinter import *
from random import randint
#buat jendela utama
main_window = Tk()
main_window.title("Permainan Kertas Gunting Batu Asik")
# tempat untuk menyimpan program kita
main_window.iconbitmap("C:\\Users\\LENOVO\\Coding\\ALPRO TUGAS")
main_window.config(background="pink")

gunting = PhotoImage(file="C:\\Users\\LENOVO\\Coding\\ALPRO TUGAS\\Gunting.png")
batu = PhotoImage(file="C:\\Users\\LENOVO\\Coding\\ALPRO TUGAS\\Batu.png")
kertas = PhotoImage(file="C:\\Users\\LENOVO\\Coding\\ALPRO TUGAS\\Kertas.png")
kbg = PhotoImage(file="C:\\Users\\LENOVO\\Coding\\ALPRO TUGAS\\kbt.png")

# Menampilkan tampilan utama
Judultampilan = Label(main_window, text="Suit Kertas Gunting Batu",font=("algerian",35,"bold"),background="light green", foreground= "black")
Judultampilan.grid(row=0, column=2)
spasi = Label(main_window, text=" ",font=("arial",30,"bold"),background="pink")
spasi.grid(row=1, column=2)
spemain = Label(main_window, text=0,font=("arial",60,"bold"),background="pink",foreground= "black")
spemain.grid(row=3, column=1)
skomputer = Label(main_window, text=0,font=("arial",60,"bold"),background="pink",foreground= "black")
skomputer.grid(row=3, column=3)
pemain = Label(main_window, font=("snap itc",30), text="PEMAIN" ,background="light green", foreground= "black")
pemain.grid(row=2, column=1)
komputer = Label(main_window, font=("snap itc",30), text="KOMPUTER" ,background="light green", foreground= "black")
komputer.grid(row=2, column=3)

#menampilkan gambar ketika mulai
gambarpemain = Label(main_window,image=kbg)
gambarkomputer = Label(main_window,image=kbg)
gambarpemain.grid(row=3, column=0)
gambarkomputer.grid(row=3, column=4)

# update pemberitahuan
def pesanupdate(a):
    pesanfinal['text'] = a
def komputerupdate():
    final = int(skomputer['text'])
    final += 1
    skomputer["text"] = str(final)
def pemainupdate():
    final = int(spemain['text'])
    final += 1
    spemain["text"] = str(final)

# mengecek pemenang
# p = pemain k = komputer
def cek_winner(p,k):
    if p == k :
        pesanupdate("Hasilnya seri nih! Yuk coba lagi!")
    elif p == "batu":
        if k == "kertas":
            pesanupdate("Yah Komputer menang Kamu kalah :(")
            komputerupdate()
        else:
            pesanupdate("Yeay Kamu menang horeee !!!")
            pemainupdate()
    elif p == "gunting":
        if k == "batu":
            pesanupdate("Yah Komputer menang Kamu kalah :(")
            komputerupdate()
        else:
            pesanupdate("Yeay Kamu menang horeee !!!")
            pemainupdate()
    elif p == "kertas":
        if k == "gunting":
            pesanupdate("Yah Komputer menang Kamu kalah :(")
            komputerupdate()
        else:
            pesanupdate("Yeay Kamu menang horeee !!!")
            pemainupdate()
    else:
        pass

pilihkgb = ["kertas","gunting", "batu"]
#update pilihan agar gambar yang muncul sama dengan apa yang dipilih
def pilihupdate(a):
    pilihkomputer = pilihkgb[randint(0,2)]
    if pilihkomputer == "kertas":
        gambarkomputer.config(image=kertas)
    elif pilihkomputer == "gunting":
        gambarkomputer.config(image=gunting)
    else:
        gambarkomputer.config(image=batu)
    # a untuk user seperti yang udah ada di atas
    if a == "kertas":
        gambarpemain.config(image=kertas)
    elif a == "gunting":
        gambarpemain.config(image=gunting)
    else:
        gambarpemain.config(image=batu)

    #cek pemenang dengan panggil fungsi
    cek_winner(a,pilihkomputer)

# menampilkan pemberitahuan
pesanfinal =  Label(main_window,font=("calibri",20,"bold"),background="purple",foreground= "white")
pesanfinal.grid(row=5, column=2)

#tombol kertas gunting batu
tbatu = Button(main_window, width= 14, height=3, text="Batu",
                font=("calibri",18,"bold"), background="light blue", foreground= "black", command=lambda:pilihupdate("batu")).grid(row=4, column=1)
tgunting = Button(main_window, width= 14, height=3, text="Gunting",
                font=("calibri",18,"bold"), background="light blue", foreground= "black", command=lambda:pilihupdate("gunting")).grid(row=4, column=2)
tkertas = Button(main_window, width= 14, height=3, text="Kertas",
                font=("calibri",18,"bold"), background="light blue", foreground= "black", command=lambda:pilihupdate("kertas")).grid(row=4, column=3)

# untuk menjalankan program yang sudah dibuat sampai program berakhir
main_window.mainloop()

