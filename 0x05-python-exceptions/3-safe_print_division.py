#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a/b
    except: ZeroDivisionError:  # Catch division by zero
        result = None
     except TypeError:  # Catch invalid types (if a or b is not a number)
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
