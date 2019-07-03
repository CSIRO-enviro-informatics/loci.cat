from flask import Flask, request, render_template, Response
from os import path
APP_DIR = path.dirname(path.realpath(__file__))
TEMPLATES_DIR = path.join(APP_DIR, 'templates')
STATIC_DIR = path.join(APP_DIR, 'static')

app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/principles')
def principles():
    return render_template('principles.html')


@app.route('/models')
def models():
    return render_template('models.html')


@app.route('/data')
def data():
    return render_template('data.html')


@app.route('/cache')
def cache():
    return render_template('cache.html')


@app.route('/examples')
def examples():
    return render_template('examples.html')


@app.route('/sparql', methods=['GET', 'POST'])
def sparql():
    return render_template('sparql.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
