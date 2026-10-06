# Minpro-2-DDP-WatchlistAnime
## FlowChart
<img width="1429" height="2130" alt="flowchartt drawio" src="https://github.com/user-attachments/assets/770f6041-a6d8-48e9-a98f-07e05ae56639" />
jadi flowchart diawali dengan start untuk memulai, lalu ada menu yaitu
1. Memasukkan username dan password
2. keluar dari program
lanjut, jika user sudah memasukkan username dan password maka akan di cek lagi, apakah itu akun admin atau akun user, jika akun admin maka akan muncul menu admin yang terdiri dari:
1. Menu 1 = untuk menambahkan anime ke dalam watchlist 
2. Menu 2 = untuk melihat watchlist anime
3. Menu 3 = untuk menandai anime yang ada di watchlist sebagai sudah ditonton dan menambahkan ratingnya
4. Menu 4 = untuk melihat anime yang sudah ditonton dan diberi rating
5. Menu 5 = untuk mengubah rating anime yang sudah di tonton
6. Menu 6 = untuk menghapus anime yang ada di watchlist
7. Menu 7 = untuk kembali ke menu login

lalu jika login sebagai user, akan ada menu user yang terdiri dari:
1. Menu 1 = untuk melihat watchlist anime
2. Menu 2 = untuk melihat anime yang sudah ditonton dan diberi rating
3. Menu 3 = untuk kembali ke menu login

## Deskripsi Singkat
Program yang saya buat adalah watchlist anime, dimana bisa menambahkan anime ke watchlist lalu memindahkan yang di watchlist ke ditonton dan menambahkan ratingnya, lalu bisa mengubah ratingnya, dan menghapus anime yang di watchlist

## Penjelasan
### Menu Utama dan Menu Login
pertama setelah program di run akan muncul menu seperti ini, yang dimana jika memilih 1 akan masuk ke menu login, dan  jika memilih 2 akan keluar dari program
berikut outputnya:

<img width="353" height="132" alt="image" src="https://github.com/user-attachments/assets/fec11c92-ae04-41cf-993a-b45fe674044a" />
<img width="468" height="127" alt="image" src="https://github.com/user-attachments/assets/a259d062-ed6c-4b72-84c9-2d568981b7cb" />

lanjut, karena ada di program yang saya buat ada 2 role, yaitu admin dan user, jika kita login sebagai admin maka kita dapat akses penuh kedalam program (menu 1-7) sedangkan jika login sebagai user hanya bisa melihat saja (menu 1-3)
berikut outputnya

<img width="367" height="481" alt="image" src="https://github.com/user-attachments/assets/6f340bc8-967e-4f96-bf91-0078b8a8132b" />

## Login sebagai admin
Saya akan menjelaskan jika memilih nomor 1 terlebih dahulu, jika memilih nomor 1, maka akan muncul output yang menjelaskan untuk memnginput selesai jika sudah mengiput judul animenya, dan dibawahnya akan muncul untuk menyuruh user menginput judul anime nya ke dalam watchlist lalu ketika menginput judul anime itu, maka akan di output "anime di tambahkan ke watchlist" lalu jika menginput selesai, akan kemnbali ke menu utama 
berikut outputnya:

<img width="497" height="302" alt="image" src="https://github.com/user-attachments/assets/f0f8d658-e814-48bb-ad29-7aa6a2e4dbb8" />

Lanjut, jika memilih nomor 2, maka akan langsung memunculkan semua watchlist anime yang sudah di tambahkan prettytable dan akan langsung kembali ke menu 
berikut outputnya:

<img width="353" height="356" alt="image" src="https://github.com/user-attachments/assets/cf530445-3ec5-497b-a0e6-634739ab4017" />

