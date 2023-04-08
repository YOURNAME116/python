class Employee:
    company = "Apple"
    def info(self):
        return(f"The name is {self.name} and company is {self.company}")
    @classmethod
    def changecompany(cls , newcompany):
        cls.company=newcompany
    

e1=Employee()
e1.name="utshav"
print(e1.info())
print(e1.company)
(e1.changecompany("tyfon"))
print(e1.info())
print(e1.company)
print(Employee.company)
