# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Ahan Roy" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():
  name = "Amar Nath Roy" # write your name
  age = "47" # write your age
  return render_template('father.html' , name = name , age = age)

# define the route to mother webpage

@app.route("/mother")
def father():
  name = "Dipanwita Roy" # write your name
  age = "40" # write your age
  return render_template('mother.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/friend")
def father():
  name = "Mainak Mukherjee" # write your name
  age = "14" # write your age
  return render_template('father.html' , name = name , age = age)

# add other routes, if you want
