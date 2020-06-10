from flask import flash, redirect, render_template, request, Blueprint
from .forms import RegisterForm

form_blueprint = Blueprint('form',__name__)

@form_blueprint.route('/',methods=['GET','POST'])
def login():
    error = None
    form = RegisterForm(request.form)
    return render_template('register.html',error=error,form=form)
