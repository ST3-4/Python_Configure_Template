from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/shop')
def shop():
    return render_template('shop.html')


if __name__ == '__main__':
    app.run()
