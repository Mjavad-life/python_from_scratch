from pathlib import Path
masir=Path('alice1.txt')
try :
    mohtava=masir.read_text(encoding='utf-8')
except FileNotFoundError :
    print(" in file mojod nist")
else :
    kalameh=mohtava.split()
    shomar = len(kalameh)
    print(shomar)