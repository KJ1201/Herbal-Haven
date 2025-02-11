from flask import Blueprint, render_template, redirect, flash, url_for

auth = Blueprint("auth", __name__)

@auth.route('/')
def login():
    return '<h1>Herbal-Haven</h1>'