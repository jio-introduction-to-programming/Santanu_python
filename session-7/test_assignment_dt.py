from assignment_dt import (
    datetime_to_str_1, datetime_to_str_2, datetime_to_str_3, datetime_to_str_4, datetime_to_str_5,
    datetime_to_str_6, datetime_to_str_7, datetime_to_str_8, datetime_to_str_9, datetime_to_str_10,
    str_to_datetime_1, str_to_datetime_2, str_to_datetime_3, str_to_datetime_4, str_to_datetime_5,
    str_to_datetime_6, str_to_datetime_7, str_to_datetime_8, str_to_datetime_9, str_to_datetime_10
)
from datetime import datetime

# datetime to string tests
def test_datetime_to_str_1():
    assert datetime_to_str_1(datetime(2023, 7, 19)) == "2023-07-19"

def test_datetime_to_str_2():
    assert datetime_to_str_2(datetime(2023, 7, 19)) == "23-07-19"

def test_datetime_to_str_3():
    assert datetime_to_str_3(datetime(2023, 7, 19)) == "July 19, 2023"

def test_datetime_to_str_4():
    assert datetime_to_str_4(datetime(2023, 7, 19)) == "Jul 19, 2023"

def test_datetime_to_str_5():
    assert datetime_to_str_5(datetime(2023, 7, 19)) == "19 July 2023"

def test_datetime_to_str_6():
    assert datetime_to_str_6(datetime(2023, 7, 19)) == "Wednesday July 19, 2023"

def test_datetime_to_str_7():
    assert datetime_to_str_7(datetime(2023, 7, 19)) == "Wed July 19, 2023"

def test_datetime_to_str_8():
    assert datetime_to_str_8(datetime(2023, 7, 19, 10, 30, 45)) == "2023-07-19 10:30:45"

def test_datetime_to_str_9():
    assert datetime_to_str_9(datetime(2023, 7, 19, 10, 30, 45)) == "10:30:45"

def test_datetime_to_str_10():
    assert datetime_to_str_10(datetime(2023, 7, 19, 10, 30, 45)) == "10:30 AM"

# string to datetime tests
def test_str_to_datetime_1():
    assert str_to_datetime_1("2023-07-19") == datetime(2023, 7, 19)

def test_str_to_datetime_2():
    assert str_to_datetime_2("23-07-19") == datetime(2023, 7, 19)

def test_str_to_datetime_3():
    assert str_to_datetime_3("July 19, 2023") == datetime(2023, 7, 19)

def test_str_to_datetime_4():
    assert str_to_datetime_4("Jul 19, 2023") == datetime(2023, 7, 19)

def test_str_to_datetime_5():
    assert str_to_datetime_5("19 July 2023") == datetime(2023, 7, 19)

def test_str_to_datetime_6():
    assert str_to_datetime_6("Wednesday July 19, 2023") == datetime(2023, 7, 19)

def test_str_to_datetime_7():
    assert str_to_datetime_7("Wed July 19, 2023") == datetime(2023, 7, 19)

def test_str_to_datetime_8():
    assert str_to_datetime_8("2023-07-19 10:30:45") == datetime(2023, 7, 19, 10, 30, 45)

def test_str_to_datetime_9():
    assert str_to_datetime_9("10:30:45") == datetime(1900, 1, 1, 10, 30, 45)  # Default date is set to Jan 1, 1900

def test_str_to_datetime_10():
    assert str_to_datetime_10("10:30 AM") == datetime(1900, 1, 1, 10, 30)  # Default date is set to Jan 1, 1900 and 24-hour format is used
