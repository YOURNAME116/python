def greet(func):
    def modified():
        print("Good morning Utshav")
        func()
        print("you have sucessfully modified the function")
    return modified
@greet 
def pandatapasvi():
    print("what are you doing right now")


pandatapasvi()
