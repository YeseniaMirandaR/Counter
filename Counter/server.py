# Build a flask application that counts the number of times the root route ('/') has been viewed. 
# As part of this assignment, please start with the following features first:

# localhost:5000 - have the template render the number of times the client has visited this site
# localhost:5000/destroy_session - Clear the session. Once cleared, redirect to the root.

from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key = "counter and session 2411"

@app.route('/')
def visitCounter():
    if "counter" not in session:
        session["counter"] = 0
    else:
        session["counter"] += 1
    return render_template("index.html")

@app.route('/addVisit+2')
def addVisit():
    session["counter"] += 1
    return redirect('/')

@app.route('/destroy_session')
def resetSession():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)