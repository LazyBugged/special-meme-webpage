# https://github.com/LazyBugged
# 11/02/2021

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Rick Rolled!'

app.run(host='0.0.0.0', port=81)
