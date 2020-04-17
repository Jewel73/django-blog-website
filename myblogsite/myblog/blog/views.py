from django.shortcuts import render, redirect
from .forms import PostCreate
from django.http import HttpResponse
from .models import Post


# Create your views here.
def home(request):
    first = Post.objects.first()
    posts = Post.objects.all()[:3]
    context ={'posts':posts, 'first_post': first}
    return render(request, 'blog/index.html', context)

def postCreate(request):
    form = PostCreate()

    if request.method == "POST":
        form = PostCreate(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'blog/postcreate.html', context)