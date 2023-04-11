from django.db import models

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class MyClubUser(models.Model): # registration form 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField('User email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Event(models.Model):
    name = models.CharField('Event Name',max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue,blank=True,null=True,on_delete=models.CASCADE)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)

    def __str__(self):
        return 
