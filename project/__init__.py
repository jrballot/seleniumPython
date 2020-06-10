from flask import Flask
from project.form.views import form_blueprint

app = Flask(__name__)
app.config.from_pyfile('_config.py')


app.register_blueprint(form_blueprint)

