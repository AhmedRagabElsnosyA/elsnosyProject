from django.db import models

# Create your models here.


class Clients(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11, blank=True)
    address = models.CharField(max_length=200, blank=True)
    date = models.DateField()
    doctor = models.CharField(max_length=100)
    # type_of_glass = models.CharField(max_length=100, blank=True)
    # type_of_lenses = models.CharField(max_length=100)
    # price = models.DecimalField(max_digits=10, decimal_places=0)
    # paid_up = models.DecimalField(max_digits=10, decimal_places=0)
    # residual = models.DecimalField(max_digits=10, decimal_places=0)

    # Prescription details
    right_sph = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    right_cyl = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    right_axis = models.IntegerField(blank=True, null=True)
    left_sph = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    left_cyl = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    left_axis = models.IntegerField(blank=True, null=True)
    addition = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name
