
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<int:num>')
def level_one(num):
    return render_template("checkboard.html", myRangeOfColums = num, myRangeOfRows = num, myChosenColor1 = "red" myChosenColor2 = "black" )

@app.route('/<int:num1>/<int:num2')
def level_two(num1,num2):
    return render_template("checkboard.html", myRangeOfColums = num1, myRangeOfRows = num2, myChosenColor1 = "red" myChosenColor2 = "black" )

@app.route('/<int:num1>/<int:num2>/string:color1>')
def level_three(num1,num2,color1):
    return render_template("checkboard.html", myRangeOfColums = num1, myRangeOfRows = num2, myChosenColor1 = color1 myChosenColor2 = "black" )

@app.route('/<int:num1>/<int:num2>/string:color1>/<string:color2>')
def level_four(num1,num2,color1,color2):
    return render_template("checkboard.html", myRangeOfColums = num1, myRangeOfRows = num2, myChosenColor1 = color1 myChosenColor2 = color2 )

if __name__=="__main__":
    app.run(debug=True)