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
        return "身分證號碼應為10碼，且第一位應為大寫字母", 400

    # Define a dictionary to map letters to numbers
    letter_to_number = {chr(i): i - ord('A') + 10 for i in range(ord('A'), ord('Z') + 1)}

    # Convert the first letter to the corresponding number
    first_digit = letter_to_number[id_number[0]] // 10
    second_digit = letter_to_number[id_number[0]] % 10

    # Multiply the converted two-digit number by 1 and 9
    total_sum = first_digit * 1 + second_digit * 9

    # Multiply the remaining digits by 8, 7, 6, 5, 4, 3, 2, 1
    weights = [8, 7, 6, 5, 4, 3, 2, 1]
    for i in range(1, 9):
        total_sum += int(id_number[i]) * weights[i - 1]

    # Add the last digit
    total_sum += int(id_number[-1])

    # Check if the result is divisible by 10
    if total_sum % 10 == 0:
        return "身分證號碼正確", 200
    else:
        return "身分證號碼不正確", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)



