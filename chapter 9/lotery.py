from random import choice

from Dice import Die 

liste_shans=['a' , 'b' , 'c' , 'd' , 1 , 2 , 3 , 4 , 5 , 6]
tekrar = 1
shomareye_man = 2

while True :
    choose=choice(liste_shans)
    tekrar += 1
    if choose == 2 :
        print(f" {choose} barande shode ast")
        print(f" tedad tekrar {tekrar} martabe bode ast")
        break
    