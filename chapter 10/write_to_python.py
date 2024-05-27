from pathlib import Path
masir=Path('writeinpy.txt')
mohtava=" ey dokhtar gol forosh \n"
mohtava += " golo arzon naforosh \n"
mohtava += " man khodam baghebonam \n"
mohtava += " ghadre gol ro midinam "
masir.write_text(mohtava)