from django.shortcuts import render , redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request) :
    # یک کاربر را ثبت نام موکوله
    if request.method !='POST' :
        # یک فرم خالی نشون میده
        form = UserCreationForm()
    else :
        # فرم کامل رو پردازش موکوله
        form = UserCreationForm(data = request.POST)

        if form.is_valid():
            new_user = form.save()
            # کاربر را وارد و به صفحه خانه برمیگرده
            login(request , new_user)
            return redirect('blogs:index')
    
    # یک فرم خالی یا نامعتبر می نماید
    context = {'form': form}
    return render(request, 'registration/register.html', context)