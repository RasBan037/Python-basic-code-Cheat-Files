#### CONDITIONALS (IF/ELSE) & BOOLEAN DATA TYPE #######
print("********* CONDITIONALS (IF/ELSE) & BOOLEAN DATA TYPE **********")
def days_to_unit(numer_of_days):
    if numer_of_days>0:
        return (f"{numer_of_days} days are {numer_of_days * to_seconds} {name_of_unit}")
    else:
        return "You entered a negative value, cannot be converted"
user_input = input("Hi, Enter number of days!\n") #\n moves cursor to the next line after executing code
user_input_number = int(user_input)
calculated_value = days_to_unit(user_input_number)
print(calculated_value)



 #### MULTIPLE CONDITIONALS (IF/ELSE)  #######
print("********* MULTIPLE CONDITIONALS (IF/ELSE)**********")
def days_to_unit(numer_of_days):
    if numer_of_days>0:
        return (f"{numer_of_days} days are {numer_of_days * to_seconds} {name_of_unit}")
    elif numer_of_days == 0:
        return"Please enter a valid value"
    else:
        return "You entered a negative value, cannot be converted"
user_input = input("Hi, Enter number of days!\n") #\n moves cursor to the next line after executing code
if user_input.isdigit():
        user_input_number = int(user_input)
        calculated_value = days_to_unit(user_input_number)
        print(calculated_value)
else:
    print("Only accepts number")

###CLEAN UP CODE##########
print("********* MULTIPLE CONDITIONALS (IF/ELSE)**********")
def days_to_unit(numer_of_days):
    if numer_of_days>0:
        return (f"{numer_of_days} days are {numer_of_days * to_seconds} {name_of_unit}")
    elif numer_of_days == 0:
        return"Please enter a valid value"
    else:
        return "You entered a negative value, cannot be converted"

def validagte_code():
    if user_input.isdigit():
        user_input_number = int(user_input)
        calculated_value = days_to_unit(user_input_number)
        print(calculated_value)
    else:
        print("Only accepts number")

user_input = input("Hi, Enter number of days!\n") #\n moves cursor to the next line after executing code
validagte_code()