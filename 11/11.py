#wap to demonstrate the use of method overriding and overloading


#Method Overriding:
class Hm:
    def huh(self):
        return "Hm hai bhai"

class Huh(Hm):
    def huh(self):
       return "huh in huh what bhai"

obj1= Hm()
obj2 = Huh()

print(obj1.huh())  # calling base class method using object obj1
print(obj2.huh())  # calling derived class method using object obj2


#Method OverLoading:
class Bruh:
    def combine_strings(self, *args):
        if len(args) == 1:
            return args[0]
        else:
            return ' '.join(args)


b = Bruh()

print(b.combine_strings("Bhai "))  
print(b.combine_strings("Now", "Ok"))  
print(b.combine_strings("?", "or", "i change more?"))

#Method OverLoading 2nd way: 
class Add:
     def addd(self, a,b=0):
         return  a+b
hm = Add()
print(hm.addd(34,56))
print(hm.addd(34))

