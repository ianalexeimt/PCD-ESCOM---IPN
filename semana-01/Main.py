import sys

def value_cleaner (dirty_value):
    no_spaces=dirty_value.strip()
    filtered=''
    accepted='-.0123456789'

    for character in no_spaces:
        if character in accepted:
            filtered+=character
    return filtered        

def line_processor (original_line):
    total=0
    parts=original_line.split(',')

    for part in parts:
        clean_part=value_cleaner(part)
        try:
            clean_part=float(clean_part)
            clean_part=int(clean_part)
            total+=clean_part
        except ValueError:
            pass
    return total