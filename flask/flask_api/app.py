from flask import Flask
app=Flask(__name__)

@app.route("/")
def Home():
    return "hello World"

@app.route("/index")
def index():
    return "this is my index page"

from controller import *

# if __name__ == "__main__":
#     app.run(debug=True)
    # with app.app_context():
    #     db.create_all()
