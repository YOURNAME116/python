class kiranapasal:
    def Sum_of_groceries():
        total=0
        
        while (True):
            userinput=(input("keep entering your price  \n"))

            # try:
            if (userinput != "q"):
                    total = total + int(userinput)
                    
            else:
                    print(f"your bill total is {total}")
                    break
            # except:
            
           # print("enter only the numeric form")
        return total    
mijas=kiranapasal
print(mijas.Sum_of_groceries())
            
