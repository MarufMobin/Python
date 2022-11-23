""" My flask Application """

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to my Home Page"

@app.route('/about', methods=['GET'])
def about():
    return "my name is maruf"

if __name__ == '__main__':
    app.run()
