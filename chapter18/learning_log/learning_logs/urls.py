# الگوهای یو آر ال را برای لرنینگ لاگز تعریف میکند

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # صفحه خانه
    path('' , views.index , name='index') ,
    # صفحه ای که تمام موضوعات را نشان میدهد
    path('topics/' , views.topics , name= 'topics') ,
    # هر صفحه را به صورت جداگانه نشان میدهد
    path('topics/<int:topic_id>' , views.topic , name='topic'),
    # صفحه ای برای اضافه کردن موضوع جدید
    path('new_topic/' , views.new_topic , name='new_topic'),
    # صفحه ای برای اضافه کردن ورودی جدید
    path('new_entry/<int:topic_id>/' , views.new_entry , 
                name='new_entry'),
    # صفحه ای برای ویرایش ورودی ها
    path('edit_entry/<int:entry_id>/' , views.edit_entry , 
                name= 'edit_entry') , 
]