from django.contrib.auth.models import User
from django.db import models

class MissingPerson(models.Model):
    gender_choices = (
        ('M', "Mężczyzna"),
        ('K', "Kobieta")
    )
    
    id = models.AutoField(primary_key=True)
    age = models.SmallIntegerField(blank=True, verbose_name="Wiek")
    first_name = models.CharField(max_length=50, verbose_name="Imie")
    last_name = models.CharField(max_length=50, verbose_name="Nazwisko")
    gender = models.CharField(choices=gender_choices, max_length=1, verbose_name="Płeć")
    photo = models.ImageField(default="default.png", upload_to="photos/", verbose_name="Zdjęcie")
    description = models.TextField(max_length=500, blank=True, verbose_name="Opis")
    last_seen = models.CharField(max_length=100, blank=True, verbose_name="Ostatnio widziany")
    reporting_person = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
