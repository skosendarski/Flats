from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=30)

    def __str__(self):
        return self.city_name

STATUS_CHOICES = (
    ('a', 'available'),
    ('n', 'not available'),
)


class Flat(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    postcode = models.CharField(max_length=6)
    street = models.CharField(max_length=100)
    number_of_building = models.CharField(max_length=10)
    number_of_flat = models.CharField(max_length=10)
    available_from = models.DateField('available from')
    available_to = models.DateField('available to')
    rented_from = models.DateField('rented from', blank=True, null=True)
    rented_to = models.DateField('rented to', blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    nickname = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "%s %s %s / %s" % (self.city.city_name, self.street, self.number_of_building, self.number_of_flat)


# Create your models here.
