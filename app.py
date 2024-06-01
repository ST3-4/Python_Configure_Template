from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', current_page='home')


@app.route('/shop')
def shop():
    return render_template('shop.html', current_page='shop')


@app.route('/about')
def about():
    return render_template('about.html', current_page='about')


@app.route('/services')
def services():
    return render_template('services.html', current_page='services')


@app.route('/blog')
def blog():
    return render_template('blog.html', current_page='blog')


@app.route('/contact')
def contact():
    return render_template('contact.html', current_page='contact')


@app.route('/jinja')
def jinja():
    now = datetime.now()
    return render_template('jinja.html', now=now)


if __name__ == '__main__':
    app.run()
