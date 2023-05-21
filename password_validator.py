def is_valid_length(password):
    return 6 <= len(password) <= 10


def contain_alpha_and_number(password):
    return password.isalnum()


def contain_at_least_2_digits(password):
    digits_counter = 0
    for ch in password:
        if ch.isdigit():
            digits_counter += 1

    return digits_counter >= 2


input_password = input()

is_valid = True

if not is_valid_length(input_password):
    is_valid = False
    print("Password must be between 6 and 10 characters")

if not contain_alpha_and_number(input_password):
    is_valid = False
    print("Password must consist only of letters and digits")

if not contain_at_least_2_digits(input_password):
    is_valid = False
    print("Password must have at least 2 digits")

if is_valid:
    print("Password is valid")
