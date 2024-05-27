# in barname mohtaviate to file ra mikhanad va chap mikonad
from pathlib import Path

def screen(filename) :
        try :
                mohtava = filename.read_text()
                print (mohtava)
        except FileNotFoundError :
                pass

fileha = ['cats.txt' , 'dogs.txt']
for file in fileha  :
    
        masir = Path(file)
        screen(masir)
    