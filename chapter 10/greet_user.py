from pathlib import Path
import json

masir = Path('karbar.json')
mohtava = masir.read_text()
karbar = json.loads(mohtava)
print (f" salam {karbar} to ghablan esmet ro neveshte bodi")