# Team 15

#!/usr/bin/env python3

__author__ = "Aidan Kelley, Ryan Hirscher, Conor Rybacki"
__copyright__ = "Copyright 2021"
__credits__ = [""]
__license__ = "GPLv3"
__version__ = "3.8.7"
__maintainer__ = ""
__email__ = "akelley1@highpoint.edu, rhirsche@highpoint.edu, crybacki@highpoint.edu"
__status__ = "Complete"

def main():

    data = open("password.txt", "r")

    passwordList = data.read().splitlines()
    #print(passwordList)

    num_of_passwords = passwordList[0]
    passwordList.pop(0)

    # validArray = [False]*num_of_passwords

    #print(passwordList)


    symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*']
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for password in passwordList:
        valid = True

        upper = False
        lower = False
        number = False
        symbol = False
        white = True

        other = True

        if len(password) <8 or len(password) >32:
            valid = False

        if password[0] in nums:
            valid = False
            #print("NO ", password)

        for char in password:
            if char in symbols:
                symbol = True
            if ord(char) in range(48, 58): # numbers
                number = True
            if ord(char) in range(97, 123): #lowercase
                lower = True
            if ord(char) in range(65, 91): #Uppercase
                upper = True
            if ord(char) == 32: #White space
                white = False
            # if (ord(char) not in range(97, 123)) or (ord(char) not in range(65, 91)) or (ord(char) not in range(48, 58)):
            #     other = False
            # if char not in symbol:
            #     other = False
        if (symbol and number and lower and upper and white and valid and other):
            print("YES", password)
        else:
            print("NO ", password)


#     Passwords must have,
#
# 1)      8 to 32 characters
#
# 2)      at least one numeric digit
#
# 3)      at least one uppercase letter
#
# 4)      at least one lowercase letter
#
# 5)      at least one symbol from the set ~!@#$%^&*
#
# 6)      must not have other characters than the above
#
# 7)      starting character must not be a number




if __name__ == "__main__":
    main()
