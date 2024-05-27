# in barnameh tedade tekrare yek kalameh ra dar matn mishomarad
from pathlib import Path

def count(filename) :
        try :
                mohtava = filename.read_text()
                tedad = mohtava.count('the ')
                print (tedad)
        except FileNotFoundError :
                pass

    
masir = Path('little_women.txt')
count(masir)