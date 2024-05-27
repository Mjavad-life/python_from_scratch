from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic , Entry
from .forms import TopicForm , EntryForm
# Create your views here.

def index(request) :
    # صفحه خانه برای لرنینگ لاگز
    return render(request , 'learning_logs/index.html')

@login_required
def topics(request) :
    # همه موضوعات را نمایش میدهد
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context ={'topics' : topics}
    return render(request , 'learning_logs/topics.html' , context)

@login_required
def topic(request , topic_id) :
    # یک موضوع و تمام محتویاتش را نشان میدهد
    topic = Topic.objects.get(id = topic_id)
    # مطمئن میشویم که موضوع به کاربر فعلی متعلق است
    if topic.owner !=request.user:
        raise Http404
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic' : topic , 'entries' : entries}
    return render(request , 'learning_logs/topic.html' , context)

@login_required
def new_topic(request) :
    # یک موضوع اضافه میکند
    if request.method !='POST' :
        # داده ای اضافه نشده پس یک فرم خالی میسازد
        form = TopicForm()
    else :
        # داده اضافه شده را پست میکند و پردازشش میکند
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # یک فرم نامعتبر یا خالی را نمایش میدهد
    context ={'form' : form}
    return render(request , 'learning_logs/new_topic.html'
                    , context)

@login_required
def new_entry(request , topic_id) :
    # یک ورودی جدید به موضوعی خاص تضتفه میکند
    topic = Topic.objects.get(id = topic_id)

    if request.method!='POST' :
        # داده ای اضافه نشده پس فرم خالی مسازد
        form = EntryForm()
    else :
        # داده اضافه شده را پست و پردازش میکند
        form = EntryForm(data= request.POST)
        if form.is_valid() :
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic' , 
                            topic_id = topic_id)
        
    # یک فرم نامعتبر یا خالی نمایش میدهد
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', 
                  context)

@login_required
def edit_entry(request , entry_id) :
    # ورودی موجود را ویرایش میکند
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic

    if request.method !='POST':
        #فرم را با ورودی فعلی پر کن
        form = EntryForm(instance = entry)
    else :
        #  ورودی را پردازش و پست میکند
        form  = EntryForm(instance =entry , data = request.POST)
        if form.is_valid() :
            form.save()
            return redirect('learning_logs:topic' , 
                            topic_id = topic.id)
        
    context = {'entry' : entry , 'topic' : topic , 'form' : form}
    return render(request , 'learning_logs/edit_entry.html' , context)