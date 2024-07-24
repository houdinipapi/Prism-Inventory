from django.shortcuts import render, get_object_or_404, redirect
from .models import Outlet, OutletWine
from .forms import OutletForm, OutletWineForm

# Create your views here.
def outlet_list(request):
    outlets = Outlet.objects.all()
    return render(
        request,
        "outlets/outlet_list.html",
        {"outlets": outlets}
    )


def outlet_detail(request, pk):
    outlet = get_object_or_404(Outlet, pk=pk)
    outlet_wines = OutletWine.objects.filter(outlet=outlet)
    return render(
        request,
        "outlets/outlet_detail.html",
        {"outlet": outlet, "outlet_wines": outlet_wines}
    )


def outlet_create(request):
    if request.method == "POST":
        form = OutletForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("outlet_list")
    else:
        form = OutletForm()

    return render(
        request,
        "outlets/outlet_form.html",
        {"form": form}
    )


def outlet_update(request, pk):
    outlet = get_object_or_404(Outlet, pk=pk)
    if request.method == "POST":
        form = OutletForm(request.POST, instance=outlet)
        if form.is_valid():
            form.save()
            return redirect("outlet_list")
    else:
        form = OutletForm(instance=outlet)

    return render(
        request,
        "outlets/outlet_form.html",
        {"form": form}
    )


def outlet_delete(request, pk):
    outlet = get_object_or_404(Outlet, pk=pk)
    if request.method == "POST":
        outlet.delete()
        return redirect("outlet_list")

    return render(
        request,
        "outlets/outlet_confirm_delete.html",
        {"outlet": outlet}
    )


def outlet_wine_create(request, outlet_pk):
    outlet = get_object_or_404(Outlet, pk=outlet_pk)
    if request.method == "POST":
        form = OutletWineForm(request.POST)
        if form.is_valid():
            outlet_wine = form.save(commit=False)
            outlet_wine.outlet = outlet
            outlet_wine.save()
            # form.save()
            return redirect("outlet_detail", pk=outlet.pk)
    else:
        # form = OutletWineForm(initial={"outlet": outlet})
        form = OutletWineForm()

    return render(
        request,
        "outlets/outlet_wine_form.html",
        {"form": form, "outlet": outlet}
    )


def outlet_wine_update(request, outlet_pk, pk):
    outlet_wine = get_object_or_404(OutletWine, pk=pk)
    if request.method == "POST":
        form = OutletWineForm(request.POST, instance=outlet_wine)
        if form.is_valid():
            form.save()
            # return redirect("outlet_detail", pk=outlet_pk)
            return redirect("outlet_detail", pk=outlet_wine.outlet.pk)
    else:
        form = OutletWineForm(instance=outlet_wine)

    return render(
        request,
        "outlets/outlet_wine_form.html",
        {"form": form, "outlet": outlet_wine.outlet}
    )


def outlet_wine_delete(request, outlet_pk, pk):
    outlet_wine = get_object_or_404(OutletWine, pk=pk)
    if request.method == "POST":
        outlet_pk = outlet_wine.outlet.pk
        outlet_wine.delete()
        return redirect("outlet_detail", pk=outlet_pk)

    return render(
        request,
        "outlets/outlet_wine_confirm_delete.html",
        {"outlet_wine": outlet_wine}
    )