from django.shortcuts import render

# Create your views here.
def users_list(request):
    return render(request, 'users/users_list.html')

def register(request):
    return render(request, 'users/register.html')
