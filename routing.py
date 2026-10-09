# STATIC ROUTE AND DYNAMIC ROUTE

# STATIC ROUTE => THAT FOLLOWS A SPECIFIC PATH AND HAVE A FIXED URL
# DYNAMIC ROUTE => IT CONTAINS A VARIABLE PART OF URL

from flask import Flask

app = Flask(__name__)

@app.route("/")
def users():
    return "YOU ARE AT USERS PAGE"

@app.route("/user/<name>")
def user(name):
    return f"HELLO {name}"

@app.route("/user/<name>/<rollno>")
def user_name(name,rollno):
    return f"HI {name}, YOUR ROLLNO IS {rollno}"

if __name__ == "__main__":
    app.run(debug=True)

