import matplotlib.pyplot as plt

# محور افقی را از 1 شروع میکندو تا 5000 ادامه میدهد
x_values = range(1 , 5001)
#محور عمودی را به صورت مکعب محور افقی قرار میدهد
y_values = [x**3 for x in x_values]

#برای پس ضمینه طرح های گوناگون دارد
plt.style.use('seaborn')

fig , ax = plt.subplots()
ax.scatter(x_values , y_values , c = y_values , cmap=plt.cm.Greens , s= 10)
# عنوان چارت را مشخص میکند
ax.set_title("square numbers" , fontsize = 24)
ax.set_xlabel("value" , fontsize = 14)
ax.set_ylabel("squre value" , fontsize = 16)
#برای هر محور محدوده مشخص میکند
ax.axis([0 , 5000 , 0 , 125_000_000_000])

ax.tick_params(labelsize = 14)
# چارت را ذخیره میکند
#plt.savefig('plothaye_gonagon.png' , bbox_inches = 'tight')
#چارت را میکشد و نشان میدهد
plt.show()