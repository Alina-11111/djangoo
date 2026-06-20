from django.shortcuts import render
from django.http import HttpResponse
from app.forms import NameForm, AgeForm, ColorForm, SecretForm
from datetime import datetime

def home_page(request):
    return HttpResponse('Hello world!')


def name(request):
    name_length = None
    submitted_name = None

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            submitted_name = form.cleaned_data['name']
            name_length = len(submitted_name)
    else:
        form = NameForm()

    return render(request, 'app/lenght.html', {
        'form': form,
        'name_length': name_length,
        'submitted_name': submitted_name,
    })

def year(request):
    age = None
    submitted_name = None
    submitted_year = None
    if request.method == 'POST':
        form = AgeForm(request.POST)
        if form.is_valid():
            submitted_name = form.cleaned_data['name_user']
            submitted_year = form.cleaned_data['birth_year']
            age = datetime.now().year - submitted_year
    else:
        form = AgeForm()

    return render(request, 'app/age.html',{
        'form': form,
        'age': age,
        'submitted_name': submitted_name,
    })

def color_view(request):
    
    user_text = None
    chosen_color = None
    if request.method == 'POST':
        form = ColorForm(request.POST)
        if form.is_valid():
            user_text = form.cleaned_data['text']
            chosen_color = form.cleaned_data['color']
    else:
        form = ColorForm()
    
    return render(request, 'app/color.html', {
        'form': form,
        'user_text': user_text,
        'chosen_color': chosen_color,
    })


def password_v(request):

    #user_password = None
    succes = None
    error_message = None
    if request.method == 'POST':
        form = SecretForm(request.POST)
        if form.is_valid():
            user_password = form.cleaned_data['password']
            if user_password=='django2026':
                succes=True
            else:
                succes = False
                error_message='Ошибка'
    else:
        form = SecretForm()
    
    return render(request, 'app/password.html', {
        'form': form,
        'succes': succes,
        'error_message': error_message,
    })

# Create your views here.
