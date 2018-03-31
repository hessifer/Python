from flask import Flask
from flask import request

# use the current namespace either __main__ or simple_app.py if called in another file
app = Flask(__name__)

# define our routes
@app.route("/")
def index(name="Treehouse"):
    # in flask we can access all arguments passed to the site
    # in args using the get() method
    # if name was set in url use it if not use the default value of name
    # for example http://localhost?name=Xavy
    name = request.args.get('name', name)
    return "Hello from {}".format(name)
# define port for app to listen on
app.run(debug=True, port=8000, host='0.0.0.0')
