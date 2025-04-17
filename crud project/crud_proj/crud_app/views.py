from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm

def home(request):
    people = Person.objects.all()
    return render(request, 'Home.html', {'people': people})

def create_persons(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PersonForm()
    return render(request, 'create_persons.html', {'form': form})

def update_person(request, id):
    person = get_object_or_404(Person, id=id)
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'create_persons.html', {'form': form})

def delete_person(request, id):
    person = get_object_or_404(Person, id=id)
    person.delete()
    return redirect('home')
