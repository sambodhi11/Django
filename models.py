from django.db import models


class Event(models.Model):
    events_name=models.CharField(max_length=50)
    events_date=models.DateField()
    events_time=models.TimeField()
    events_description=models.TextField()

