from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return "dojo!"

@app.route('/hi/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hi(name):
    print(name)
    return f"<h1>Hi, {name}</h1>"

@app.route('/repeat/<roll>/<name>')
def repeat(roll,name):
    # name= "yeah<br>"
    print(name)
    return f"{name * int(roll)}"


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)

