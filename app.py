from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Database connection
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            port=3305,
            password="samuel",  # Replace with your MySQL password
            database="construct_capture"
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

@app.route('/index.html')
def index():
    return "Welcome to the Construction Capture App!"

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

# Endpoint to capture material data
@app.route('/submit/materials', methods=['POST'])
def submit_materials_data():
    data = request.json
    material = data.get('material_name')
    quantity = data.get('quantity')
    amount_per_piece = data.get('amount_per_piece')
    date = data.get('date')

    conn = get_db_connection()
    if conn is None:
        return jsonify({"message": "Database connection failed!"}), 500

    cursor = conn.cursor()

    try:
        # Insert material data
        cursor.execute("""
            INSERT INTO materials (material_name, quantity, amount_per_piece, date) VALUES (%s, %s, %s, %s)
        """, (material, quantity, amount_per_piece, date))

        conn.commit()
        return jsonify({'message': 'Materials data submitted successfully.'})
    
    except Error as e:
        conn.rollback()
        return jsonify({'message': f'Error: {e}'}), 500
    
    finally:
        cursor.close()
        conn.close()

# Endpoint to capture employee data
@app.route('/submit/employees', methods=['POST'])
def submit_employee_data():
    data = request.json
    employee_name = data.get('employee_name')
    days_worked = data.get('days_worked')
    amount_paid_per_day = data.get('amount_paid_per_day')
    date = data.get('date')

    conn = get_db_connection()
    if conn is None:
        return jsonify({"message": "Database connection failed!"}), 500

    cursor = conn.cursor()

    try:
        # Insert employee data
        cursor.execute("""
            INSERT INTO employees (employee_name, days_worked, amount_paid_per_day, date) VALUES (%s, %s, %s, %s)
        """, (employee_name, days_worked, amount_paid_per_day, date))

        conn.commit()
        return jsonify({"message": "Employee data submitted successfully!"})
    
    except Error as e:
        conn.rollback()
        return jsonify({"message": f"Error: {e}"}), 500

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
