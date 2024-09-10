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
    

    fetch('/materials/Submit', {
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
        console.error('Error occurred:', error);
        // Optionally, log more detailed error information
        if (error.response) {
            // The server responded with a status code that falls out of the range of 2xx
            console.error('Response data:', error.response.data);
            console.error('Response status:', error.response.status);
            console.error('Response headers:', error.response.headers);
        } else if (error.request) {
            // The request was made but no response was received
            console.error('Request data:', error.request);
        } else {
            // Something happened in setting up the request that triggered an Error
            console.error('Error message:', error.message);
        }
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
        console.error('Error occurred:', error);
        // Optionally, log more detailed error information
        if (error.response) {
            // The server responded with a status code that falls out of the range of 2xx
            console.error('Response data:', error.response.data);
            console.error('Response status:', error.response.status);
            console.error('Response headers:', error.response.headers);
        } else if (error.request) {
            // The request was made but no response was received
            console.error('Request data:', error.request);
        } else {
            // Something happened in setting up the request that triggered an Error
            console.error('Error message:', error.message);
        }
    });
}
