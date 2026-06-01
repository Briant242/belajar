import time
kondisi = True
sapaan = "Halo, selamat datang di program penghitung rata rata!"
time.sleep(1)
print(sapaan)
time.sleep(1)

while True:
    opsi1= input("Apakah kamu ingin menghitung rata rata? (y/n) ")
    if opsi1 == "y":
        time.sleep(1)
        value1= float(input("Masukan besar seluruh data jika dijumlahkan : "))
        value2= float(input("Masukan berapa banyak data: "))
        check1= isinstance(value1, float)
        check2= isinstance(value2, float)
        if check1 == True & check2 == True:
            print("Sedang memproses data di sistem!")
            i = 0
            for i in range(10):
                print(".")
                time.sleep(0.3)
            hasil = value1 / value2
            print(f"Hasil dari rata rata data {value1} dan {value2} adalah {hasil}")
    elif opsi1 == "n":
        break