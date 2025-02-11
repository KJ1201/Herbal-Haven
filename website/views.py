from flask import Blueprint, render_template, redirect, flash, url_for

views = Blueprint("views", __name__)

@views.route('/')
def home():
    return render_template('auth/signup.html')