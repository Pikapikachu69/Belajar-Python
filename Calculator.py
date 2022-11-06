angka1 = int(input("masukan angka pertama : "))
opr = input("pilih operasinya ( +, -, *, / ) : ")
angka2 = int(input("masukan angka kedua : "))

if "+" in opr :
    answer = angka1 + angka2
    print(f"Hasil dari {angka1} + {angka2} = {answer}")
if "-" in opr :
    answer = angka1 - angka2
    print(f"Hasil dari {angka1} - {angka2} = {answer}")
if "*" in opr :
    answer = angka1 * angka2
    print(f"Hasil dari {angka1} * {angka2} = {answer}")
if "/" in opr :
    answer = angka1 / angka2
    print(f"Hasil dari {angka1} / {angka2} = {answer}")