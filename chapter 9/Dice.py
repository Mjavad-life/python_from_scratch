from random import randint
class Die :
    def __init__(self ) :
        self.sides = 6

    def roll_die(self) :
        adad=randint(1 , self.sides)
        if adad == 6 :
             print(adad)

diedie=Die()
diedie.sides = 20
n=10
while n > 0 :
    diedie.roll_die()
    n-=1