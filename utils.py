def show_menu():
    print("""Main menu:
    1.- Enter text
    2.- Number of uppercase letters and lowercase letters
    3.- Is the string a date?
    4.- Number of total punctuation characters
    5.- Count user punctuation characters
    6.- Get usernames
    7.- Exit
    """)

def get_option():
    exit = False
    result = ""
    while not exit:
        option = input("What do you want to do?: ")
        if option.isdigit():
            result = int(option)
            exit = True
        else:
            print("The selected option needs to be an integer number: ")
    return result


def get_punctuation_characters():
    exit = False
    while not exit:
        punctuation = input("Enter a string with only punctuation characters")
        if is_punctuation_string_correct(punctuation):
            exit = True
        else:
            print("One of your characters is not a punctuation mark.")
    return punctuation


def get_text():
    exit = False
    result = ""
    while not exit:
        text = input("Enter a string with at least 10 characters: ")
        if len(text) >= 10:
            result = text
            exit = True
        else:
            print("The text must have 10 or more characters ", end="")
    return result


def upper_lower(text):
    count_l = 0
    count_u = 0
    for c in text:
        if c.islower():
            count_l += 1
        elif c.isupper():
            count_u += 1
    return count_l, count_u


def print_option2_results(count_l, count_u):
    print("The number of lowercase letters is", count_l)
    print("The number of uppercase letters is", count_u)


def correct_month(month):
    correct_month = True
    if month.isdigit() and len(month) == 2:
        # check if day is correct
        if int(month) < 1 or int(month) > 12:
            correct_month = False
    else:
        correct_month = False
    return correct_month


def is_leap_year(year):
    int_year = int(year)
    return (int_year % 4 == 0) and (int_year % 100 != 0 or int_year % 400 == 0)


def max_day(month, year):
    if month == "02":
        if is_leap_year(year):
            max_day = 29
        else:
            max_day = 28
    elif month == "09" or month == "04" or month == "06" or month == "11":
        max_day = 30
    else:
        max_day = 31
    return max_day


def correct_day(day, month, year):
    correct_day = True
    if day.isdigit() and len(day) == 2:
        # check if day is correct
        m_day = max_day(month, year)
        correct_day = int(day) >= 1 and int(day) <= m_day
    else:
        correct_day = False
    return correct_day


def correct_year(year):
    return year.isdigit() and len(year) == 4


def is_it_a_date(text):
    correct_date = True
    date_list = text.split("-")
    if len(date_list) == 3:
        day = date_list[0]
        month = date_list[1]
        year = date_list[2]
        correct_date = correct_date and correct_month(month) and correct_year(year)
        if correct_date:
            correct_date = correct_date and correct_day(day, month, year)
        else:
            correct_date = False
    else:
        correct_date = False
    return correct_date


def count_punctuation_c(text, punctuation):
    import string
    count = 0
    for c in text:
        if c in punctuation:
            count += 1
    return count


def is_punctuation_string_correct(punctuation_string):
    import string
    i = 0
    is_correct = True
    while i < len(punctuation_string) and is_correct:
        if not punctuation_string[i] in string.punctuation:
            is_correct = False
        i += 1
    return is_correct



