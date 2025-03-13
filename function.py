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

