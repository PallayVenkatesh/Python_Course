import re
password = input("Please input your password which needs to be verified?")
flag = True
while flag:
    if (len(password)<6 or len(password)>12):
        break
    elif not re.search("[$#@]",password):
        break
    elif not re.search("[a-z]",password):
        break
    elif not re.search("[A-Z]",password):
        break
    elif not re.search("[0-9]",password):
        break
    elif re.search("\s",password):
        break
    else:
        print("Valid Password")
        flag=False
        break

if flag:
    print(" Password Is Not Valid")