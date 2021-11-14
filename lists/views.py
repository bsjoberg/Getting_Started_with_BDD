from django.shortcuts import render


def hello_world_page(request):
    return render(request, 'hello_world.html')


def home_page(request):
    return render(request, 'home.html')


def sign_up_page(request):
    return render(request, 'sign_up.html')


def application_status_page(request):
    return render(request, 'application_status.html')
