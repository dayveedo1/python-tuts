# define the class

class Employee:

    def __init__(self, name, dept, address, nationality):
        self.name = name
        self.dept = dept
        self.address = address
        self.nationality = nationality

    def display(self):
        print("Name: " + self.name,
              "; Dept: " + self.dept,
              "; Address: " + self.address,
              "; Nationality: " + self.nationality)
