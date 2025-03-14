###### ACCEPTING USER INPUT  ############
print("**********ACCEPTING USER INPUT*********")
user_input = input("Hi, Enter number of days!\n") #\n moves cursor to the next line after executing code
print(user_input)

############## ACCEPTING USER INPUT IN A FUNCTION #########
print("****** ACCEPTING USER INPUT IN A FUNCTION *****")
def days_to_unit(numer_of_days):
    return (f"{numer_of_days} days are {numer_of_days * to_seconds} {name_of_unit}")

user_input = input("Hi, Enter number of days!\n") #\n moves cursor to the next line after executing code
user_input_number = int(user_input)
calculated_value = days_to_unit(user_input_number)
print(calculated_value)