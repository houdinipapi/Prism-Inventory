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
