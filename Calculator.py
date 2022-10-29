
# angka1 = int(input("masukan angka pertama : "))
# opr = input("pilih operasinya ( +, -, *, / ) : ")
# angka2 = int(input("masukan angka kedua : "))

# if "+" in opr :
#     answer = angka1 + angka2
#     print(f"Hasil dari {angka1} + {angka2} = {answer}")
# if "-" in opr :
#     answer = angka1 - angka2
#     print(f"Hasil dari {angka1} - {angka2} = {answer}")
# if "*" in opr :
#     answer = angka1 * angka2
#     print(f"Hasil dari {angka1} * {angka2} = {answer}")
# if "/" in opr :
#     answer = angka1 / angka2
#     print(f"Hasil dari {angka1} / {angka2} = {answer}")
import random
rand = random.randrange(0, 11)
confirm = input("Maukah kau bermain ? \n")
while confirm == "ya" :

    player = input("Masukan (Batu, Gunting atau Kertas) :\n").lower()
    if rand >= 0 and rand <= 3 :
        computer = "Batu"
        if "gunting" in player : print(f"aku {computer} dan kamu {player} maka aku menang")
        elif "kertas" in player : print(f"aku {computer} dan kamu {player} maka kamu menang")
        elif "batu" in player : print(f"aku {computer} dan kamu {player} maka kita seri yah")
        
    elif rand > 3 and rand <= 7   :
        computer = "Gunting"
        if "batu" in player : print(f"aku {computer} dan kamu {player} maka kamu menang ")
        elif "kertas" in player : print(f"aku {computer} dan kamu {player} maka aku menang")
        elif "gunting" in player : print(f"aku {computer} dan kamu {player} maka kita seri yah")
    else :
        computer = "Kertas"
        if "gunting" in player : print(f"aku {computer} dan kamu {player} maka kamu menang ")
        elif "batu" in player : print(f"aku {computer} dan kamu {player} maka aku menang")
        elif "kertas" in player : print(f"aku {computer} dan kamu {player} maka kita seri yah")
confirm = input("Kamu ingin bermain lagi ? \n")

print("MAKASEH WAKTUNYA")
