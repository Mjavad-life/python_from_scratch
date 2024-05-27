from pathlib import Path
import json

adadha = [1, 2, 3, 4, 5, 6, 7]
masir = Path('numbers.json')
mohtava = json.dumps(adadha)
masir.write_text(mohtava)