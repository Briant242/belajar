def kali(a,b):
    operasi= a * b
    return operasi

def cek_lulus(nilai):
    if int(nilai) >= 75:
        return "Lulus"
    else:
        return "Tidak lulus"

def nilai_akhir(benar, total):
    operasi= benar / total * 100
    hasil= cek_lulus(operasi)
    return f"Nilai: {operasi}, {hasil}" 

hasil = nilai_akhir(3, 10)
print(hasil)
