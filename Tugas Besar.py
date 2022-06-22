# untuk memanggil semua komponen yang ada pada tkinter agar bisa kita gunakan untuk membuat program
# tanda bintang menunjukan all atau semua artinya import semua yang ada di modul tkinter
from tkinter import *
from random import randint
#buat jendela utam
main_window = Tk()
main_window.title("Permainan Kertas Gunting Batu Asik")
# tempat untuk menyimpan program kita
main_window.iconbitmap("C:\\Users\\LENOVO\\Coding\\ALPRO TUGAS")
main_window.geometry("1050x400")
main_window.config(background="pink")

gunting = PhotoImage(file="C:\\Users\\LENOVO\\Coding\\ALPRO TUGAS\\Gunting.png")
batu = PhotoImage(file="C:\\Users\\LENOVO\\Coding\\ALPRO TUGAS\\Batu.png")
kertas = PhotoImage(file="C:\\Users\\LENOVO\\Coding\\ALPRO TUGAS\\Kertas.png")
kbg = PhotoImage(file="C:\\Users\\LENOVO\\Coding\\ALPRO TUGAS\\kbt.png")

#menampilkan gambar ketika mulai
labelpemain = Label(main_window,image=kbg)
labelkomputer = Label(main_window,image=kbg)
labelpemain.grid(row=1, column=0)
labelkomputer.grid(row=1, column=4)

# Menampilkan score, komputer dan pemain
spemain = Label(main_window, text=0,font=("calibri",60,"bold"),background="light blue",foreground= "black").grid(row=1, column=1)
skomputer = Label(main_window, text=0,font=("calibri",60,"bold"),background="light blue",foreground= "black").grid(row=1, column=3)
pemain = Label(main_window, font=("snap itc",30), text="PEMAIN" ,background="light blue", foreground= "black").grid(row=0, column=1)
komputer = Label(main_window, font=("snap itc",30), text="KOMPUTER" ,background="light blue", foreground= "black").grid(row=0, column=3)

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
        pesanupdate("Yap Hasilnya seri")
    elif p == "batu":
        if k == "kertas":
            pesanupdate("Yah Komputer menang Kamu kalah...")
            komputerupdate()
        else:
            pesanupdate("Yeay Kamu menang !!!")
            pemainupdate()
    elif p == "gunting":
        if k == "batu":
            pesanupdate("Yah Komputer menang Kamu kalah...")
            komputerupdate()
        else:
            pesanupdate("Yeay Kamu menang !!!")
            pemainupdate()
    elif p == "kertas":
        if k == "gunting":
            pesanupdate("Yah Komputer menang Kamu kalah...")
            komputerupdate()
        else:
            pesanupdate("Yeay Kamu menang !!!")
            pemainupdate()
    else:
        pass

pilihkgb = ["kertas","gunting", "batu"]
#update pilihan agar gambar yang muncul sama dengan apa yang dipilih
def pilihupdate(a):
    pilihkomputer = pilihkgb[randint(0,2)]
    if pilihkomputer == "kertas":
        labelkomputer.config(image=kertas)
    elif pilihkomputer == "gunting":
        labelkomputer.config(image=gunting)
    else:
        labelkomputer.config(image=batu)
    # a untuk user seperti yang udah ada di atas
    if a == "kertas":
        labelpemain.config(image=kertas)
    elif a == "gunting":
        labelpemain.config(image=gunting)
    else:
        labelpemain.config(image=batu)

    #cek pemenang dengan panggil fungsi
    cek_winner(a,pilihkomputer)

# menampilkan pemberitahuan
pesanfinal =  Label(main_window,font=("calibri",40,"bold"),background="purple",foreground= "black").grid(row=4, column=2)

#tombol kertas gunting batu
tbatu = Button(main_window, width= 14, height=3, text="Batu",
                font=("calibri",18,"bold"), background="light blue", foreground= "black", command=lambda:pilihupdate("batu")).grid(row=3, column=1)
tgunting = Button(main_window, width= 14, height=3, text="Gunting",
                font=("calibri",18,"bold"), background="light blue", foreground= "black", command=lambda:pilihupdate("gunting")).grid(row=3, column=2)
tkertas = Button(main_window, width= 14, height=3, text="Kertas",
                font=("calibri",18,"bold"), background="light blue", foreground= "black", command=lambda:pilihupdate("kertas")).grid(row=3, column=3)

# untuk menjalankan program yang sudah dibuat sampai program berakhir
main_window.mainloop()

