from flask import Flask, render_template


# Create a Flask instance
app = Flask(__name__)


# Create a route
@app.route('/')

def index():
    return render_template("index.html")


# localhost:5000/user/John
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", username=name)


# Create custom error pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
