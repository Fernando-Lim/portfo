# routes.py

from flask import Blueprint, render_template, request, redirect
from .services import write_to_file, write_to_csv

# Create a Blueprint for routes
main = Blueprint('main', __name__)

@main.route('/')
def my_home():
    return render_template('index.html')

@main.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)

@main.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong, please try again.'
