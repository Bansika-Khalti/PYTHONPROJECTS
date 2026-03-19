password = input("Enter your password: ")
has_number = any(char.isdigit() for char in password)
has_letter = any(char.isalpha() for char in password)
is_strong = has_number and has_letter and len(password) >= 8
print("Password strong? " + str(is_strong))