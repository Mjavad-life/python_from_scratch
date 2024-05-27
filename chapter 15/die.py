from random import randint

class Die :
    # کلاسی برای ارایه یک وجه

    def __init__(self , num_sides = 6) :
        self.num_sides = num_sides

    def roll(self) :
        # یک عدد بین 1 تا تعداد وجه ها میسازد
        return randint(1 , self.num_sides)   
