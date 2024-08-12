from django.shortcuts import render


def index(request):
    context = {'message': 'Hello world', 'text':'Welcome to my page. Horaaaay!'}
    # user = {'username': 'Amos', 'authenticated': True, 'items': ['rabbit', 'cats']}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')