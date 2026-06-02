import time

def header():
    print("==============================================")
    for i in range(5):
        print("==                                          ==")
    print("==             Selamat datang               ==")
    print("==      Konversi Celcius oleh Jeryco        ==")
    for i in range(5):
        print("==                                          ==")
    print("==============================================")

def farenheit(celcius):
    hasil = 9 / 5 * celcius + 32
    return hasil

def reamur(celcius):
    hasil = 4 / 5 * celcius
    return hasil

def kelvin(celcius):
    hasil = celcius + 273
    return hasil

def jeda():
    time.sleep(1)

while True:
    header()
    jeda()
    print("Silahkan pilih ingin mengubah satuan celcius ke satuan apa?")
    print("[1] Farenheit") 
    print("[2] Reamur")
    print("[3] Kelvin")
    print("[4] Keluar program")
    pilihan1 = int(input("Pilih nomor menu : "))
    if pilihan1 == 1:
        jeda()
        nilai_celcius= float(input("Masukan besar nilai Celcius yang akan di konversi (0 - 100) : "))
        hasil_konversi= farenheit(nilai_celcius)
        print(hasil_konversi)
        jeda()
    elif pilihan1 == 2:
        jeda()
        nilai_celcius= float(input("Masukan besar nilai Celcius yang akan di konversi (0 - 100) : "))
        hasil_konversi= reamur(nilai_celcius)
        print(hasil_konversi)
        jeda()
    elif pilihan1 == 3:
        jeda()
        nilai_celcius = float(input("Masukan besar nilai Celcius yang akan di konversi (0 - 100) : "))
        hasil_konversi= kelvin(nilai_celcius)
        print(hasil_konversi) 
        jeda()
    elif pilihan1 == 4:
        jeda()
        print("Terimakasih sudah menggunakan program konversi celcius oleh Jeryco")
        jeda()
        break     
        