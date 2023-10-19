#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask ,render_template
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB!"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')

@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def im_a_number(n):
    """display “n is a number” only if n is an integer"""
    return f'{n} is a number'

@app.route('/number_template/<int:n>', strict_slashes=False)
def display_html(n):
    """display a HTML page only if n is an integer"""
    return render_template("5-number.html", number=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        n_type = 'even'
    else:
        n_type = 'odd'
    return render_template("6-number_odd_or_even.html", number=n, n_type=n_type)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
