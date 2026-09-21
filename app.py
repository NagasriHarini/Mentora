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

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        data = request.get_json()

        student_id = login_student(data)

        if student_id:
            return jsonify({
                "success": True,
                "message": "Login successful!",
                "redirect": "/dashboard"
            })

        return jsonify({
            "success": False,
            "message": "Invalid Student ID or password."
        })

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        data = request.get_json()

        student_id = register_student(data)

        return jsonify({
            "success": True,
            "message": "Registration successful!",
            "redirect": f"/registration-success/{student_id}"
        })

    return render_template('register.html')

@app.route('/registration-success/<int:student_id>')
def registration_success(student_id):

    return render_template(
        'registration_success.html',
        student_id=student_id
    )


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