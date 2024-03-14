from flask import Flask

# creating a simple flask application

app = Flask(__name__)  # entry point of program

if __name__ == "__main__":
    app.run(debug = True)  #debug is true coz it prevents from  letting the server stop whenever the code is updated or changed
    # also app.run makes the flask web server run
    # app.run func takes 2 input parameters by default
    # 1st input : we are giving no url so it considers local host
    # 2nd input : port number - by default - 5000

    
