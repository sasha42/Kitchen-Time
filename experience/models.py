from django.db import models
from django.utils import timezone
import uuid

class Experience(models.Model):
    name = models.CharField(max_length=50, default="")
    location = models.CharField(max_length=50, default="")
    number = models.CharField(max_length=15, default="")
    email = models.EmailField(max_length=75, default="")
    description = models.TextField(default="")
    photo = models.CharField(max_length=250, default="")
    experience_id = models.CharField(max_length=10, default="", editable=False, primary_key=True, unique=True)
    creation_time = models.DateTimeField(default=timezone.now, blank=True)

    def __unicode__(self):
        return self.name

    def save(self):
        if not self.experience_id:
            self.experience_id = uuid.uuid1().hex[:10]
        super(Experience, self).save()