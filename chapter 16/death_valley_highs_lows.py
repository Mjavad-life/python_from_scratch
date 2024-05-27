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
        print(f" moshkel dar tarikh ")
    else :
        lows.append(min_dama)
        highs.append(max_dama)
        dates.append(tarikh)

# اطلاعات جدول را میکشد
plt.style.use('seaborn')
fig , ax = plt.subplots()
#حداکثر دما را میکشد
ax.plot(dates , highs , color ='green' , alpha = 0.5)
#حداقل دما را میکشد
ax.plot(dates , lows , color ='red' , alpha = 0.5)
#فاصله بین دو نمودار را سایه میزند
ax.fill_between(dates , lows , highs , facecolor = 'blue' , alpha = 0.1)
ax.set_title(" death valley max and min temperature" , fontsize = 24)
ax.set_xlabel('daily high and low temperature 2021' , fontsize = 16)
#برای اینکه محور افقی تو هم نره
fig.autofmt_xdate()
ax.set_ylabel("temperature" , fontsize = 16)
ax.tick_params(labelsize = 16)

plt.show()
