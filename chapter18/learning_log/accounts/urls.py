# الگوهای یو آر ال را برای اکانتس طراحی میکند

from django.urls import path , include

from .import views

app_name = 'accounts'
urlpatterns = [
    # شامل یو آر ال پیش فرض اعتبار سنجی است
    path('' , include('django.contrib.auth.urls')) ,
    # صفحه ثبت نام
    path('register/' , views.register , name='register') ,
]