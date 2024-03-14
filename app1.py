#flask app url routing
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

@app.route("/", methods = ["GET"]) # two paramters - url and 
# "/" ->  at url's homepage, below func should get triggered
# methods -> get/post  considers get as default if no method is mentioned

def welcome():
    return "<h1>Flask Demo it is!!</h1>"

@app.route("/index", methods = ["GET"])

def index():
    return "<h2>Welcome to Index page</h2>"

@app.route('/success/<int:score>') # can give parameters to the success page as well
                        # its called variable - rule.
# also can write it as ('/success/<int : score>')
# and inside func write str(sdore)
def success(score):
    return "The person has passed and the score is : " + str(score)

@app.route('/fail/<int:score>')

def fail(score):
    return "The person has failed and the score is : " + str(score)

@app.route('/form', methods = ["GET","POST"])
def form(): # importing render template and a request library at the beginning
    if request.method == "GET":
        return render_template('form.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])
        average_marks = (maths+science+history)/3

        #return render_template('form.html', score = average_marks)

        res = ""
        if average_marks >= 50:
            res = "success"
        else:
            res = "fail"
        
        return redirect(url_for(res, score = average_marks))
    

@app.route('/api', methods = ["POST"])
def calculate_sum():
    data = request.get_json()
    a_val = float(dict(data)['a'])
    b_val = float(dict(data)['b'])
    return jsonify(a_val+b_val)


if __name__ == "__main__":
    app.run(debug = True) 

