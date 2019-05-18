from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello_handler():
    return 'hello, i am flask2'


def main():
    app.run(host='0.0.0.0', port=8081, debug=True)


if __name__ == '__main__':
    main()
