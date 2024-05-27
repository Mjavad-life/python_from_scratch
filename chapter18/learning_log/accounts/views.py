from django.shortcuts import render , redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request) :
    # یک کاربر را ثبت نام میکند
    if request.method !='POST' :
        # یک صفحه ثبت نام خالی نشون میده
        form = UserCreationForm()
    else :
        # فرم کامل رو می پردازد
        form = UserCreationForm(data = request.POST)

        if form.is_valid():
            new_user = form.save()
            # کاربر را وارد میکند و به صفحه خانه برمیگردد
            login(request , new_user)
            return redirect('learning_logs:index')
        
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)