from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from database import register_student,login_student

app = Flask(__name__)


@app.route('/')
def home(): 
    return render_template('Main.html')


@app.route("/student")
def student():
    return render_template("student.html")


@app.route("/student/login", methods=["POST"])
def student_login():

    email = request.form["email"]
    password = request.form["password"]

    print("Email:", email)
    print("Password:", password)

    return "Login successful"


@app.route("/student/register", methods=["POST"])
def student_register():

    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    confirm_password = request.form["confirm_password"]

    print("Name:", name)
    print("Email:", email)

    return "Registration successful"



@app.route('/Admin')
def admin():
    return render_template('Admin.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')    


@app.route('/tutor')
def tutor():
    return render_template('tutor.html')

if __name__ =='__main__':
    app.run(debug=True)