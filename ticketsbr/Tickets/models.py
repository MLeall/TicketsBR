from django.db import models

class Venue(models.Model):
    name = models.CharField('Venue name', max_length=250)
    address = models.CharField(max_length=350)
    zip_code = models.CharField('Zip Code', max_length=15)
    web = models.URLField('Website address')

    def __str__(self):
        return self.name


class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField('User email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    name = models.CharField('Event name', max_length=250)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE ,blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    attendees = models.ManyToManyField(Users, blank=True)

    def __str__(self):
        return self.name