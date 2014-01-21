from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", 
        title = 'Home')
@app.route('/home')
def home():
    return render_template("index.html",
        title = "Home")
@app.route('/about')
def about():
    return render_template("about.html", 
        title = 'about')
@app.route('/contact')
def contact():
    return render_template("contact.html",
        title = "contact")
@app.route('/photos')
def photos():
    return render_template("photos.html",
        title = "photos")
@app.route('/season')
def season():
    return render_template("season.html",
        title = "season")
@app.route('/class')
def classes():
    return render_template("class.html",
        title = "class")