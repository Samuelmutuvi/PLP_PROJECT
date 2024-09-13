// Function to show the appropriate form
function showForm(formId) {
    // Hide both forms first
    document.getElementById('materialsForm').style.display = 'none';
    document.getElementById('employeesForm').style.display = 'none';

    // Show the selected form
    document.getElementById(formId).style.display = 'block';
}

// Get CSRF token from the form
function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

// Submit materials form using fetch
function submitMaterials() {
    const material = document.getElementById('material').value;
    const quantity = document.querySelector('input[name="quantity"]').value;
    const amount_per_piece = document.querySelector('input[name="amount_per_piece"]').value;
    const date = document.querySelector('input[name="date"]').value;

    fetch('capture/material/submit/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()  // Include CSRF token
        },
        body: JSON.stringify({
            material: material,
            quantity: quantity,
            amount_per_piece: amount_per_piece,
            date: date
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('response').innerText = 'Materials submitted successfully!';
        console.log('Success:', data);
    })
    .catch(error => {
        document.getElementById('response').innerText = 'Error submitting materials.';
        console.error('Error:', error);
    });
}

// Submit employees form using fetch
function submitEmployees() {
    const employee_name = document.getElementById('employee_name').value;
    const days_worked = document.getElementById('days_worked').value;
    const amount_paid_per_day = document.getElementById('amount_paid_per_day').value;
    const date = document.getElementById('employee_date').value;

    fetch('capture/employee/submit/', {  // Ensure this matches your Django URL pattern
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()  // Include CSRF token
        },
        body: JSON.stringify({
            employee_name: employee_name,
            days_worked: days_worked,
            amount_paid_per_day: amount_paid_per_day,
            date: date
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('response').innerText = 'Employee data submitted successfully!';
        console.log('Success:', data);
    })
    .catch(error => {
        document.getElementById('response').innerText = `Error: ${error.message}`;
        console.error('Error:', error);
    });
}


// Function to get CSRF token (assuming it's in a hidden input field)
function getCSRFToken() {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    return csrfToken;
}
