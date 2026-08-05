#Input

password = input("Enter Password: ")

#Processing
#minimum length criteria

has_min_length = len(password)>=8

#number criteria

has_digit = any(map(str.isdigit, password))

#contains upper case
has_upper = password.lower() != password

score = has_min_length + has_digit + has_upper

# Output
if score == 3:
    print("Strong Password")
elif score ==2:
    print("Weak Password")
else:
    print("Very weak password")