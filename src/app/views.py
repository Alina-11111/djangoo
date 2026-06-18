from django.shortcuts import render
from django.http import HttpResponse
from app.forms import NameForm, AgeForm
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

# Create your views here.
