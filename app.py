from flask import Flask, request, jsonify, render_template
import mysql.connector
from mysql.connector import Error
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


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
        print(f"Error in connecting to MySQL: {e}")
        return None

# Route to serve HTML page (if you have an index.html file)
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to capture material data
@app.route('/submit/materials', methods=['POST'])
def submit_materials_data():
    data = request.json
    material = data.get('material')
    quantity = data.get('quantity')
    amount_per_piece = data.get('amount_per_piece')
    date = data.get('date')

    conn = get_db_connection()
    if conn is None:
        return jsonify({"message": "Database connection failed!"}), 500

    cursor = conn.cursor()

    try:
        # Insert material data into database
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
        # Insert employee data into database
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
