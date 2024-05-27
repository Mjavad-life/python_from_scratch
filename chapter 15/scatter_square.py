import matplotlib.pyplot as plt

# محور افقی را از 1 شروع میکند
x_values = range(1 , 1001)
y_values = [x**2 for x in x_values]

#برای پس ضمینه طرح های گوناگون دارد
plt.style.use('seaborn')

fig , ax = plt.subplots()
ax.scatter(x_values , y_values , c = y_values , cmap=plt.cm.Greens , s= 10)
# عنوان چارت را مشخص میکند
ax.set_title("square numbers" , fontsize = 24)
ax.set_xlabel("value" , fontsize = 14)
ax.set_ylabel("squre value" , fontsize = 16)
#برای هر محور محدوده مشخص میکند
ax.axis([0 , 1100 , 0 , 1_100_000])

ax.tick_params(labelsize = 14)
# چارت را ذخیره میکند
plt.savefig('plothaye_gonagon.png' , bbox_inches = 'tight')
#چارت را میکشد و نشان میدهد
#plt.show()