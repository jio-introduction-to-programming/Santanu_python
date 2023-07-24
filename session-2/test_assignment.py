from assignment import (convert_to_int, find_max_of_numbers, get_char_from_num,
                        get_num_from_char, calculate_sum_of_numbers, check_type_of_value,
                        check_any_true_in_list, check_all_true_in_list, get_current_time)

def test_convert_to_int():
    assert convert_to_int('5') == 5
    assert convert_to_int('0') == 0
    assert convert_to_int('-3') == -3

def test_find_max_of_numbers():
    assert find_max_of_numbers([1, 2, 3, 4, 5]) == 5
    assert find_max_of_numbers([-1, -2, -3, -4, -5]) == -1
    assert find_max_of_numbers([0]) == 0

def test_get_char_from_num():
    assert get_char_from_num(65) == 'A'
    assert get_char_from_num(97) == 'a'
    assert get_char_from_num(48) == '0'

def test_get_num_from_char():
    assert get_num_from_char('A') == 65
    assert get_num_from_char('a') == 97
    assert get_num_from_char('0') == 48

def test_calculate_sum_of_numbers():
    assert calculate_sum_of_numbers([1, 2, 3, 4, 5]) == 15
    assert calculate_sum_of_numbers([-1, -2, -3, -4, -5]) == -15
    assert calculate_sum_of_numbers([0]) == 0

def test_check_type_of_value():
    assert check_type_of_value(5) == int
    assert check_type_of_value('hello') == str
    assert check_type_of_value([1, 2, 3]) == list

def test_check_any_true_in_list():
    assert check_any_true_in_list([0, False, None]) == False
    assert check_any_true_in_list([0, 1, False]) == True

def test_check_all_true_in_list():
    assert check_all_true_in_list([1, True, 'hello']) == True
    assert check_all_true_in_list([1, 0, 'hello']) == False

def test_get_current_time():
    import time
    assert abs(get_current_time() - time.time()) < 3600  # tested within 3600 seconds
