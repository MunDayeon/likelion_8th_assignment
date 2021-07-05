from django.shortcuts import render, get_object_or_404, redirect
from .models import Crudeapp
from .forms import PostForm

# Create your views here.
def home(request):
    crudeapps = Crudeapp.objects
    return render(request, 'home.html', {'crudeapps' : crudeapps})

def detail(request, crudeapp_id):
    crudeapp_detail = get_object_or_404(Crudeapp, pk = crudeapp_id)
    return render(request, 'detail.html', {'crudeapp':crudeapp_detail})

def new(request):
    return render(request, 'new.html')

def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = PostForm()
        return render(request, 'new.html', {'form':form})

def edit(request):
    return render(request, 'edit.html')

def postupdate(request, crudeapp_id):
    post = get_object_or_404(Crudeapp, pk=crudeapp_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            return redirect('detail', crudeapp_id=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'edit.html', {'form':form})

def postdelete(request, crudeapp_id):
    post = get_object_or_404(Crudeapp, pk=crudeapp_id)
    post.delete()
    return redirect('home')