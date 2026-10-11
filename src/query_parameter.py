# QUERY PARAMETER => PART OF URL WHICH GIVES EXTRA INFO TO SERVER AND URL HAS KEY AND VALUE PAIRS
# MULTIPLE QUERY PARAMETER => WE USE MORE THAN ONE KEY VALUE PAIR AND USE & BETWEEN THE PAIRS

from flask import Flask, request 
# REQUEST => IT HELPS IN READING THE DATA COMING FROM BROWSER/CLIENT

app = Flask(__name__)

@app.route("/search")
def search():
    name = request.args.get("name","guest")
    course = request.args.get("course","unkown course")
    return f"{name} is learning {course}"

if __name__ == "__main__":
    app.run(debug=True)