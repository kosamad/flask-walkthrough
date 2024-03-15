import os # import os from python library
import json
from flask import Flask, render_template, request, flash #import flask class (request is finding out what method (in the contact form) we used. flash is for giving feedback to user.  

#import the env library only if the stystem can find an env.py file. This creates a pycache file on the left, put into gitignore
if os.path.exists("env.py"):
    import env


# creat an instance of the class and store it in variable app. 
# () = name of the applications module. We just want one so use the built in python variable __name__.
# tells flask where to look for templates

app = Flask(__name__)

#grab hidden key variable
app.sercret_key = os.environ.get("SECRET_KEY")

# render_template allows python to render contents of the HTML files and render to the screen
# in html file the format for the <a> MUST be Jinja format EXACTLY '
@app.route("/") # decorator (@) wraps the function. when we direct to the route directry (/), flask triggers the index function below
def index():
    return render_template('index.html') #render template function from flask (note where my templates/index file is in the directory!)


#another route view (function)
@app.route("/about")
def about():
    data = [] #initialise empty array. The next line opens the json file using a with block, r = readonly
    with open("data/company.json", "r") as json_data: 
        data = json.load(json_data) # sets empty data list to = the parsed json data.
    return render_template('about.html', page_title="About", company = data) # The second argument uses server side code to set front end data (page title), third is assigning a new varibale company which = the data list from Json

#route for individual members. the second / says that it is where we route when we have the about page with something after it. <> is data from url path
@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member = member) # first member here is variable being passed through html file, second is the object created above


@app.route("/contact", methods = ["GET", "POST"]) # methods tells flask we are handling a post request too (for form)
def contact():
    if request.method == "POST":
        # flash message for UX
        flash("Thanks {}, we have received your message!".format(request.form.get("name"))) # request.form.name gets the name inputed by the user using the name attribute
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