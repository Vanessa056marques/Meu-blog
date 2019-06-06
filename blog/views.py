from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Poat
from .forms import PoatForm

# Create your views here.


def post_list(request):
    posts = Poat.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})



def poat_detail(request, pk):
    poat = get_object_or_404(Poat, pk=pk)
    return  render(request, 'blog/post_detail.html', {'poat': poat})

def poat_new(request):
    if request.method == "POST":
        form = PoatForm(request.POST)
        if form.is_valid():
            poat = form.save(commit=False)
            poat.authot = request.user
            poat.published_date = timezone.now()
            poat.save()
        return redirect('poat_detail', pk=poat.pk)
    else:
            form = PoatForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def poat_edit(request, pk):
    poat = get_object_or_404(Poat, pk=pk)
    if request.method == "POST":
        form = PoatForm(request.POST, instance=poat)
        if form.is_valid():
            poat = form.save(commit=False)
            poat.authot = request.user
            poat.published_date = timezone.now()
            poat.save()
            return redirect('poat_detail', pk=poat.pk)
    else:
        form = PoatForm(instance=poat)
    return render(request, 'blog/post_edit.html', {'form': form})

