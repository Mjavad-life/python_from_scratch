# yel adad az karbar migirad va be sorat json zakhire mikonad
from pathlib import Path
import json

masir = Path('number.json')
adad = input(" yek adad vared kon jonam :")
mohtava = json.dumps(adad)
masir.write_text(mohtava)