# JINJA2 => JINJA2 IS A TEMPLATE ENGINE USED BY FLASK TO GENERATE DYNAMIC HTML PAGES USING PYTHON DATA
# COMMENTS =>
#  HTML = <!--  -->, ( IT CAN BE SEEN IN SOURCE CODE)
#  JINJA = {#....#} (IT IS REMOVED FROM SERVER SIDE AND CAN'T BE SEEN IN SOURCE CODE)

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    is_logged_in = False
    marks = 75
    courses = ['PYTHON','FLASK','FASTAPI','DJANGO','BOOTSTRAP']
    
    return render_template("index.html",
     is_logged_in=is_logged_in,marks=marks,courses=courses)

if __name__ == "__main__":
    app.run(debug=True)