# from django.http import HttpResponse

# def homepage(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# def about(request):
#     return HttpResponse("Hello, world. You're at the polls about.")

from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
