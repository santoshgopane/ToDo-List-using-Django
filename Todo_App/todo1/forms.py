from django import forms
from .models import List

class Listform(forms.ModelForm):
    class Meta:
        model = List
        # fields = ['item','user']
        fields = '__all__'
# class Regform(forms.ModelForm):
#     class Meta:
#         model = Register
#         fields = '__all__'