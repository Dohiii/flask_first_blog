from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    first_name = 'John'
    return render_template('index.html', first_name=first_name)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

# Create a custom error pages

#invalid URL
@app.errorhandler(404)
def error404(e):
    return render_template('page404.html'), 404
    
 