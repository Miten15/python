#wap to demonstrate the use of simple and mutli inhertens

class Huh:
    def __init__(self, name, sal):
        self.name = name
        self.sal = sal

class Dek(Huh):
    def display_info(self):
        print("Name : ", self.name)
        print("Salary : ", self.sal)

#creating object of class Dek
obj1 = Dek("John",  5000)

print("\nDisplaying information using display_info method")
obj1.display_info()


#Multiple Inheritance
class Work:
    def work(self):
        print("What type of work he doing")

class Coding(Work):
    def code(self):
        print("He is coding")

class Designing(Work):
    def design(self):
        print("He is designing")

class Developer(Coding,Designing):

    def __init__(self, name):
      self.name = name

    def show_work(self):
        Work.work(self)
        Coding.code(self)
        Designing.design(self)

dev = Developer("em")
print("Hes name is:",dev.name)
dev.show_work()


  





    
 


