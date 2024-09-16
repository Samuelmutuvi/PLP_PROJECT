from django.db import models

# Material model to store data for daily materials used
class Material(models.Model):
    material_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    amount_per_piece = models.DecimalField(max_digits=10, decimal_places=2)
    date_used = models.DateField()  # Changed the field name from 'date' to 'date_used'

    def __str__(self):
        return f"{self.material_name} - {self.quantity}"  # Improved string representation

# Employee model to store employee work details
class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    days_worked = models.PositiveIntegerField()
    amount_paid_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField( null=False)   # Changed the field name from 'date' to 'date_worked' for clarity

    def __str__(self):
        return f"{self.employee_name} ({self.days_worked} days)"  # Improved string representation
