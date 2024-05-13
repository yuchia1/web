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

# 假设 id_number 是一个字符串
id_number = "A123456789"  # 这里假设 id_number 是一个具体的身份证号码，你可以根据实际情况修改

# 检查后九个字符是否都是数字
if id_number[1:].isdigit():
    print("后九位字符都是数字")
else:
    print("后九位字符不全是数字")


    # 假设 id_number 的第一个字母为 letter
letter = id_number[0]  # 这里假设字母为 id_number 的第一个字母，你可以根据实际情况修改

if letter.isalpha() and letter.isupper():  # 确保是大写字母
    corresponding_number = ord(letter) - 55  # A 对应的 ASCII 码是 65，所以减去 55
    print(corresponding_number)
else:
    print("请输入大写字母")

  # 假设 id_number 是一个字符串
id_number = "A123456789"  # 这里假设 id_number 是一个具体的身份证号码，你可以根据实际情况修改

# 将转换后的两位数字分别乘以1和9
first_digit = 1
second_digit = 9

# 分别将第二个到第九个数字乘以8, 7, 6, 5, 4, 3, 2, 1
weights = [8, 7, 6, 5, 4, 3, 2, 1]
products = [int(id_number[i]) * weights[i] for i in range(1, 9)]

# 计算所有乘积的总和
total_sum = first_digit * 1 + second_digit * 9 + sum(products)

# 加上最后一个数字
last_digit = int(id_number[-1])
total_sum += last_digit

print("所有乘积相加的结果（未加上最后一位）：", total_sum)

# 这里假设身份证号码的校验结果是通过的
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
  # Listen on all available network interfaces and port 80

