from django.shortcuts import render
from .models import Pizza

# Create your views here.

def index(request) :
    # صفحه خانه برای میل پلنر
    return render(request , 'meal_organize/index.html')

def pizzas(request) :
    # همه موضوعات را نمایش میدهد
    pizzas = Pizza.objects.order_by('date_added')
    context ={'pizzas' : pizzas}
    return render(request , 'meal_organize/pizzas.html' , context)

def pizza(request , pizza_id) :
    # یک موضوع و تمام محتویاتش را نشان میدهد
    pitza = Pizza.objects.get(id = pizza_id)
    toppings1 = pitza.topping_set.get('-date_added')
    context = {'pizza' : pitza , 'toppings' : toppings1}
    return render(request , 'meal_organize/pizza.html' , context)