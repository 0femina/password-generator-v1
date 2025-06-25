#password generator first version, and my first git project. 
#it generates secure passwords with options for numbers and symbols

#we start by importing the chaos we will need
import random #used to randomly pick characters for the password
import string #gives us access to letters, digits, punctuation
#idea for later: turn this into a username generator too 

#the main function: will build a password based on given options
def generate_password(min_length, numbers=True, special_characters=True): #je déclare ma fonction et les caractéristiques du mdp que je vais générer
    """
    generates a random password with a minimum length
    includes letters by default, and optionally numbers and special characters
    """
    #we start by defining our character pools
    #define letter/digit/symbol sets using clear variable names
    letters = string.ascii_letters #A-Z and a-z
    digits = string.digits  #0-9
    special = string.punctuation #special characters, the !@#$%& stuff
    # it starts with letters by default, then add more if requested
    characters = letters #base character set, will expand if needed
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    #initialize the password and validation flags
    pwd = ""
    meets_criteria = False #false by default and will be True once the password is valid
    has_number = False
    has_special = False

    #we set a loop that adds characters until we meet the criteria AND have the required length
    while not meets_criteria or len(pwd) < min_length: 
        new_char = random.choice(characters) #pick a random character from the final set
        pwd += new_char #we add these new characters to the password

    #we check if the new  character is a digit or a special symbol
        if new_char in digits : 
            has_number = True
        elif new_char in special :
            has_special = True
        
        #validate based on user preferences
        meets_criteria = True # assume it's valid for now
        if numbers: 
            meets_criteria = has_number # must include a number
        if special_characters:
            meets_criteria = meets_criteria and has_special # must include special too if asked
    
    return pwd  #finally return the generated password

#now we get our user input and turn the responses into usable booleans
min_length = int(input("Enter the minimum length : "))
has_number = input("Do you want to have numbers ? (y/n) ").lower() == "y"
has_special = input("Do you want to have special characters ? (y/n) ").lower() == "y" # if the user answers anything other than 'y', we treat it as False

#we generate and print the final result
pwd = generate_password(min_length, has_number, has_special)
print("The generated password is : ", pwd)
