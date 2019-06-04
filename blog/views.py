from django.shortcuts import render, get_object_or_404
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
    form = PoatForm()
    return render(request, 'blog/post_edit.html', {'form': form})

