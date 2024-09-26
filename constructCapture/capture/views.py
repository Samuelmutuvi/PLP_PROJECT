from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import logging
logger = logging.getLogger(__name__)

from .models import Material
from .models import Employee

import json

# capture/views.py
def index(request):
    # You can pass context variables to the template if needed
    return render(request, 'index.html')


# Disable CSRF protection just for testing (not recommended for production)
@csrf_exempt
def submit_materials(request):
    if request.method == 'POST':
        try:
            # Parse the JSON body
             # Extract fields from the request data
            data = json.loads(request.body)
            
            material = data.get('material')
            quantity = data.get('quantity')
            amount_per_piece = data.get('amount_per_piece')
            date = data.get('date')
            
            #  logger.info(f"Inserting: {material}, {quantity}, {amount_per_piece}, {date_used}")
            
               # Save data to the Material model (using Django ORM)
            Material.objects.create(
                material_name=material,
                quantity=quantity,
                amount_per_piece=amount_per_piece,
                date_used=date
            )
            
            # Return a success response
            return JsonResponse({'message': 'Materials submitted successfully!'}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid data format'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)


@csrf_exempt  # Exempt from CSRF for testing purposes (remove in production)
def submit_employees(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            
            employee_name = data.get('employee_name')
            days_worked = data.get('days_worked')
            amount_paid_per_day = data.get('amount_paid_per_day')
            role = data.get('role_of_the_employee')
            date = data.get('date')

 # Save the employee data (if Employee model exists)
            Employee.objects.create(
                employee_name=employee_name,
                days_worked=days_worked,
                amount_paid_per_day=amount_paid_per_day,
                role = role,
                date=date
            )

            # Return success response
            return JsonResponse({'message': 'Employee data submitted successfully!'}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON format'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
    
    