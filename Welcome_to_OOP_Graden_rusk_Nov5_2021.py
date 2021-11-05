#--------
#Welcome_To_OOP
#Graden_Rusk
#Nov_4_2021
#--------

#---classes---#
class Students():
    
    taxes = .11
    
    def __init__(self, first, age, mark, gender, money):
        self.name = first
        self.age = age
        self.mark = mark
        self.gender = gender
        self.cost = float(money)
        self.info =  'Name: ' + first + '\nAge: ' + age + "\nMark: " + average + "\nGender: " + gender + "\nMoney spent: " + money + "$"
    
    def pos(self):
        self.cost = int(money)
        self.cost = int(self.cost * self.taxes)
        
class Teachers(Students):
    taxes = .15
    
    def __init__(self, first, age, mark, gender, money, classes):
        super().__init__(first, age, mark, gender, money)
        self.classes = classes
        
#----code here----#
name = input("What is your name?\n>>>" )
age = input("What is your age?\n>>>" )
average = input("What is your average?\n>>>" )
gender = input("What is your gender?\n>>>" )
money = (input("How much money did you spend this year?\n>>>" ))
staff = input("Are you a Teacher?\n>>>" )
if staff == 'yes':
    classes = input("How many classes do you teach?\n>>>" )
    person = Teachers(name, age, average, gender, money, classes)
else:
    person = Students(name, age, average, gender, money)
print(person.info)
person.pos()
print(f"You have to pay", person.cost,"$ in taxes.")
if staff == 'yes':
    print(f"You also teach", person.classes, "classes.")
 

