from die import Die
import plotly.express as go
#import plotly.offline as iplot
#import plotly as py

# 2 بار تاس میریزد
die_1 = Die()
die_2 = Die()
#چند بار تاس میریزد و نتایج را در لیست ذخیره میکند
results = []
for rool_num in range(1000) :
    natijeh = die_1.roll() * die_2.roll()
    results.append(natijeh)
# تیتر چارت را مشخص میکند
title = ' charti baraye rasm bazi shish taie vaghti 2 ta tas mirizim'
# برای هر محور برچسب میگذارد ولی کار نکرد
lables = {'x' : 'mehvar' , 'y' : 'tahtaghar'}
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
adad = range(2 , max_result+1)
for value in adad :
    tekrar = results.count(value)
    frequencies.append(tekrar)
#print(frequencies)
# یک چارت میکشد
fig = go.bar(x= adad , y= frequencies , title = title  )
#fig.update_layout()
# چارت را به صورت html  ذخیره میکند
fig.write_html('2 ta tase 6 taee rikhtim zarb kardim dah ham.html')
#چارت را در مرورگر میکشد که بعضی وقتا نمایش نمیدهد
fig.show()