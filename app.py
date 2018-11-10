
from flask import Flask

# create application object
app = Flask("__name__")

# link view function to a url
@app.route("/")

# define view using a function
def hello():
    return "Hello Dude!"

if __name__ == "__main__":
    app.run("0.0.0.0")
