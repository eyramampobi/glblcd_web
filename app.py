from flask import Flask, render_template, request
import database

user_logins= {
    "eyramampobi" : "jujutsu",
    "juliasroda" : "sweedie"
}

app = Flask(__name__)

@app.route('/',methods = ["GET","POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        email = request.form["email1"]
        password = request.form["password1"]
        
        if user_logins.get(email) == None:
            return render_template('error.html')
        elif user_logins.get(email) != password:
            return render_template("error.html")
        else:
            return render_template("homepage.html")
        

    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='3000')