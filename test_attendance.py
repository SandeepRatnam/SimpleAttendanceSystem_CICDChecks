
from attendance import calculate_attendance, check_eligibility


def test_attendance_calculation():

    assert calculate_attendance(85, 100) == 85.0


def test_eligible_employee():

    assert check_eligibility(85) == "Eligible"


def test_employee_with_shortage():

    assert check_eligibility(60) == "Shortage"


def test_zero_total_days():

    try:
        calculate_attendance(10, 0)

    except ValueError:
        assert True

    else:
        assert False
