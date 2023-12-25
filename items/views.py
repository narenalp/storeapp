from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from .forms import ItemForm
from .forms import AddItemForm

from .models import Items


# Create your views here
def index(request):
    item = Items.objects.all()
    context = {"item": item}
    return render(request, "items/index.html", context)


def add(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')  # Redirect to a view that lists all items
    else:
        form = AddItemForm()
    return render(request, 'items/add_item.html', {'form': form})


def edit(request, item_code):
    item = get_object_or_404(Items, pk=item_code)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list', item_code=item.ItemCode)
        else:
            form = ItemForm(instance=item)
        return render(request, 'items/edit.html', {'form': form})


def disp(request, item_code):
    item = get_object_or_404(Items, pk=item_code)
    return render(request, 'items/disp.html', {'item': item})
