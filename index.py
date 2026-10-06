import os
import pwinput
from prettytable import PrettyTable

os.system("cls")

watchlist = ["naruto", "black clover", "kny", "jjk", "horimiya"]
ditonton = []

users = {
    "admin": {"password": "123", "role": "admin"},
    "tyon": {"password": "123", "role": "user"}
}

def login():
    username = input("Username: ")
    password = pwinput.pwinput(prompt="Password: ", mask="*")
    if username in users and users[username]["password"] == password:
        print("Login berhasil, selamat datang", username)
        return username
    else:
        print("Username atau password salah.")
        return None

def tambah_anime():
    while True:
        print("Ketik 'selesai' kalau sudah tidak ingin memasukkan watchlist lagi.")
        judul = input("masukkan judul anime: ")
        sudah_ditonton = False
        for anime in ditonton:
            if anime[0] == judul:
                sudah_ditonton = True
                break
        if judul == "selesai":
            break
        elif judul == "":
            print("judul tidak boleh kosong")
        elif sudah_ditonton:
            print("anime sudah di tonton")
        elif judul in watchlist:
            print("anime sudah ada di watchlist")
        else:
            watchlist.append(judul)
            print("anime di tambahkan ke watchlist")

def daftar_watchlist():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Judul"]
    nomor = 1
    for anime in watchlist:
        tabel.add_row([nomor, anime])
        nomor = nomor + 1
    print(tabel)

def tambah_ditonton():
    while True:
        print("daftar Watchlist:")
        daftar_watchlist()
        print("Ketik 'selesai' kalau sudah selesai.")
        anime = input("Masukkan judul anime yang sudah ditonton: ")
        if anime == "selesai":
            break
        elif anime in watchlist:
            while True:
                rating_input = input("Masukkan rating (0-10): ")
                if not rating_input.isdigit():
                    print("Rating harus berupa angka.")
                    continue
                else:
                    rating = int(rating_input)
                    if rating < 0 or rating > 10:
                        print("Rating harus antara 0 - 10.")
                    else:
                        watchlist.remove(anime)
                        ditonton.append([anime, rating])
                        print(anime, "dipindahkan ke daftar sudah ditonton dengan rating", rating)
                        break
        else:
            print(anime, "tidak ada di watchlist.")

def daftar_ditonton():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Judul", "Rating"]
    nomor = 1
    for anime in ditonton:
        tabel.add_row([nomor, anime[0], anime[1]])
        nomor = nomor + 1
    print(tabel)

def ubah_ditonton():
    if not ditonton:
        print("Belum ada anime yang selesai ditonton.")
    else:
        while True:
            print("Daftar anime yang sudah ditonton:")
            daftar_ditonton()
            print("Ketik 'selesai' kalau sudah selesai.")
            ubah = input("Masukkan judul anime yang ingin diubah ratingnya: ")
            if ubah == "selesai":
                break
            for anime in ditonton:
                if anime[0] == ubah:
                    while True:
                        rating_baru = input("Masukkan rating baru untuk " + ubah + " (0-10): ")
                        if not rating_baru.isdigit():
                            print("Rating harus berupa angka.")
                            continue
                        rating = int(rating_baru)
                        if rating < 0 or rating > 10:
                            print("Rating harus antara 0 - 10.")
                        else:
                            anime[1] = rating
                            print("Rating", ubah, "berhasil diubah menjadi", rating)
                            break
                    break
            else:
                print(ubah, "tidak ada di daftar yang sudah ditonton.")

def hapus_anime():
    while True:
        print("daftar Watchlist:")
        daftar_watchlist()
        print("Ketik 'selesai' kalau sudah tidak ingin memasukkan watchlist lagi.")
        hapus = input("Masukkan judul anime yang ingin dihapus dari watchlist: ")
        if hapus == "selesai":
            break
        elif hapus in watchlist:
            watchlist.remove(hapus)
            print(hapus, "berhasil dihapus dari watchlist.")
        else:
            print(hapus, "tidak ditemukan di watchlist.")  
def menu_admin():
    input("Tekan Enter untuk kembali...")
    while True:
        print("MENU")
        print("1. Tambah anime ke watchlist")
        print("2. Lihat watchlist")
        print("3. Tandai anime sudah ditonton + beri rating")
        print("4. Lihat daftar anime yang sudah ditonton")
        print("5. Ubah rating anime yang sudah ditonton")
        print("6. Hapus anime dari watchlist")
        print("7. Keluar")    
        menu = input("Pilih menu (1-7): ")

        if menu == "1":
            tambah_anime()
        elif menu == "2":
            daftar_watchlist()
        elif menu == "3":
            tambah_ditonton()
        elif menu == "4":
            daftar_ditonton()
        elif menu == "5":
            ubah_ditonton()
        elif menu == "6":
            hapus_anime()
        elif menu == "7":
            print("exit")
            break
        else:
            print("Pilihan tidak ada, input lagi.")

def menu_user():
    input("Tekan Enter untuk kembali...")
    while True:
        print("MENU")
        print("1. Lihat watchlist")
        print("2. Lihat daftar anime yang sudah ditonton")
        print("3. Keluar")    
        menu = input("Pilih menu (1-3): ")

        if menu == "1":
            daftar_watchlist()
        elif menu == "2":
            daftar_ditonton()
        elif menu == "3":
            print("exit")
            break
        else:
            print("Pilihan tidak ada, input lagi.")

while True:
    print("=== LOGIN WATCHLIST ANIME ===")
    print("1. Login")
    print("2. Keluar program")
    pilihan = input("Pilih (1-2): ")
    if pilihan == "1":
            username = login()
            if username:
                role = users[username]["role"]
                if role == "admin":
                    menu_admin()
                else:
                    menu_user()
    elif pilihan == "2":
            print("Program selesai.")
            break
    else:
            print("Pilihan tidak ada, input lagi.")
