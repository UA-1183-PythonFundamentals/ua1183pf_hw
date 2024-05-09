# Task 3

def calculate_number_of_char(str):
    """
    Calculate number of characters in string and return

    With loop check every char in str and check the count of this char in word

    Arguments:
    arg1 (str): Some string

    :return:
    dict with key(char):value(count)
    """
    result = {}
    str = str.lower()

    for char in str:
        result[char] = str.count(char)

    return result
