from flask import Flask, render_template, request, redirect, url_for

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


if __name__ == '__main__':
    app.run(debug=True)
