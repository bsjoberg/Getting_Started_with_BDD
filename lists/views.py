from django.shortcuts import render


def hello_world_page(request):
    return render(request, 'hello_world.html')


# Create your views here.
def home_page(request):
    return render(request, 'home.html')

