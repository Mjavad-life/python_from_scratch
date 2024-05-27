from die import Die
import plotly.express as go
#import plotly.offline as iplot
#import plotly as py

#py.offline.init_notebook_mode(connected = True)
die = Die()
#چند بار تاس میریزد و نتایج را در لیست ذخیره میکند
results = []
for rool_num in range(1000) :
    natijeh = die.roll()
    results.append(natijeh)
#print (results)
title = ' charti baraye rasm bazi shish taie'
lables = {'x' : 'mehvar' , 'y' : 'tahtaghar'}
frequencies = []
adad = range(1 , die.num_sides+1)
for value in adad :
    tekrar = results.count(value)
    frequencies.append(tekrar)
#print(frequencies)

fig = go.bar(x= adad , y= frequencies , title = title )
fig.write_html('che chizaye bahaly.html')
fig.show()
