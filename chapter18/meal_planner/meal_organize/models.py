from django.db import models

# Create your models here.

class Pizza(models.Model) :
    # موضوعی که کاربر در موردش یاد میگیرد
    text = models.CharField(max_length = 200)
    #text_add = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self) :
        # توضیح مدل را به صورت رشته برمیگرداند
        return self.text
    

class Topping(models.Model) :
    #چیز خاصی که در مورد یک موضوع یاد گرفته ایم
    pizza = models.ForeignKey(Pizza , on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta :
        verbose_name_plural = 'toppings'
    def __str__(self) :
        # یک رشته ساده برمیگرداند که انتری را توضیح میدهد
       if len(self.text) > 50 :
        return f"{self.text[:50]}..."
       elif len(self.text) <50 :
          return self.text
