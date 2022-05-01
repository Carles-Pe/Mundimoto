from django import forms
from .models import brands
from .models import versions


class BrandForm(forms.ModelForm):
    class Meta:
        model = brands
        fields = ["name"]
        labels = {"name": "Name"}


class VersionForm(forms.ModelForm):
    class Meta:
        model = versions
        fields = [
            "brand",
            "modelname",
            "version",
            "year",
            "km",
            "sell_price",
            "purchase_price",
        ]

        labels = {
            "brand": "Brand Name",
            "modelname": "Model Name",
            "version": "Model version",
            "year": "Production year",
            "km": "Milage [in Km]",
            "sell_price": "Sell price (Set to -1 for price pediction)",
            "purchase_price": "Purchase price (can be null)",
        }
