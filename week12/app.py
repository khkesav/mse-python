from flask import request
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile/<name>/<int:user_id>')
def user(name, user_id):
    return render_template('profile.html', username=name, id=user_id)

if __name__ == '__main__':
    app.run(debug=True)