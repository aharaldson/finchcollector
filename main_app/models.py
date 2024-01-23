from django.db import models
from django.urls import reverse

SERVICE = (
    ('O', 'Oil Change'),
    ('T', 'Rotate Tires'),
    ('F', 'Check Fluids & Filters')
)
# Create your models here.

class Mod(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mods_detail', kwargs={'pk': self.id})

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(default=0)
    kind = models.CharField(max_length=100)
    mods = models.ManyToManyField(Mod)

    def __str__(self):
        return self.make

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})

class Service(models.Model):
    date = models.DateField()
    service = models.CharField(
        max_length=1,
        choices=SERVICE,
        default=SERVICE[0][0]
    )

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_service_display()} on {self.date}"

    class Meta:
        ordering = ['-date']