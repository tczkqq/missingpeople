from django.forms import ModelForm
from . import models

class AddPerson(ModelForm):
    class Meta:
        model = models.MissingPerson
        fields = [
            'first_name',
            'last_name',
            'gender',
            'photo',
            'description',
            'last_seen',
            'age'
        ]