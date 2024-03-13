import os # import os from python library

from flask import Flask, render_template #import flask class

# creat an instance of the class and store it in variable app. 
# () = name of the applications module. We just want one so use the built in python variable __name__.
# tells flask where to look for templates

app = Flask(__name__)

# render_template allows python to render contents of the HTML files and render to the screen
# in html file the format for the <a> MUST be Jinja format EXACTLY '
@app.route("/") # decorator (@) wraps the function. when we direct to the route directry (/), flask triggers the index function below
def index():
    return render_template('index.html') #render template function from flask (note where my templates/index file is in the directory!)


#another route view (function)
@app.route("/about")
def about():
    return render_template('about.html', page_title="About")


@app.route("/contact")
def contact():
    return render_template('contact.html', page_title="Contact")


@app.route("/careers")
def careers():
    return render_template('careers.html', page_title="Careers")

# if name == main then run app with the following arguments:
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"), # uses the op module to get the IP environment but a default value s set if this isn't found (0.0.0.0)
        port=int(os.environ.get("PORT", "5000")), # cast as an integer and the defualt here is 5000 (common port used by flask)
        debug=True)# !!!!!!!!!!!! helps debugging during developent (THIS MUST BE TURNED OFF WHEN WE SUBMIT OUR PROJECTS!!!!!!!!)