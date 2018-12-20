import datetime

from jinja2 import Environment, FileSystemLoader
from flask import Flask, render_template
import os

app = Flask(__name__)

_root = os.path.dirname(os.path.abspath(__file__))
templates_dirctory = os.path.join(_root, 'templates')

env = Environment(loader=FileSystemLoader(templates_dirctory))
# Jinja2 supports a templates Environment (central object) and is used to load templates from the file system

template = env.get_template('template(Parent).html')


#
@app.route("/")
def template_test():
    # Render the template (template(Parent).html) via render_template() function!
    try:
        templateTest = render_template(
            'child.html', Title="MindRoad AB",
            my_list=["Embedded", "Academy", "Application", "Sourcing"], title="Home", my_var=2)
        return templateTest
    except Exception as e:
        return str(e)

@app.template_filter()
def power(x, y):
    return x**y


# To make the function as a filter simply you have to add it to Jinja Environment as following:
app.jinja_env.filters['POWER'] = power

if '__main__' == __name__:
    app.run(debug=True)
