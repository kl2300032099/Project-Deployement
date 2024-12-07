from django.shortcuts import render


def base(request):
    return render(request, 'pro/base.html')

def create(request):
    return render(request, 'pro/create.html')

def event(request):
    return render(request, 'pro/event.html')

def login(request):
    return render(request, 'pro/login.html')

def pw(request):
    return render(request, 'pro/pw.html')

def about(request):
    return render(request, 'pro/about.html')

def contact(request):
    return render(request, 'pro/contact.html')

def help(request):
    return render(request, 'pro/help.html')

def reg(request):
    return render(request, 'pro/reg.html')