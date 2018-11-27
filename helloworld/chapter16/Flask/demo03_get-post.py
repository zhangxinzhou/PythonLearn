from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_login()
    else:
        show_login_form()


def do_login():
    return 'input your username and password'


def show_login_form():
    return 'login form'


if __name__ == '__main__':
    app.run(debug=True)
