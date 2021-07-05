from django import forms
from .models import Crudeapp

class PostForm(forms.ModelForm):
    class Meta:
        model = Crudeapp
        fields = ['title', 'body', 'pub_date']
        widgets = {
            'pub_date' : forms.DateInput(
                attrs = {
                    'class' : 'form-control',
                    'type' : 'date'
                }
            )
        }