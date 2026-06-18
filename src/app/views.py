from django.shortcuts import render
from django.http import HttpResponse
from app.forms import NameForm

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

# Create your views here.
