from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

masir = Path('weather_data/death_valley_2021_simple.csv')
khotot = masir.read_text().splitlines()

reader = csv.reader(khotot)
header_row = next(reader)
#لیستی برای ذخیره درجه دما
highs , lows , dates = [] , [] , []
for row in reader :
    tarikh = datetime.strptime(row[2] , '%Y-%m-%d')
    try : 
        max_dama = int(row[3])
        min_dama = int(row[4])
    except ValueError:
        print(f" moshkel dar tarikh {tarikh}")
    else :
        lows.append(min_dama)
        highs.append(max_dama)
        dates.append(tarikh)