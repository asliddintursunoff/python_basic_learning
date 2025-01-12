import re

while True:
    password = input("\nenter your pasword: ")
    pattern = re.compile(r"[A-Za-z0-9@#$%^&+=]{8,}\d")
    checking= pattern.fullmatch(password)
   
    if checking==None:
        print("Please enter true password")
    else:
        print("You did it correct!!")
        break
    
                         
    
