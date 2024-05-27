from django.contrib import admin
# انتری و تاپیک را ایمپورت میکند
from .models import Topic , Entry

# Register your models here.

# مدل انتری و تاپیک را به صفحه ادمین اضافه میکند

admin.site.register(Topic)
admin.site.register(Entry)