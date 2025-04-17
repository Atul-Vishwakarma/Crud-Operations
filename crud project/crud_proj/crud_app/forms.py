from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'name',
            'email',
            'phone',
            'address',
            'skills',
            'experience',
            'qualification',
            'college',
            'current_company',
            'notice_period',
            'expected_salary',
            'resume',
        ]
