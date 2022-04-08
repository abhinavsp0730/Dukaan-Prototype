from django import forms 
from .models import Product, Order
from django.contrib.auth.models import User as mu

class NewProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.Textarea(attrs={'rows':1}), max_length=30)
    mrp = forms.IntegerField(widget=forms.NumberInput)
    discounted_price = forms.IntegerField(widget=forms.NumberInput) 

    class Meta:
        model = Product
        fields = ['name', 'mrp','discounted_price', 'details'] 

"""
class BuyProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(BuyProductForm, self).__init__(*args, **kwargs)
        a = [i.name for i in Product.objects.filter(User=self.request.user)]
        name = forms.ChoiceField(choices=a)
        qty = forms.IntegerField(widget=forms.NumberInput)

    class Meta:
        model = Order 
        fields = ['product_name', 'qty']
""" 
class BuyProductForm(forms.Form):
    name = forms.ChoiceField(choices=[])
    user_name = forms.CharField(widget=forms.Textarea(attrs={'rows':1}), max_length=30)
    adress = forms.CharField(widget=forms.Textarea(attrs={'rows':2}), max_length=4000)
    mobile = forms.CharField(widget=forms.Textarea(attrs={'rows':1}), max_length=10)
    qty = forms.IntegerField(widget=forms.NumberInput)
    def __init__(self, *args, **kwargs):
        self.choices = kwargs.pop("choices")
        super(BuyProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].choices = self.choices

class UpdateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.Textarea(attrs={'rows':1}), max_length=30)
    mrp = forms.IntegerField(widget=forms.NumberInput)
    discounted_price = forms.IntegerField(widget=forms.NumberInput) 

    class Meta:
        model = Product
        fields = ['name', 'mrp','discounted_price', 'details'] 
