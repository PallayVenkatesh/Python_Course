books = {"ISA":60, "Python":20, "ASE":80,"web":50, "mobile":90}

minimum = int(input("Enter  minimum price"))
maximum = int(input("Enter  maximum price"))

a = True

for (key,value) in books.items():
    if minimum <= value <= maximum:
     if a:
         print('Available books for the price range', minimum, 'and', maximum,'are:')
         a = False
     print(key)
    else:
     exit