from flask_app import app

# controllers has to match controllers

from flask_app.controllers import dojo_controllers, ninjas_controllers





if __name__ == "__main__":
    app.run(debug=True)