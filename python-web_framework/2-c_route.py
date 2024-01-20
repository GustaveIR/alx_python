#!/usr/bin/python3
"""Start a Flask web application"""

from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route / display “Hello HBNB!”"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route /hbnb display “HBNB”"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Route /c/<text> display “C ” followed by the value of the text variable"""
    text_with_spaces = escape(text.replace('_', ' '))
    return 'C {}'.format(text_with_spaces)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
