from django.db import models

# Create your models here.

class Mabhas(models.Model) :
    # موضوعی که کاربر در موردش یاد میگیرد
    text = models.CharField(max_length= 300)
    date_added = models.DateTimeField(auto_now_add= True)

    def __str__(self) :
        return self.text
    
class Mohtava(models.Model) :
    # چیز خاصی که در مورد موضوع یاد گرفته شده
    mabhas = models.ForeignKey(Mabhas , on_delete=models.CASCADE)
    text = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now_add= True)

    class Meta :
        verbose_name_plural = 'mohtavas'

    def __str__(self) :
        return f"{self.text[:50]}..."
