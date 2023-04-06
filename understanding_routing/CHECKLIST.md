MAKE NEW DIRECTORY

inside the directory create virtual environment

RUN PIPENV INSTALL FLASK

PIPENV SHELL

SERVER.PY

from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.




START APP BY RUNNING IN TERMINAL PYTHON SERVER.PY

GO TO LOCALHOST:5000

CREATE A TEMPLATE INDEX.HTML templates/index.html

RENDER TEMPLATE AT TOP NEXT TO IMPORT...RENDER_TEMPLATE

RETURN RENDER_TEMPLATE ('INDEX.HTML)
