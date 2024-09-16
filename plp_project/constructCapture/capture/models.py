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
    date = models.DateField( null=False)  
    role = models.CharField(max_length = 50,default="Worker")
    unique_identifier = models.CharField(max_length=255,unique=True,blank=True) 
    
    
    def save(self,*args,**kwargs):
        # Generate unique identifier before saving
        if not self.unique_identifier:
            prefix = self.role[0].upper()  # M for Mason, P for Plumber, etc.
            count = Employee.objects.filter(role=self.role).count() + 1
            self.unique_identifier = f"{prefix}{count}"

        super(Employee, self).save(*args, **kwargs)
    
    
    

    def __str__(self):
        return f"{self.employee_name} ({self.unique_identifier})"  # Improved string representation
