from django.shortcuts import render

# Create your views here.
def platform(request):
    title = 'Главная страница'
    ref1 = 'Главная'
    ref2 = 'Магазин'
    ref3 = 'Корзина'
    context = {
        'title' : title,
        'ref1' : ref1,
        'ref2' : ref2,
        'ref3' : ref3
    }
    return render(request, 'thrid_task/platform.html', context)

def games(request):
    title = 'Магазин'
    ref1 = 'Главная'
    ref2 = 'Игры'
    ref3 = 'Купить'
    context = {
        'title' : title,
        'ref1' : ref1,
        'ref2' : ref2,
        'ref3' : ref3
    }
    return render(request, 'thrid_task/games.html', context)

def cart(request):
    title = 'Корзина'
    ref1 = 'Главная'
    context = {
        'title' : title,
        'ref1' : ref1,
    }
    return render(request, 'thrid_task/cart.html', context)
