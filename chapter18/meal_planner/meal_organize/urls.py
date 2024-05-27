# الگوی یو آر ال را برای میل ارگنایز تعریف میکند
from django.urls import path

from . import views

app_name = 'meal_organize'

urlpatterns = [
    # صفحه اصلی
    path('' , views.index , name='index') ,
     # صفحه ای که تمام پیتزاها را نشان میدهد
    path('pizzas/' , views.pizzas , name= 'pizzas') ,
    # هر پیتزا را به صورت جداگانه نشان میدهد
    path('pizzas/<int:pizza_id>/' , views.pizza , name='pizza')
]