from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

masir = Path('weather_data/sitka_weather_2021_simple.csv')
khotot = masir.read_text().splitlines()

reader = csv.reader(khotot)
header_row = next(reader)
#لیستی برای ذخیره درجه دما
highs , dates = [] , []
for row in reader :
    tarikh = datetime.strptime(row[2] , '%Y-%m-%d')
    max_dama = int(row[4])
    highs.append(max_dama)
    dates.append(tarikh)

# اطلاعات جدول را میکشد
plt.style.use('seaborn')
fig , ax = plt.subplots()
ax.plot(dates , highs , color ='green')
ax.set_title("max temperature" , fontsize = 24)
ax.set_xlabel('daily high temperature 2021' , fontsize = 16)
#برای اینکه محور افقی تو هم نره
fig.autofmt_xdate()
ax.set_ylabel("temperature" , fontsize = 16)
ax.tick_params(labelsize = 16)

plt.show()
