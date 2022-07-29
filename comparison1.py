name = input("enter your name")
#print (len(name))
if len(name) < 4:
     print("your can't add name less then three characters")
elif len(name) > 50:
     print("your can't add name more then fifty characters")
else:
     print("looks good name")