class Employee:
    language = "Python"     # This is class attribute
    salary = 120000

emp1 = Employee()
emp1.name = "Nazim"       # This is an instance attribute
print(emp1.name,emp1.language,emp1.salary)

# Instance attribute take preference over the class attribute 
emp2 = Employee()         
emp2.name = "Harish"
emp2.language = "Java"      
print(emp2.name,emp2.language,emp2.salary)      # Ouput -> Harish Java 1200000

