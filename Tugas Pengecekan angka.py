
confirm = input("Mengecek angka ? ").lower()

while "y" in confirm :
    
    angka = int(input("Masukan angka : "))
    if angka % 2 == 1   :   print(f"{angka} Nilai nya Ganjil")
    elif angka == 0     :   print(F"{angka} Nilai nya Netral")
    else :
        print(f"{angka} Nilai nya Genap")
    confirm = input("Mengecek angka lagi ? ").lower()

print("Akhir dari Program")
