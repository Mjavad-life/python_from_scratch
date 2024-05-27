import matplotlib.pyplot as plt

# محور افقی را از 1 شروع میکند
input_value = [1 , 2 , 3 , 4 ,5]
squares = [1 , 4 , 9 , 16 , 25]

#برای پس ضمینه طرح های گوناگون دارد
plt.style.use('classic')

fig , ax = plt.subplots()
ax.plot(input_value , squares , linewidth=3)
ax.scatter(2 , 4 , s = 200)
# عنوان چارت را مشخص میکند
ax.set_title("square numbers" , fontsize = 24)
ax.set_xlabel("value" , fontsize = 14)
ax.set_ylabel("squre value" , fontsize = 16)

ax.tick_params(labelsize = 14)
plt.show()