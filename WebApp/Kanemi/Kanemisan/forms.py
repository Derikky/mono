from django import forms
from .models import Things


class ThingsForm(forms.ModelForm):
    class Meta:
        model= Things
        fields = '__all__'
        labels = {'name':'商品名', 'price': '単品価格', 'amount':'数量'}
        
    
