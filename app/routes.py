# routes.py

from flask import Blueprint, render_template, request, redirect
from .services import send_email
import os

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
        send_email(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong, please try again.'
