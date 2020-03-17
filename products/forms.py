from django import forms
from .models import Product

class ProductsForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['name','description','original_item_cost','instant_buy_price','reserved_buy_price','image','series','character']

    def clean_data(self):
        name = self.cleaned_data.get('name')
        description = self.cleaned_data.get('description')
        instant_buy_price = self.cleaned_data.get('instant_buy_price')
        original_item_cost = self.cleaned_data.get('original_item_cost')
        reserved_buy_price = self.cleaned_data.get('reserved_buy_price')
        image = self.cleaned_data.get('image')
        series = self.cleaned_data.get('series')
        character = self.cleaned_data.get('character')

        if Product.objects.filter(name=name).exclude(name=name):
            raise forms.ValidationError(u'Products must be unique.')
        return name