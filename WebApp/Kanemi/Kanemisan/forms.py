from django import forms
 
class ContactForm(forms.Form):
    things = forms.CharField(label="商品名")
    one_price = forms.IntegerField(label="1コ")
    amount = forms.IntegerField(label="数量")
    
