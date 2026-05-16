import sys

def value_cleaner (dirty_value):
    no_spaces=dirty_value.strip()
    filtered=''
    accepted='-.0123456789'

    for character in no_spaces:
        if character in accepted:
            filtered+=character
    return filtered        