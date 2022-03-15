from django.shortcuts import redirect, render, get_object_or_404
from .models import MissingPerson
from .forms import AddPerson

def home_view(request):
    persons = MissingPerson.objects.all().order_by('-created')   
    context = {
        'title': 'Strona głowna',
        'persons': persons
    }
    return render(request, 'core/home.html', context)

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
