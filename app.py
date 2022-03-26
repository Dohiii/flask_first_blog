from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import os



load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


 
# Create a Form Class
class NameForm(FlaskForm):
    name = StringField('Whats Your Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

@app.route('/name', methods=['GET', 'POST'])
def name():
    
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash('Form submited succesfully')
    return render_template('name.html', name=name, form=form)

# Create a custom error pages

#invalid URL
@app.errorhandler(404)
def error404(e):
    return render_template('page404.html'), 404


#internal Server Error
@app.errorhandler(500)
def error500(e):
    return render_template('page500.html'), 500



    
 