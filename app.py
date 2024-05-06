from flask import Flask, request, render_template

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
    if len(id_number) != 10:
        return "身分證號碼應為10碼", 400
    if not id_number[0].isalpha():
        return "身分證號碼第一位應為字母", 400

    # Convert the first letter to the corresponding number (A=10, B=11, C=12, ..., Z=33)
    first_letter_value = ord(id_number[0].upper()) - ord('A') + 10

    # Multiply the converted two-digit number by 1 and 9
    first_digit = first_letter_value // 10
    second_digit = first_letter_value % 10
    total_sum = first_digit * 1 + second_digit * 9

    # Multiply the remaining digits by 8, 7, 6, 5, 4, 3, 2, 1
    weights = [8, 7, 6, 5, 4, 3, 2, 1]
    for i in range(1, 9):
        total_sum += int(id_number[i]) * weights[i - 1]

    # Add the last digit
    last_digit = int(id_number[-1])
    total_sum += last_digit

    # Check if the result is divisible by 10
    if total_sum % 10 == 0:
        return "身分證號碼正確", 200
    else:
        return "身分證號碼不正確", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
  # Listen on all available network interfaces and port 80

