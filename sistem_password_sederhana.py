import time

def jeda(waktu):
    time.sleep(waktu)

def header():
    print("==============================================")
    for i in range(5):
        print("==                                          ==")
    print("==             Selamat datang               ==")
    print("==   Sistem Password Sederhana oleh Jeryco  ==")
    for i in range(5):
        print("==                                          ==")
    print("==============================================")

def disclaimer():
    print("==============================================")
    for i in range(2):
        print("==                                          ==")
    print("==             Disclaimer !!!               ==")
    print("==  Sistem hanya digunakan untuk testing!   ==")
    for i in range(2):
        print("==                                          ==")
    print("==============================================")

def rules():
    print("==============================================")
    for i in range(2):
        print("==                                          ==")
    print("==                   Rules                      ==")
    print("== [1] Setidaknya password terdiri dari 8 huruf ==")
    print("== [2] Password harus memiliki symbol           ==")
    print("== [3] Password harus memiliki angka            ==")
    for i in range(2):
        print("==                                          ==")
    print("==============================================")  

symbol = ["!", "@", "#", "$", "%", "^", "&", "*", "_", "-", "?"]
angka = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

while True:
    header()
    jeda(1)
    disclaimer()

    input_password= input("Silahkan masukkan password yang anda inginkan : ")

    cek_symbol = any(s in input_password for s in symbol)
    cek_angka = any(a in input_password for a in angka)

    
    if len(input_password) < 8:
        print("Password harus terdiri dari 8 huruf atau lebih")
        continue
    elif not cek_angka and not cek_symbol:
        print("Password setidaknya memiliki 1 angka dan satu symbol di dalamnya")
        continue
    elif not cek_angka and len(input_password)<8:
        print("Password setidaknya memiliki 1 angka dan terdiri dari 8 huruf atau lebih di dalamnya")
        continue
    elif len(input_password)<8 and not cek_symbol:
        print("Password setidaknya memiliki 1 symbol dan terdiri dari 8 huruf atau lebiha di dalamnya")
    elif not cek_angka:
        print("Password setidaknya memiliki 1 angka di dalamnya")
        continue
    elif not cek_symbol:
        print("Password setidaknya memiliki 1 symbol di dalamya")
        continue
    elif len(input_password) >= 8 and cek_angka and cek_angka:
        print("Password berhasil dibuat!")
        jeda(1)
        break

    jeda(2)