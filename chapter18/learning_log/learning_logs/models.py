from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model) :
    # موضوعی که کاربر در موردش یاد میگیرد
    text = models.CharField(max_length = 200)
    text_add = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self) :
        # توضیح مدل را به صورت رشته برمیگرداند
        return self.text
    

class Entry(models.Model) :
    #چیز خاصی که در مورد یک موضوع یاد گرفته ایم
    topic = models.ForeignKey(Topic , on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta :
        verbose_name_plural = 'entries'
    def __str__(self) :
        # یک رشته ساده برمیگرداند که انتری را توضیح میدهد
       if len(self.text) > 50 :
        return f"{self.text[:50]}..."
       elif len(self.text) <50 :
          return self.text
