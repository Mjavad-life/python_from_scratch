from pathlib import Path
import json

masir = Path('numbers.json')
mohtava = masir.read_text()
adadha = json.loads(mohtava)
print(adadha)