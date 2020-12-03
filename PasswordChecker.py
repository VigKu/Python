# Define a Function to check the strength of a Password

#(i) length between 8 and 24,
def hasProperLength(password):
    if 8 < len(password) < 24:
        return True
    return False
    
# (ii) at least one uppercase character,
def hasUpperCase(password):
    flag = False
    for i in password:
        if i.isupper():
            flag = True
            break
    return flag
            

# (iii) at least one lowercase character,
def hasLowerCase(password):
    flag = False
    for i in password:
        if i.islower():
            flag = True
            break     
    return flag


# (iv) at least one digit,
def hasDigit(password):
    flag = False
    for i in password:
        if i.isdigit():
            flag = True
            break     
    return flag

# (v) at least one special character amongst !@#%&*    
def hasSpecChar(password):
    flag = False
    list1 = "!@#%&*"
    for i in password:
        if list1.find(i) >= 0:
            flag = True
            break     
    return flag 

# (vi) no spaces in between
def hasNoSpace(password):
    if password.find(" ") < 0:
        return True
    return False

def isGoodPassword(password):
    ''' Checks whether an input password is 'Good' or 'Bad'.
        input : password (string)
        output : True / False (bool)
    '''
    # Write your code here (to check password strength)
    # Remember to return either True or False at the end
    len_flag = False
    uc_flag = False
    lc_flag = False
    digit_flag = False
    specchar_flag = False
    nospace_flag = False
    
    len_flag = hasProperLength(password)
    uc_flag = hasUpperCase(password)
    lc_flag = hasLowerCase(password)
    digit_flag = hasDigit(password)
    specchar_flag = hasSpecChar(password)
    nospace_flag = hasNoSpace(password)
    
    # bitwise addition
    res_flag = len_flag & uc_flag & lc_flag & digit_flag & specchar_flag & nospace_flag
    
    return res_flag
    


# Call the function with a Password
print(isGoodPassword("AI6120@NTUSingapore"))