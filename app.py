
import os
import logging

from flask import Flask, render_template, request

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# Create Flask application
app = Flask(__name__)

# Read attendance threshold from environment variable
ATTENDANCE_THRESHOLD = int(
    os.environ.get("ATTENDANCE_THRESHOLD", 75)
)


# Home page
@app.route("/")
def home():
    logger.info("Home page accessed")

    return render_template("index.html")

#Health check
@app.route("/health")
def health_check():

    logger.info("Health check requested")

    return {
        "status": "healthy",
        "application": "Employee Attendance System"
    }, 200

# Attendance calculation
@app.route("/attendance", methods=["POST"])
def calculate_attendance():

    logger.info("Attendance calculation requested")

    employee_name = request.form["employee_name"]
    total_days = int(request.form["total_days"])
    attended_days = int(request.form["attended_days"])

    # Validate attendance values
    if total_days <= 0 or attended_days < 0 or attended_days > total_days:

        logger.warning("Invalid attendance values received")

        return "Invalid attendance values", 400

    # Calculate attendance percentage
    percentage = (attended_days / total_days) * 100

    logger.info(
        "Attendance calculated for employee: %s",
        employee_name
    )

    # Check attendance eligibility
    if percentage >= ATTENDANCE_THRESHOLD:
        status = "Eligible"
    else:
        status = "Shortage"

    logger.info("Attendance status: %s", status)

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


# Start Flask application
if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    logger.info("Starting Employee Attendance Application")

    app.run(host="0.0.0.0", port=port)
