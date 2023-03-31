from __future__ import print_function
import sys

from flask import Flask


app = Flask(__name__)


@app.route('/')

def main():
    return "<h1>Hello, bitch!</h1><br><a href='/index'>перейти на 2-ую страницу</a>"

@app.route('/index')

def index():
    return 'It is my first project'



if __name__ == '__main__':
    app.run()