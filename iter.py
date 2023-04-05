
class iteration:
    def __init__(self):
        self.number=1
    def __iter__(self):
        return self
    def __next__(self):
       
            val = self.number
            self.number+=1
            return val
      
           
        
levelup = iteration()
for i in levelup:
    print (i)