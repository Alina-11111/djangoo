from django import forms
from datetime import datetime


class NameForm(forms.Form):
    name = forms.CharField(
        label='Имя',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}),
    )


class AgeForm(forms.Form):
    name_user = forms.CharField(
        label = 'Имя',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}),
        
    )
    birth_year = forms.IntegerField(
        label='Год рождения',
        min_value=1900,
        max_value=datetime.now().year,
        widget=forms.NumberInput(attrs={'placeholder': 'Введите год рождения'}),
    )
