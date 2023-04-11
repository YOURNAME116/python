class person:
    name = "utshav"
    age = "20"
    gender = "male"

    def greet(self):
        return(f"Good morning {self.name} ")
    
if __name__ == '__main__':
    person1=person()
    print (person1.greet())
