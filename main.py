
###########    PRINT  ###################
#Printing string
print("*************PRINTING STRINGS**************")
print("Helo World")
print("I am learning python")

#Printing numbers
print("************PRINTING NUMBERS************")
print(36)
print(36.7)

#Printing a statement that has strings and integers in python in different formats
print("************Printing a statement that has string and integer in python in different format***********")
#1
print  ("Paramole" +  " Akanimodo" + " from"  + " Nigeria" " is " + str( 36))
#2
print  ("Paramole" +  " Akanimodo" + " from"  + " Nigeria" " is " + " 36")
#3
print(f"Paramole Akanimodo from Nigeria is {36}")


##########  ARITHMETICS   ###################
print("********ARITHMETICS********")
#Mathematical calculations in Python
print("**********Mathematical calculations in Python********")
print(6+3)
print(6*3)
print(6/3)
print(6-3)

######## CONCANTINATING ARITHMETICS AND STRINGS   ##########
print("***********CONCANTINATING ARITHMETICS AND STRINGS ***********")
#convert days to seconds
print("*************convert days to seconds**********")
print(f"20 days are {20*24*60*60} seconds")
print(f"40 days are {40*24*60*60} seconds")
print(f"63 days are {63*24*60*60} seconds")
print(f"91 days are {91*24*60*60} seconds")

########    VARIABLES     ##########
print("******** VARIABLES **********")
to_seconds = 24*60*60
name_of_unit = "seconds"

print(f"20 days are {20*to_seconds} {name_of_unit}")
print(f"40 days are {40*to_seconds} {name_of_unit}")
print(f"63 days are {63*to_seconds} {name_of_unit}")
print(f"91 days are {91*to_seconds} {name_of_unit}")

#######  FUNCTION ########
print("********* FUNCTION ********")

to_seconds = 24*60*60
name_of_unit = "seconds"
 ###### Declaring Function #########
def days_to_unit():
    print(f"20 days are {20 * to_seconds} {name_of_unit}")
    print("ALL good")

##### Calling a Function #######
days_to_unit()

###### using a function within a program ########
def days_to_unit(numer_of_days):
    print(f"{numer_of_days} days are {numer_of_days * to_seconds} {name_of_unit}")
    print("ALL good")

##### Calling a Function #######
days_to_unit(20)
days_to_unit(40)
days_to_unit(63)
days_to_unit(91)

###### passing multiple parameters into a function ########
def days_to_unit(numer_of_days, custom_message):
    print(f"{numer_of_days} days are {numer_of_days * to_seconds} {name_of_unit}")
    print(custom_message)

##### Calling a Function #######
days_to_unit(20, "All good")
days_to_unit(40, "Very good")
days_to_unit(63, "All good")
days_to_unit(91, "Very good")


###### ACCEPTING USER INPUT  ############
print("**********ACCEPTING USER INPUT*********")
user_input = input("Hi, Enter number of days!\n") #\n moves cursor to the next line after executing code
print(user_input)

####### FUNcTION WITH RETURN VALUE ######################
print("************** FUNcTION WITH RETURN VALUE **************")
def days_to_unit(numer_of_days):
    return (f"{numer_of_days} days are {numer_of_days * to_seconds} {name_of_unit}")

my_var = days_to_unit(20)
print(my_var)


############## ACCEPTING USER INPUT IN A FUNCTION #########
print("****** ACCEPTING USER INPUT IN A FUNCTION *****")
def days_to_unit(numer_of_days):
    return (f"{numer_of_days} days are {numer_of_days * to_seconds} {name_of_unit}")

user_input = input("Hi, Enter number of days!\n") #\n moves cursor to the next line after executing code
user_input_number = int(user_input)
calculated_value = days_to_unit(user_input_number)
print(calculated_value)

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
