from assignment import ( add_one_to_number, add_two_numbers, subtract, 
                        sum_first_n_natural_numbers, divide_x_by_y_float, 
                        remainder_x_by_y, divide_x_by_y_numeric )

def test_add_one_to_number():
    assert add_one_to_number(1) == 2 
    assert add_one_to_number(5) == 6 

def test_add_two_numbers():
    assert add_two_numbers(5, 7) == 12 
    assert add_two_numbers(-4, -8) == -12 

def test_subtract():
    assert subtract(9, 11) == -2  
    assert subtract(-2, -2) == 0 
    assert subtract(100, 3) == 97 

def test_sum_first_n_natural_numbers():
    assert sum_first_n_natural_numbers(1) == 1 
    assert sum_first_n_natural_numbers(2) == 3 
    assert sum_first_n_natural_numbers(3) == 6 
    assert sum_first_n_natural_numbers(10) == 55 
    assert sum_first_n_natural_numbers(100) == 5050

def test_divide_x_by_y_float():
    assert divide_x_by_y_float(0, 12) == 0.0
    assert divide_x_by_y_float(90, 2) == 45.0
    assert divide_x_by_y_float(2, 10) == 0.2
    assert divide_x_by_y_float(-18, 36) == -0.5


def test_divide_x_by_y_numeric():
    assert divide_x_by_y_numeric(0, 12) == 0
    assert divide_x_by_y_numeric(90, 2) == 45
    assert divide_x_by_y_numeric(2, 10) == 0
    assert divide_x_by_y_numeric(-18, 36) == -1 

def test_remainder_x_by_y():
    assert remainder_x_by_y(10, 2) == 0
    assert remainder_x_by_y(0, 5) == 0
    assert remainder_x_by_y(27, 4) == 3 
    assert remainder_x_by_y(987, 10) == 7 
    assert remainder_x_by_y(93, 12) == 9 