from pathlib import Path
import json

karbar_esm = input(" esmet chie agha pesare gol :")
karbar_sen = input(" chand salete agha pesar :")
karbar_ghad = input(" ghadet chande pesare golam :")
collection = {'esm':karbar_esm , 'sen' : karbar_sen , 'ghad' : karbar_ghad}
masir = Path('karbar.json')
mohtava = json.dumps(collection)
masir.write_text(mohtava)
print(f" dafeye badi be khater miavarimat {mohtava}")