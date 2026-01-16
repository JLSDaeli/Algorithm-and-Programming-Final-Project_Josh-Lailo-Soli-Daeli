# import the Flask class to make a web applications functional deeply
from flask import Flask
# import the index following its controller function
from controller import index

# Form an instance of the Flask application
# The __name__ component can lead the Flask to locate and coordinate resources and templates  
app = Flask(__name__)

# enroll the URL route for shaping the home page
# The route can allow GET and POST requests into process.
app.add_url_rule("/", "index", index, methods=["GET", "POST"])

# The application is flowed if the file is performed.
# The debug turned in True to allow auto-reload and error messages.
if __name__ == "__main__":
    app.run(debug=True)
    