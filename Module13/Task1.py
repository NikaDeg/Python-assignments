from flask import Flask, request
app = Flask(__name__)
@app.route('/prime_number/<num>')
def prime_or_not (num):
    num = int(num)
    def check (n):
        division = 0
        for i in range(1, n+1):
            if n % i == 0:
                division = division + 1
        if division == 2:
            answer = True
        else: answer = False

        return answer
    true_or_false = check(num)
    response = {
        "Number": num,
        "isPrime": true_or_false
    }

    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)