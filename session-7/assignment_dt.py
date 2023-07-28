from datetime import datetime

# datetime to string
def datetime_to_str_1(dt):
    return dt.strftime('%Y-%m-%d') # Convert to format "2023-07-19"

def datetime_to_str_2(dt):
    return dt.strftime('%y-%m-%d') # Convert to format "23-07-19"

def datetime_to_str_3(dt):
    return dt.strftime('%B %d, %Y') # Convert to format "July 19, 2023"

def datetime_to_str_4(dt):
    return dt.strftime('%b %d, %Y') # Convert to format "Jul 19, 2023"

def datetime_to_str_5(dt):
    return dt.strftime('%d %B %Y')# Convert to format "19 July 2023"

def datetime_to_str_6(dt):
    return dt.strftime('%A %B %d, %Y') # Convert to format "Wednesday July 19, 2023"

def datetime_to_str_7(dt):
    return dt.strftime('%a %B %d, %Y') # Convert to format "Wed July 19, 2023"

def datetime_to_str_8(dt):
    return dt.strftime('%Y-%m-%d %X')# Convert to format "2023-07-19 10:30:45"

def datetime_to_str_9(dt):
    return dt.strftime('%X') # Convert to format "10:30:45"

def datetime_to_str_10(dt):
    return dt.strftime('%I:%M %p')  # Convert to format "10:30 AM"

# string to datetime
def str_to_datetime_1(s):
    return datetime.strptime(s,'%Y-%m-%d') # Convert from format "2023-07-19"

def str_to_datetime_2(s):
    return datetime.strptime(s,'%y-%m-%d') # Convert from format "23-07-19"

def str_to_datetime_3(s):
    return datetime.strptime(s,'%B %d, %Y') # Convert from format "July 19, 2023"

def str_to_datetime_4(s):
    return datetime.strptime(s,'%b %d, %Y') # Convert from format "Jul 19, 2023"

def str_to_datetime_5(s):
    return datetime.strptime(s,'%d %B %Y') # Convert from format "19 July 2023"

def str_to_datetime_6(s):
    return datetime.strptime(s,'%A %B %d, %Y') # Convert from format "Wednesday July 19, 2023"

def str_to_datetime_7(s):
    return datetime.strptime(s, '%a %B %d, %Y') # Convert from format "Wed July 19, 2023"

def str_to_datetime_8(s):
    return datetime.strptime(s,'%Y-%m-%d %X') # Convert from format "2023-07-19 10:30:45"

def str_to_datetime_9(s):
    return datetime.strptime(s, '%X') # Convert from format "10:30:45"

def str_to_datetime_10(s):
    return datetime.strptime(s, '%I:%M %p') # Convert from format "10:30 AM"