import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True :
        
    rw = RandomWalk(5_000)
    rw.fill_walk()
    # گام ها را میکشد
    plt.style.use('classic')
    fig , ax = plt.subplots(figsize = (15 , 9))
    # مسیر حرکت را به شکل خط میکشد
    #ax.plot(rw.x_values , rw.y_values , linewidth = 2)
    point_number = range(rw.num_point)
    # مسیر حرکت را به صورت نقطه نقطه به تصویر در می آورد
    ax.scatter(rw.x_values , rw.y_values , c= point_number , cmap=plt.cm.Greens ,
                edgecolors= 'none' , s= 10)
    #ax.set_aspect('equal')
    #نقطه ابتدا و انتها را مشخص میکند
    ax.scatter(0 , 0 , c='blue' , edgecolors='none' , s= 50)
    ax.scatter(rw.x_values[-1] , rw.y_values[-1] , c='red' ,
               edgecolors='none' , s= 50)
    # محورها را پاک میکند.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input( " edame bedahim ya na? (y/n): ")
    if keep_running == 'n' :
        break