from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/attendance", methods=["POST"])
def calculate_attendance():

    employee_name = request.form["employee_name"]

    total_days = int(request.form["total_days"])

    attended_days = int(request.form["attended_days"])

    if total_days <= 0 or attended_days < 0 or attended_days > total_days:
        return "Invalid attendance values", 400

    percentage = (attended_days / total_days) * 100

    if percentage >= 75:
        status = "Eligible"
    else:
        status = "Shortage"

    return f"""
        <h1>Attendance Result</h1>

        <p>Employee Name: {employee_name}</p>

        <p>Total Working Days: {total_days}</p>

        <p>Days Attended: {attended_days}</p>

        <p>Attendance Percentage: {percentage:.2f}%</p>

        <p>Attendance Status: {status}</p>

        <a href="/">Go Back</a>
    """


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


# if __name__ == "__main__":

    # app.run(host="0.0.0.0", port=5000)