// Function to show a specific form and hide the others
function showForm(formId) {
    // Hide all forms
    document.querySelectorAll('.form-container').forEach(form => {
        form.style.display = 'none';
    });

    // Show the selected form
    document.getElementById(formId).style.display = 'block';
}

// Function to submit materials form
function submitMaterials() {
    const form = document.getElementById('materialsForm').querySelector('form');
    const formData = new FormData(form);
    const data = {
        material: formData.get('material'),
        quantity: formData.get('quantity'),
        amount_per_piece: formData.get('amount_per_piece'),
        date: formData.get('date')
    };

    fetch('/submit/materials', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Function to submit employees form
function submitEmployees() {
    const form = document.getElementById('employeesForm').querySelector('form');
    const formData = new FormData(form);
    const data = {
        employee_name: formData.get('employee_name'),
        days_worked: formData.get('days_worked'),
        amount_paid_per_day: formData.get('amount_paid_per_day'),
        date: formData.get('date')
    };

    fetch('/submit/employees', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
