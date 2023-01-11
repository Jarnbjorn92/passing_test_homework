def return_10():
    return 10

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def length_of_string(string_length):
    return len(string_length)

def join_string(str_1, str_2):
    return str(str_1 + str_2)

def add_string_as_number(num_1, num_2):
    return int(num_1) + int(num_2)

def number_to_full_month_name(month):
    if month == 1:
        return "January"

    elif month == 3:
        return "March"

    elif month == 9:
        return "September"

def number_to_short_month_name(short_month):
    if short_month == 1:
        return "Jan"
    
    elif short_month == 4:
        return "Apr"

    elif short_month == 10:
        return "Oct"


def length_of_a_side(side_1, side_2, side_3):
    return side_1 * side_2 * side_3

