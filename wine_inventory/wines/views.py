from django.shortcuts import render, get_object_or_404, redirect
from .models import Wine
from .forms import WineForm

# Create your views here.
def wine_list(request):
    wines = Wine.objects.all()
    return render(
        request,
        'wines/wine_list.html',
        {'wines': wines}
    )


def wine_detail(request, pk):
    wine = get_object_or_404(Wine, pk=pk)
    return render(
        request,
        'wines/wine_detail.html',
        {'wine': wine}
    )


def wine_create(request):
    if request.method == "POST":
        form = WineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wine_list')
        else:
            form = WineForm()
        return render(
            request,
            'wines/wine_form.html',
            {'form': form}
        )
    

def wine_update(request, pk):
    wine = get_object_or_404(Wine, pk=pk)
    if request.method == "POST":
        form = WineForm(request.POST, instance=wine)
        if form.is_valid():
            form.save()
            # return redirect('wine_detail', pk=wine.pk)
            return redirect("wine_list")
    else:
        form = WineForm(instance=wine)
    return render(
        request,
        'wines/wine_form.html',
        {'form': form}
    )


def wine_delete(request, pk):
    wine = get_object_or_404(Wine, pk=pk)
    if request.method == "POST":
        wine.delete()
        return redirect('wine_list')
    return render(
        request,
        'wines/wine_confirm_delete.html',
        {'wine': wine}
    )
