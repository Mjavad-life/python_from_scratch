from pathlib import Path
import json
import plotly.express as px

masir = Path('eq_data/eq_data_30_day_m1.geojson')
# وقتی انکودینگ رو مشخص نکنیم خطا میگیرد
mohtava = masir.read_text(encoding= 'utf_8')
    
all_eq_data = json.loads(mohtava)

#masir_dovom = Path('eq_data/readable_eq_data.geojson')
#mohtava_json = json.dumps(all_eq_data , indent= 4 )
#masir_dovom.write_text(mohtava_json)
# تعداد زمین لرزه ها رو مشخص میکنه
all_eq_dicts = all_eq_data['features']

# چهار لیست از ریشتر و طول و عرض و محل وقوع میسازیم
rishter , lons , lati , eq_titles = [] , [] , [] ,[]
for all_eq in all_eq_dicts :

    rishter.append(all_eq ['properties']['mag'])
    lons.append(all_eq ['geometry']['coordinates'][0])
    lati.append(all_eq ['geometry']['coordinates'][1])
    eq_titles.append(all_eq['properties']['title'])
# تیتر رو از فایل جی سان درآوردم
titr = all_eq_data['metadata']['title']
# ریشتر را به سایز گزاردم و نتیجه بزرگتر شدن نقاط با شدت بالاتر است
fig = px.scatter_geo(lat = lati , lon = lons , size = rishter , title = titr ,
                     color = rishter,
                     color_continuous_scale = 'rainbow',
                     labels = {'color':'Magnitude'},
                     projection = 'natural earth',
                      hover_name = eq_titles )
fig.write_html('30 day global earthquake.html')
fig.show()
