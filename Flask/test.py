from flask import Flask

app = Flask(__name__)

# root or index
@app.route('/')
def index():
    return "You have made it to the Index!"

# sub directories
@app.route("/hello")
def hello():
    return "Hello there!"


@app.route("/members")
def members():
    return "We have many members please supply a name"


# Listing variables to pass to function
@app.route("/members/<string:name>")
def getMember(name):
    return "I think " + name + " is a member"

@app.route("/members/<string:firstname>/<string:lastname>/<int:id>")
def getMemberID(firstname,lastname,id):
    return f'Member {id}: {lastname}, {firstname}'

if __name__ == "__main__":
    app.run(debug = True)
