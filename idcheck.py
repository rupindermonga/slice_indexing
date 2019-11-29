
import string

alphas = string.ascii_letters
nums = string.digits

print("Welcome to the Identifier Checker v1.0")
print("Testees must be at least 2 chars long.")
myInput = input("Identifier to test? ")

if len(myInput) > 1:
    if myInput[0] not in alphas:
        print("invalid: first symbol must be alphabetic")
    else:
        for otherChar in myInput[1:]:
            if otherChar not in alphas + nums:
                print("Invalid: remaining symbols must be alphanumeric")
                exit()
        print("Okay as an identifier")
            
else:
    print("Input more than 1 char")
