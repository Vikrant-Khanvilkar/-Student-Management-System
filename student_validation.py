
def validate_student(name, roll_no):
    if name.strip() and roll_no > 0:
        return True
    return False


print(validate_student("Vikrant", 19))
