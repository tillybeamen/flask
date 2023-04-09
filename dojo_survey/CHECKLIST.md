- [x] create a new directory
- [x] inside the directory create virtual env by running:
  
'''bash
[python -m] pipenv install flask
'''
- [x] activate the virtual env every time you open a new terminal:
  
  '''bash
  [python -m] pipenv shell
  '''

- [x] create [server.py](server.py)

'''py
from flask import Flask, render_template, redirect, session, request #import flask to allow us to create our app

app = Flask(__name__)
app.secret_key = "any string you want"

@app.route('/')        #the "@" decorator associates this route with the function imeediately following
def index():
    return render_template('index.html')  

@app.route('/handle_form', methods=['POST'])
def create():
    ## code to process date from form
    return redirect('/')  # always redirect to a route

@app.route('/show')
    def show():

        return render_template('show.html')

if __name__=="__main__":     # Ensure this file is being run directly and not from a different module
    app.run(debug=True)     # Run the app in debug mode.

- [x] start app by running python server.py