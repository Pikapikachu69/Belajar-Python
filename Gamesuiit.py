# membuat gamesuit

import random
rand = random.randrange(0, 11)
confirm = input("Maukah kau bermain ? \n")
while "y" in confirm :

    player = input("Masukan (Batu, Gunting atau Kertas) :\n").lower()
    if rand >= 0 and rand <= 3 : 
        computer = "Batu"
        if "gunting" in player : print(f"aku {computer} dan kamu {player} maka aku menang")
        elif "kertas" in player : print(f"aku {computer} dan kamu {player} maka kamu menang")
        elif "batu" in player : print(f"aku {computer} dan kamu {player} maka kita seri yah")
    elif rand >= 4 and rand <= 7   :
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

print("AKHIR DARI PROGRAM")
