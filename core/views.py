import re
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from .models import MissingPerson
from .forms import AddPerson


def home_view(request):
    persons = MissingPerson.objects.all().order_by('-created')   
    context = {
        'title': 'Strona głowna',
        'persons': persons
    }
    return render(request, 'core/home.html', context)


@login_required
def create_view(request):
    if request.method == "POST":
        form = AddPerson(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.reporting_person = request.user
            instance.save()
            return redirect('core:home')
    else:
        form = AddPerson()
    
    context = {
        'title': 'Dodaj osobę', 
        'form': form
    }
    return render(request, 'core/create.html', context)


@login_required
def submited_view(request):
    persons = MissingPerson.objects.filter(
        reporting_person=request.user).order_by('-created')
    context = {
        'title': 'Dodaj osobę',
        'persons': persons
    }
    return render(request, 'core/submited.html', context)


def detail_view(request, id):
    person = get_object_or_404(MissingPerson, id=id)
    context = {
        'title': 'Strona głowna',
        'person': person
    }
    return render(request, 'core/detail.html', context)


def get_persons_ajax(request):        
    persons = MissingPerson.objects.all().order_by('-created')
    if 'gender' in request.GET: 
        persons = persons.filter(gender=request.GET['gender'])
        
    if 'fill_from' in request.GET:
        persons = persons.filter(age__gte=request.GET['fill_from'])
        
    if 'fill_to' in request.GET:
        persons = persons.filter(age__lte=request.GET['fill_to'])

    serialized_persons = serializers.serialize('json', persons)
    return HttpResponse(serialized_persons, content_type="application/json")


@login_required
def delete_person(request, id):
    person = get_object_or_404(MissingPerson, id=id)
    
    if (request.user.is_superuser) or (person.reporting_person == request.user):
        person.delete()
    return redirect('core:home')
