from flask import Flask, render_template, request, redirect, url_for
import json
import requests

app = Flask(__name__)
# url_for('static', filename='index.html')


@app.route('/')
def home():
    url_for('static', filename='index.html')
    return render_template('index.html', message="Hello, World! This is my first Flask app.")


@app.route('/about')
def about():
    return "This is the about page."


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return f"Hello, {name}! Welcome to my Flask app."


@app.route('/login', methods=['POST'])
def login():
    return {
        "name": "xiaoming"
    }


@app.route('/picture', methods=['POST'])
def picture():
    # url = "https://www.baidu.com/index.htm"
    # res = requests.get(url, headers={
    #     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36 Core/1.116.484.400 QQBrowser/13.6.6320.400"
    # })
    # print(res)
    return {
        "name": "xiaoming"
    }


if __name__ == '__main__':
    app.run(debug=True)
