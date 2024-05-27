from django.shortcuts import render , redirect
from .models import Mabhas , Mohtava
from .forms import MabhasForm , MohtavaForm

# Create your views here.

def index(request) :
    # صفحه اصلی برای بلاگز
    return render(request , 'blogs/index.html')

def mabahes(request) :
    # تمام مباحث را نشان میدهد
    mabahes = Mabhas.objects.order_by('date_added')
    context = {'mabahes' : mabahes}
    return render(request , 'blogs/mabahes.html' , context)

def mabhas(request , mabhas_id) :
    # یک مبحث و تمام اطلاعات آنرا نشان میدهد
    mabhas = Mabhas.objects.get(id = mabhas_id)
    mohtavaha = mabhas.mohtava_set.order_by('-date_added')
    context = {'mabhas' : mabhas , 'mohtavaha' : mohtavaha}
    return render(request , 'blogs/mabhas.html' , context)

def new_mabhas(request) :
    # یک مبحث نو اضافه میکند
    if request.method !='POST':
        # داده ای اضافه نشده یک فرم خالی بساز
        form = MabhasForm()
    else :
        # داده را ارسال و پردازش میکند
        form = MabhasForm(data= request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:mabahes')
        
    context ={'form': form}
    return render(request , 'blogs/new_mabhas.html' , context)

def new_mohtava(request , mabhas_id) :
    # یک ورودی جدید برای مبحث اضافه میکند
    mabhas = Mabhas.objects.get(id=mabhas_id)
    if request.method !='POST' :
        # یک فرم خالی میسازد
        form = MohtavaForm()

    else :
        # داده را ارسال و پردازش میکند
        form = MohtavaForm(data=request.POST)
        if form.is_valid():
            new_mohtava = form.save(commit=False)
            new_mohtava.mabhas = mabhas
            new_mohtava.save()
            return redirect('blogs:mabhas' , mabhas_id=mabhas_id)
        
    context = {'mabhas': mabhas, 'form': form}
    return render(request, 'blogs/new_mohtava.html', 
                  context)