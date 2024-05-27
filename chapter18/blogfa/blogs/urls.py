# الگوی یو ار ای را برای بلاگز طراحی میکند
from django.urls import path
from . import views
app_name = 'blogs'
urlpatterns = [
# صفحه اصلی
 path('', views.index, name='index'),
 # صفحه ای که مباحث را نشان میدهد
 path('mabahes/' , views.mabahes , name='mabahes'),
 # هر مبحث را جداگانه نشان میدهد.
path('mabahes/<int:mabhas_id>/', views.mabhas, name='mabhas'),
# صفحه ای برای اضافه کردن مبحث جدید
path('new_mabhas/' , views.new_mabhas , name='new_mabhas') ,
# صفحه ای برای اضافه کردن محتوا نو
path('new_mohtava/<int:mabhas_id>/' , views.new_mohtava ,
      name='new_mohtava') ,
 ]