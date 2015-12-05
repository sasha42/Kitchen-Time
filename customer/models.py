from django.db import models
from experience.models import Experience
from django.utils import timezone
import uuid

class Customer(models.Model):
    first_name = models.CharField("first name", max_length=30, default="")
    last_name = models.CharField(max_length=30, default="")
    number = models.CharField(max_length=15, default="")
    email = models.EmailField(max_length=75, default="")
    reason = models.TextField(default="")
    experience = models.ForeignKey(Experience, verbose_name='Experience')
    denial = models.BooleanField(default="0")
    experience_time = models.DateTimeField(blank=True)
    customer_id = models.CharField(max_length=10, default="", editable=False, primary_key=True, unique=True)
    submission_time = models.DateTimeField(default=timezone.now, blank=True)

    def save(self):
        if not self.order_key:
            self.order_key = uuid.uuid1().hex[:10]
        super(Order, self).save()

    def __unicode__(self):
        return self.first_name + " " + self.last_name
