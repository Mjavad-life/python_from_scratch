from pathlib import Path
masir=Path('inpython.txt')
mohatava=masir.read_text()
khotot=mohatava.splitlines()
st=''
for khat in khotot :
    st +=khat
print(st)