from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('input_data.html')

@app.route('/submit_form', methods=['POST'])
def handle_form():
    id_number = request.form.get('id')

    # Validate ID number
    if len(id_number) != 10 or not id_number[0].isalpha():
        return False

    # Convert the first letter to the corresponding number (A=10, B=11, ..., Z=35)
    first_digit = (ord(id_number[0]) - ord('A') + 10) // 10
    second_digit = (ord(id_number[0]) - ord('A') + 10) % 10

    # Multiply the converted two-digit number by 1 and 9
    total_sum = first_digit * 1 + second_digit * 9

    # Multiply the remaining digits by 8, 7, 6, 5, 4, 3, 2, 1
    weights = [8, 7, 6, 5, 4, 3, 2, 1]
    for i in range(1, 9):
        total_sum += int(id_number[i]) * weights[i - 1]

    # Add the last digit
    total_sum += int(id_number[-1])

    # Check if the result is divisible by 10
    return total_sum % 10 == 0

# Test the function
id_number = "A123456789"  # Example ID number
result = validate_id_number(id_number)
print("Result:", result)

