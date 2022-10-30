from django.db import models
import uuid

# Create your models here.

class Person(models.Model):
    # alias = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Person, related_name="patient_for_appointment", on_delete=models.CASCADE)
    data = models.CharField(max_length=20)


class Sales(models.Model):
    customer = models.ForeignKey(Appointment, related_name="customer_for_sales", on_delete=models.CASCADE)
    amount = models.FloatField()
