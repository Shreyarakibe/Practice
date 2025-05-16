# #DEFAULT CONSTRUCTOR
# class Details:            
#     def __init__(self):
#         print("Hey I am person")

# a = Details()

# #PARAMETERIZED CONSTRUCTOR
# class person:                  
#     def __init__(self, name, occ):
#         self.name= name
#         self.occ = occ

#     def info(self):
#         print(f"Hey I am {self.name} and I am a {self.occ}")    

# b = person("Shreya", "Student")  
# b.info()  


# GETTERS AND SETTERS 
# class Myclass:
#     def __init__(self, value):
#         self._value = value

#     def show(self):
#         print(f"The value is {self._value}")    

#     @property
#     def ten_value(self):
#         return 10 * self._value

#     @ten_value.setter    
#     def ten_value(self, new_value):
#         self._value = new_value/10

# obj = Myclass(10)   
# obj.show()     

# obj.ten_value = 20
# print(obj.ten_value)
# obj.show()

#INHERITANCE
# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     def showDetails(self):
#         print(f"The name of the employee: {self.id} is {self.name}")

# class Programmer(Employee):
#     def showLanguage(self):
#         print("The default language is Python") 

# e1 = Employee("Shreya", 101)
# e1.showDetails()
# e2 = Programmer("Samiksha", 102)
# e2.showDetails()
# e2.showLanguage()  

# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     def showDetails(self):
#         print(f"The name of the employee: {self.id} is {self.name}")

# class Programmer(Employee):
#     def showLanguage(self):
#         print("The default language is Python") 

# e1 = Employee("Shreya", 101)
# e1.showDetails()
# e2 = Programmer("Samiksha", 102)
# e2.showDetails()
# e2.showLanguage()  
