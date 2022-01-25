"""Greeting Flask app."""

from random import choice
from re import X

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page.<a href='/hello'> Go to greeting </a></html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet" method="GET">
        What's your name? <input type="text" name="person"><br><br>
        Pick a compliment: <br>
        <input type="radio" name="comp" value="awesome">awesome<br>
        <input type="radio" name="comp" value="terrific">terrific<br>
        <input type="radio" name="comp" value="fantastic">fantastic<br>
        <input type="radio" name="comp" value="neato">neato<br>
        <input type="radio" name="comp" value="fantabulous">fantabulous<br>
        <input type="radio" name="comp" value="Wowza">Wowza<br>
        <input type="radio" name="comp" value="oh-so-not-meh">oh-so-not-meh<br>
        <input type="radio" name="comp" value="brilliant">brilliant<br>
        <input type="radio" name="comp" value="ducky">ducky<br>
        <input type="radio" name="comp" value="coolio">coolio<br>
        <input type="radio" name="comp" value="incredible">incredible<br>
        <input type="radio" name="comp" value="wonderful">wonderful<br>
        <input type="radio" name="comp" value="smashing">smashing<br>
        <input type="radio" name="comp" value="lovely">lovely<br><br>
        <input type="submit" value="Submit"><br><br>
        </form>

        <form action="/diss" method="GET">
        What's your name? <input type="text" name="person"><br><br>
        Or pick a diss: You are...<br>
        <input type="radio" name="diss" value="a clown">a clown<br>
        <input type="radio" name="diss" value="better as a paper weight">better as a paper weight<br>
        <input type="radio" name="diss" value="a literal fruit loop">a literal fruit loop<br>
        <input type="radio" name="diss" value="a penny- two faced">a penny- two faced<br>
        <input type="radio" name="diss" value="so ugly you make onions cry">so ugly you make onions cry<br><br>
        <input type="submit" value="Submit">
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("comp")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


@app.route('/diss')
def give_diss():

    player = request.args.get("person")

    diss = request.args.get("diss")


    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}.
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
