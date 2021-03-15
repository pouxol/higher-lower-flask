from flask import Flask
import random

app = Flask(__name__)

number = random.randint(0, 9)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<int:num>')
def test(num):
    if number < num:
        return f"<h1>Your number is too high.</h1>"
    elif number > num:
        return f"<h1>Your number is too low.</h1>"
    else:
        return f'<h1>YESSS!!!</h1>'


if __name__ == "__main__":
    app.run(debug=True)
