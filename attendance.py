
def calculate_attendance(attended_days, total_days):

    if total_days <= 0:
        raise ValueError("Total days must be greater than zero")

    percentage = (attended_days / total_days) * 100

    return round(percentage, 2)


def check_eligibility(percentage):

    if percentage >= 75:
        return "Shortage"
    else:
        return "Eligible"


# Main program

attended = 85
total = 100

percentage = calculate_attendance(attended, total)

status = check_eligibility(percentage)

print("Employee Attendance Management")

print("Total Working Days:", total)
print("Days Attended:", attended)
print("Attendance Percentage:", percentage)

print("Attendance Status:", status)
