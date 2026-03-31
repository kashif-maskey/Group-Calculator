def division(a, b):
    try:
        result = a/b;
        return result;
    except ZeroDivisionError:
        print("Division by zero not possible");