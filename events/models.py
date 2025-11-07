from django.db import models

# Create your models here.
class Category(models.Model) : 
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Event(models.Model) :
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=150)
    participant_to = models.ManyToManyField("Participant", related_name="events")
    # Catgory One to one relation with Catgory
    category = models.ForeignKey(Category, null=True, blank=True, related_name="events")

    def __str__(self):
        return self.name

class Participant(models.Model) :
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name