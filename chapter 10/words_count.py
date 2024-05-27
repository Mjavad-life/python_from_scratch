from pathlib import Path

def shomareshgar(masir) :
    # tedad kalemate yek matn ra mishomarad
    try :
        mohtava=masir.read_text(encoding='utf-8')
    except FileNotFoundError :
        print(" hamchin fily mojod nist")
    else :
        kalemat = mohtava.split()
        tedad = len(kalemat)
        print(f"kalemate mojod dar {masir} , hododan be tedade {tedad} ast .")

masirha=['alice.txt','little_women1.txt','romeo_joliet.txt'
            ,'room_with_view.txt']
for masir1 in masirha :

    path = Path(masir1)
    shomareshgar(path)
