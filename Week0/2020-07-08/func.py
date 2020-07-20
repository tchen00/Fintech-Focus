# Built in methods
print("tammy".upper())

# Built in methods 
print(len("tammy"))

# Define function
def shout(name): 
    name = name.upper()
    return 'HELLO ' + name + "!"

# Call the function
print(shout("tammy"))

# Function with multiple arguments
def personalized_age_check(name,age):
    if age > 18: 
        return "Congrats " + name + "! You are old enough to vote."
    else: 
        time_left = 18 - age 
        return "Sorry " + name + ". You can't vote for another " + str(time_left) + " years."

print(personalized_age_check("tammy", 12))

# Functions with default arguments 
def create_user(name="Tammy"): 
    return "Your username is " + name

print(create_user())


# Scope
age = 20 
def have_a_birthday(): 
    global age 
    age += 1
    return age 

print(have_a_birthday())