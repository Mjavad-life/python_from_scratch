from pathlib import Path
masir=Path('mihmanan.txt')
st = ''
while True :
    mehman = input(" name mehmane mohtaram ro benevisid :")
    if mehman == 'tamam' :
        break
    st += f"{mehman} \n"
    masir.write_text(st)
    