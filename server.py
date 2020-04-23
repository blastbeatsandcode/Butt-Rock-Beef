from flask import Flask, request, render_template
import MySQLdb
import json

app = Flask(__name__, static_url_path='/static', template_folder='template')

# Application routes determine the functions to call when the user tries to access a particular URL
@app.route('/')
def index():
	return render_template("index.html", title='Butt-Rock Beef : How angry can these dads get?')

@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
	return render_template('500.html'), 500
