
import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Read attendance threshold from environment variable
# If it is not set, use 75 as the default value
ATTENDANCE_THRESHOLD = int(
    os.environ.get("ATTENDANCE_THRESHOLD", 75)
)


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

    # Compare attendance percentage with configured threshold
    if percentage >= ATTENDANCE_THRESHOLD:
        status = "Eligible"
    else:
        status = "Shortage"

    return f"""
        <h1>Attendance Result</h1>

        <p>Employee Name: {employee_name}</p>

        <p>Total Working Days: {total_days}</p>

        <p>Days Attended: {attended_days}</p>

        <p>Attendance Percentage: {percentage:.2f}%</p>

        <p>Required Attendance: {ATTENDANCE_THRESHOLD}%</p>

        <p>Attendance Status: {status}</p>

        <a href="/">Go Back</a>
    """


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port)
