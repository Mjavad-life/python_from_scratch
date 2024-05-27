from pathlib import Path
import json

masir = Path('number.json')
if masir.exists() :
    mohtava = masir.read_text()
    adad = json.loads(mohtava)
    print(f" adadi ke ghablan neveshti {adad} ast")
else :
        masir = Path('number.json')
        adad = input(" yek adad vared kon jonam :")
        mohtava = json.dumps(adad)
        masir.write_text(mohtava)