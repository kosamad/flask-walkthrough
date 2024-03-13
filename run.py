import os # import os from python library

from flask import Flask #import flask class

# creat an instance of the class and store it in variable app. 
# () = name of the applications module. We just want one so use the built in python variable __name__.
# tells flask where to look for templates

app = Flask(__name__)


@app.route("/") # decorator (@) wraps the function. when we direct to the route directry (/), flask triggers the index function below
def index():
    return "Hello, World"

# if name == main then run app with the following arguments:
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"), # uses the op module to get the IP environment but a default value s set if this isn't found (0.0.0.0)
        port=int(os.environ.get("PORT", "5000")), # cast as an integer and the defualt here is 5000 (common port used by flask)
        debug=True)# !!!!!!!!!!!! helps debugging during developent (THIS MUST BE TURNED OFF WHEN WE SUBMIT OUR PROJECTS!!!!!!!!)