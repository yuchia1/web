from flask import Flask, request, render_template
import re

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('input_data.html')

@app.route('/submit_form', methods=['POST'])
def handle_form():
    id_number = request.form.get('id')
    name = request.form.get('name')
    gender = request.form.get('gender')
    email = request.form.get('email')

    # Validate ID number (assuming it's numeric)
    if len(id_number) != 10 or not id_number[0].isalpha():
        return "身分證號碼應為10碼，且第一位應為大寫字母", 400

    # Convert the first letter to the corresponding number
    first_letter_value = ord(id_number[0].upper()) - ord('A') + 10
    first_digit = first_letter_value // 10
    second_digit = first_letter_value % 10

    # Print the first digit after conversion
    print("First digit after conversion:", first_digit)

    # Multiply the converted two-digit number by 1 and 9
    total_sum = first_digit * 1 + second_digit * 9

    # Multiply the remaining digits by 8, 7, 6, 5, 4, 3, 2, 1
    weights = [8, 7, 6, 5, 4, 3, 2, 1]
    for i in range(1, 9):
        total_sum += int(id_number[i]) * weights[i - 1]

    # Add the last digit
    total_sum += int(id_number[-1])

    # Check if the result is divisible by 10
    if total_sum % 10 != 0:
        return "身分證號碼不正確", 400

    # Validate name (assuming it's alphabetic)
    if not re.match(r'^[A-Za-z\s]+$', name):
        return "Invalid name", 400

    # Validate gender
    if gender not in ['Male', 'Female']:
        return "Invalid gender", 400

    # Validate email
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return "Invalid email", 400

    return "All entries are valid", 200

if __name__ == '__main__':
    app.run(host='0.0.0, port=80)  # Listen on all available network interfaces and port 80






