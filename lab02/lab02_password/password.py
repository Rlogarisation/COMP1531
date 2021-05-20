
def check_password(password):
    '''
    Takes in a password, and returns a string based on the strength of that password.

    The returned value should be:
    * "Strong password", if at least 12 characters, contains at least one number, 
    at least one uppercase letter, at least one lowercase letter.

    * "Moderate password", if at least 8 characters, contains at least one number.
    * "Poor password", for anything else
    * "Horrible password", if the user enters "password", "iloveyou", or "123456"
    '''
    contain_number = False
    contain_uppercase = False
    contain_lowercase = False
    length = len(password)
    for character in password:
        if character.isdigit():
            contain_number = True
        if character.isupper():
            contain_uppercase = True
        if character.islower():
            contain_lowercase = True
    

    if (length >= 12 and contain_number and contain_uppercase and contain_lowercase):
        return("Strong password")
    elif (length >= 8 and contain_number):
        return("Moderate password")
    elif (password == "password" or 
    password == "iloveyou" or password == "123456"):
        return("Horrible password")
    else:
        return("Poor password")

if __name__ == '__main__':
    print(check_password("goodweather1"))

