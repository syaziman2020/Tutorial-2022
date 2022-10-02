x = []


nama = input("Masukkan nama : ")

while (True):
    try:
        y = int(input("masukkan harga : "))
        if (isinstance(y, int)):
            x.append(y)
            if (len(x) == 2):
                break
    except:
        print("Terjadi kesalahan")


keuntungan = x[0] - x[1]

print("nama penjual ", nama)
print("keuntungannya adalah ", keuntungan)
