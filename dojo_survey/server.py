from flask import Flask, render_template, redirect, session, request #import flask to allow us to create our app

app = Flask(__name__)
app.secret_key = "any string you want"

languages = ["Python", "Javascript", "C#", "Java", "Ruby"]
locations = ["Oakland", "Chicago", "New York", "Paris", "Dubai"]

@app.route('/')        #the "@" decorator associates this route with the function imeediately following
def index():
    return render_template('index.html', locations = locations, languages = languages)  

@app.route('/handle_form', methods=['POST'])
def create():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    ## code to process date from form
    return redirect('/show')  # always redirect to a route

@app.route('/show')
def show():

    return render_template('show.html')

if __name__=="__main__":     # Ensure this file is being run directly and not from a different module
    app.run(debug=True)     # Run the app in debug mode.