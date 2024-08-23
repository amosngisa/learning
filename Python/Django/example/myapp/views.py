from django.shortcuts import render, redirect
from .models import Blog
from .models import Subscriber
from django.contrib import messages
from .forms import BlogForm




def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog_list(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog.html', context)

def subscriber(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Subscriber.objects.filter(email=email).exists():
            messages.error(request, 'You are already subscribed!')
        else:
            subscriber = Subscriber(email=email)
            subscriber.save()
            messages.success(request, 'Thank you for subscribing!')
            return redirect('subscribe')
        
    return render(request, 'subscribe.html')


def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False) 
            blog.save()  # Make sure the save method is called correctly
            return redirect('blog')
        else:
            print(form.errors)  # Print form errors if any (for debugging)
    else:
        form = BlogForm()

    return render(request, 'add_blog.html', {'form': form})