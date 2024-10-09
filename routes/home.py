from flask import Blueprint, render_template

home_route = Blueprint('home_route',  __name__, template_folder='templates')

@home_route.route('/')
def home():
    return render_template('index.html')