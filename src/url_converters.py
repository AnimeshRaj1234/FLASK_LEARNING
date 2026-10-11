# CONVERTERS
# INT, FLOAT, STRING
# PATH => FOR FILES
# UUID => UNIQUE USER ID

from flask import Flask
from uuid import UUID
app = Flask(__name__)

@app.route("/")
def users():
    return "YOU ARE AT CONVERTERS PAGE"

@app.route("/user/<name>/<int:rollno>")
def user_name(name,rollno):
    return f"HI {name}, YOUR ROLLNO IS {rollno}"

@app.route("/files/<path:file_path>")
def files(file_path):
    return file_path

@app.route("/user/<uuid:user_id>")
def userID(user_id):
    return str(user_id)

if __name__ == "__main__":
    app.run(debug=True)