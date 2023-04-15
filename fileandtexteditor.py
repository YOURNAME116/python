
import os
# import keyboard


class File:
    def __init__(self, file_name):
        self.file = file_name

    def read(self):
        with open(self.file, "r") as f:
            return f.read()

    def create(self):
        with open(self.file, "x"):
            pass

    def write(self):
        with open(self.file, "w") as f:

            for i in range(500):

                if i == 0:
                    text = input(
                        "Enter the text here to write into the file or press q to quit:\n""")
                    f.write(text + "\n")
                if text.capitalize() == "Q":
                    exit()

                text = input("")
                f.write(text + "\n")

    def delete(self):
        name = input("Enter the name of the file you want to delete:")
        os.remove(name)
    def append(self):
         with open(self.file, "a") as f:

            for i in range(500):

                if i == 0:
                    text = input(
                        "Enter the text here to write into the file or press q to quit:\n""")
                    f.write(text + "\n")
                if text.capitalize() == "Q":
                    exit()

                text = input("")
                f.write(text + "\n")


    def rename(self):
        while (True):
            self.fileRename = input(
                f"Enter the new file name of {self.file}: ")
            if os.path.exists(self.fileRename):
                print("file exist give a different name:\n")
                continue
            else:
                os.rename(self.file, self.fileRename)
                break

    @classmethod
    def ask(self):
        self.command = (input(
            "what do you want to do:\n 1.read file \n 2.write file\n 3.append on the file\n 4.delete file\n 5.rename file\n 6.create the file 7.'q' to quit\n"))

        def commanding():
            
            self.file = input("enter the name of the  file you want to edit: ")
            file=File(self.file)
            try:
                if int(self.command) == 6 :
                    
                    
                    if os.path.exists(self.file):
                        
                        file.create()
                

                        if self.command[0] != "q":
                            try:
                                self.command = int(self.command)
                                try:

                                    if self.command <= 6:

                                        try:
                                            if self.command == 1:

                                                print(file.read())
                                            elif self.command == 2:
                                                file.write()
                                            elif self.command == 3:
                                                file.append()
                                            elif self.command == 4:
                                                file.delete()
                                            elif self.command == 5:
                                                file.rename()
                                            
                                        

                                        except ValueError:
                                            print("enter a input integer or 'q' to exit")
                                    else:
                                        print(
                                            "please enter a valid self.command form 1-5 or enter q to exit:")
                                        commanding()
                                except ValueError:
                                    print(
                                        "Please enter a valid input from 1-5 or enter q to exit \n\n")
                                    commanding()
                            except ValueError:
                                print("Enter the valid input please")
                        else:
                            exit()
                    else:
                        print("file don't exists")
            except FileExistsError:
                print("file exists")
        commanding()
          


if __name__ == '__main__':
    File.ask()
