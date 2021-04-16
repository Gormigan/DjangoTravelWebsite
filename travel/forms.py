from travel.models import Order
from django import forms


class OrderForm(forms.ModelForm):
    first_name = forms.CharField()
    class Meta:
        model = Order
        fields = ('travel',"first_name","email","last_name","adult_count","children_count","price")