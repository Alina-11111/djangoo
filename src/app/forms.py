from django import forms
from datetime import datetime
from app.models import Customer


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

class ColorForm(forms.Form):

    text = forms.CharField(
    label = 'Текст',
    max_length=200,
    widget=forms.TextInput(attrs={'placeholder': 'Введите любую фразу'}),
    )

    COLOR_CHOICES = [
        ('red', 'Красный'),
        ('green', 'Зеленый'),
        ('blue', 'Синий'),
        ('purple', 'Фиолетовый'),
        ('orange', 'Оранжевый'),
    ]

    color = forms.ChoiceField(
        label='Выберите цвет',
        choices=COLOR_CHOICES
    )

class SecretForm(forms.Form):

    password = forms.CharField(
    label = 'Пароль',
    max_length=100,
    widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}),
    )

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname', 'age', 'profession']
    