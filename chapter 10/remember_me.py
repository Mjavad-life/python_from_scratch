from pathlib import Path
import json

karbar_esm = input(" esmet chie agha pesare gol :")
masir = Path('karbar.json')
mohtava = json.dumps(karbar_esm)
masir.write_text(mohtava)
print(f" dafeye badi be khater miavarimat {mohtava}")