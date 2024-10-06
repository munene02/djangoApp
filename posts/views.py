from django.shortcuts import render

# Create your views here.
def posts_list(request):
    return render(request, 'posts/posts_list.html')

def post_detail(request, id):
    return render(request, 'posts/posts_detail.html', {'id': id})

