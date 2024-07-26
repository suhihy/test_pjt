from django.shortcuts import render
import random
from faker import Faker
from faker_food import FoodProvider

# Create your views here.

def root(request):
    return render(request, 'root.html')

def index(request):
    return render(request, 'index.html')

def lotto(request):

    ran_num = sorted(random.sample(range(1, 46), 6))

    context = {
        'ran_num': ran_num,
    }

    return render(request, 'lotto.html', context)

def lunch(request):
    fake = Faker()
    fake.add_provider(FoodProvider)

    fake_name = fake.name()

    menus = ['김밥', '떡볶이', '라면', '우동', '다이어트']

    food = random.choice(menus)

    fake_dish1 = fake.dish()
    fake_dish2 = fake.dish()
    fake_dish3 = fake.dish()

    context = {
        'fake_name': fake_name,
        'fake_dish1': fake_dish1,
        'fake_dish2': fake_dish2,
        'fake_dish3': fake_dish3,
        'food': food,
    }


    return render(request, 'lunch.html', context)

def cube(request, number):
    result = number ** 3

    context = {
        'result': result,
    }
    
    return render(request, 'cube.html', context)

def posts(request):
    fake = Faker()

    fake_posts = []

    for i in range(40):
        fake_posts.append(fake.text())

    context = {
        'fake_posts': fake_posts,
    }

    return render(request, 'posts.html', context)