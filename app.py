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

    first_letter = id_number[0]
    if first_letter.isalpha() and first_letter.isupper():
        corresponding_number = ord(first_letter) - 55  # A 对应的 ASCII 码是 65，所以减去 55
        first_digit = corresponding_number // 10
        second_digit = corresponding_number % 10
        total_sum = first_digit * 1 + second_digit * 9
        weights = [8, 7, 6, 5, 4, 3, 2, 1]
        for i in range(1, 9):
            total_sum += int(id_number[i]) * weights[i - 1]
        last_digit = int(id_number[-1])
        total_sum += last_digit

        if total_sum % 10 == 0:
            return "身分證號碼正確", 200
        else:
            return "身分證號碼不正確", 400
    else:
        return "第一個字母不是大寫英文字母", 400
        if total_sum % 10 == 0:
    print("身份证号码校验通过")
else:
    print("身份证号码校验未通过")


    # Check if the result is divisible by 10
    if total_sum % 10 == 0:
        return "身分證號碼正確", 200
    else:
        return "身分證號碼不正確", 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

