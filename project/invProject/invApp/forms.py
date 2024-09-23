from django import forms
from .models import Product
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    password_confirm=forms.CharField(widget=forms.PasswordInput,label='Confirm Password')

    class Meta:
        model=User
        fields=['username','password','password_confirm']

    def  clean(self):
        cleaned_data=super().clean()
        password=cleaned_data.get("password")
        password_confirm=cleaned_data.get("password_confirm")
        if  password != password_confirm:
            raise forms.ValidationError("Password doesn't match!")
        return cleaned_data


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"
        labels={
            'product_id':'Product ID',
            'name':'Name',
            'sku':'Sku',
            'price':'Price',
            'quantity':'Quantity',
            'supplier':'Supplier',
        }
        widgets={
            'product_id':forms.NumberInput(attrs={'placeholder':'e.g 1','class':'form-control'}),
            'name':forms.TextInput(attrs={'placeholder':'e.g shirt','class':'form-control'}),
            'sku':forms.TextInput(attrs={'placeholder':'e.g S123','class':'form-control'}),
            'price':forms.NumberInput(attrs={'placeholder':'e.g 12.3','class':'form-control'}),
            'quantity':forms.NumberInput(attrs={'placeholder':'e.g 19','class':'form-control'}),
            'suppliers':forms.TextInput(attrs={'placeholder':'e.g ABC_company','class':'form-control'}),
        }

