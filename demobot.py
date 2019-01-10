# Import flask
from flask import Flask, request

# Create your app (web server)
app = Flask(__name__)


# When people visit the home page '/' use the hello_world function
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/ncss')
def page_ncss():
    return '<h1>NCSS!</h1>'

@app.route('/greet')
def greet_person():
    # Get the value of the 'name' query parameter
    # request.values is a dictionary (cool!)
    name = request.values.get('name')
    # This bot says hi to every name it gets sent!
    return f'hi {name}!'

@app.route('/weather')
def page_weather():
    temperature = request.values.get('temp')
    if int(temperature) > 30 :
        return "It's too hot!"
    else :
        return f'The temperature is {temperature}.'

if __name__ == '__main__':
    # Start the web server!
    app.run()
    