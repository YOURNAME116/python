def outer_function(word):
    def inner_function(addingtext):
        return(word+" "+addingtext)
    return inner_function

func=outer_function("hello")
print(func("utshav"))
