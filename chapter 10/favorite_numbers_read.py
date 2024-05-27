# adadi ke karbar zakhire karde bod ra neshan midahad
from pathlib import Path
import json

masir = Path('number.json')
mohtava = masir.read_text()
adad = json.loads(mohtava)
print(f" adadi ke ghablan neveshti {adad} ast")