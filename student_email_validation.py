
def validate_email(email):
    return "@" in email and "." in email.split("@")[-1]


print(validate_email("student@example.com"))