Lanjut, jika memilih nomor 3, maka akan muncul output watchlist yang sudah di tambahkan prettytable dan sama seperti menu 1 juga, akan muncul output yang menjelaskan untuk memnginput selesai jika sudah mengiput judul animenya, dan dibawahnya akan muncul untuk menyuruh user menginput judul anime nya ke dalam ditonton lalu ketika menginput judul anime itu, maka akan lanjut disuruh untuk input ratingnya, jika ratingnya bukan angka, makan disuruh input ulang ratingnya, jika rating <1 atau >10 akan disuruh untuk input ulang, lalu jika sudah, akan muncul output "anime dipindahkan ke daftar sudah ditonton dengan rating 1-10" lalu jika meginput judul anime yang tidak ada di watchlist akan muncul output "anime tidak ada di watchlist" lalu jika menginput selesai, akan kemnbali ke menu utama 
berikut outputnya:

<img width="442" height="476" alt="image" src="https://github.com/user-attachments/assets/2ab5032b-7249-4d04-9923-96c3b5b56137" />
<img width="448" height="442" alt="image" src="https://github.com/user-attachments/assets/18ef1375-97ac-49a3-977c-716811763bb3" />

Lanjut, jika memilih nomor 4, maka akan langsung memunculkan semua anime yang sudah ditonton dan akan langsung kembali ke menu berikut outputnya:

<img width="388" height="272" alt="image" src="https://github.com/user-attachments/assets/e58bf947-fc87-44bb-be31-c9e3192d159f" />

Lanjut, jika memilih nomor 5, maka akan muncul output anime yang sudah di tonton dan di rating dan ditambahkan prettytable,dan sama seperti menu 1 dan 3 juga, akan muncul output yang menjelaskan untuk memnginput selesai jika sudah mengiput judul animenya, dan dibawwahnya akan muncul untuk menyuruh user menginput judul anime yg ingin di ubah ratingnya, jika user menginput judul yg tidak ada di dalam ditonton maka akan muncul output "anime tidak ada di daftar yang sudah ditonton.", lalu jika user menginput anime yg ada di daftar ditonton, maka akan lanjut untuk menginput rating baru, jika ratingnya bukan angka, maka disuruh input ulang ratingnya, jika rating <1 atau >10 akan disuruh untuk input ulang, lalu jika sudah, akan muncul output "Rating anime berhasil diubah menjadi 1-10", lalu jika menginput selesai, akan kemnbali ke menu utama 
berikut ouputnya:

<img width="466" height="637" alt="image" src="https://github.com/user-attachments/assets/9d337f9d-4c04-459c-b109-4e39dc442969" />

Lanjut, jika memilih nomor 6, maka akan muncul output watchlist dan sama seperti menu 1 juga, akan muncul output yang menjelaskan untuk memnginput selesai jika sudah mengiput judul animenya, lalu jika anime yg ingin dihapus ada di daftar watchlist akan muncul output "anime berhasil dihapus dari watchlist." dan jika menginput yang tidak ada di dalam di watchlist maka akan muncul output "anime tidak ditemukan di watchlist." dan jika menginput selesai, maka akan kembali ke menu 
berikut ouputnya:

<img width="541" height="692" alt="image" src="https://github.com/user-attachments/assets/132a3dcc-c00b-46c4-989e-cd1a582adb3f" />

Terakhir, jika memilih nomor 7, maka akan muncul output "exit" dan akan keluar dari menu admin dan kembali ke menu utama
berikut outputnya:

<img width="382" height="227" alt="image" src="https://github.com/user-attachments/assets/4b8e1714-cba3-4861-9fca-728457644f34" />

### Login Sebagai User
Pertama, jika memilih 1 maka akan memunculkan watchlist anime
berikut outputnya

<img width="390" height="262" alt="image" src="https://github.com/user-attachments/assets/6b0381fe-4ed0-4f19-ad52-b0b4b22662fd" />

Kedua, jika memilih 2 maka akan memunculkan list anime yang sudah ditonton dan diberi rating
berikut outputnya:

<img width="388" height="211" alt="image" src="https://github.com/user-attachments/assets/a12f08c7-2792-4c51-9a14-c28097509db9" />

Terakhir, jika memilih 3 maka akan keluar dari menu user dan kembali ke menu utama
berikut outpunya:

<img width="378" height="182" alt="image" src="https://github.com/user-attachments/assets/9e070db9-ec1d-4d1b-8ae3-9ac66e20a973" />

