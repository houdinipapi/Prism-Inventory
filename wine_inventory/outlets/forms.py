from django import forms
from .models import Outlet, OutletWine


class OutletForm(forms.ModelForm):
    class Meta:
        model = Outlet
        fields = ["name", "location"]


class OutletWineForm(forms.ModelForm):
    class Meta:
        model = OutletWine
        fields = ["outlet", "wine", "quantity"]