# 02/11/26 
# Encapsulation

# class Employee:
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self._salary = salary


#     def get_salary(self):
#         return self._salary


#     def inc_salary(self, amount):
#         if amount >0:
#             self._salary += amount
#             print("Salary updated")
#         else:
#             print("Invalid amount")
# emp=Employee("Shailesh",25,50000)
# print("Salary:",emp.get_salary())

# emp.inc_salary(8000)
# print("New Balance:",emp.get_salary())


# Inheritance

#single inheritance


# class Animal():

#     def property(self):
#         print("Animal has 4 leg")

# class Dog(Animal):

#     def bark(self):
#         print("Dog barks")
        
# d=Dog()
# d.bark()
# d.property()

#Multiple inheritance

# class Father():

#     def skill1(self):
#         print("Driving")
# class Mother():

#     def skill2(self):
#         print("cooking")

# class child(Father,Mother):

#     def Qualities(self):
#         print("Inherited skills from parents:")

# x=child()
# x.Qualities()
# x.skill1()
# x.skill2()


# multilevel inheritance

# class Grandfather():

#     def house(self):
#         print("Grandfather's house")

# class Father(Grandfather):

#     def bike(self):
#         print("Father's bike")

# class Son(Grandfather):

#     def laptop(self):
#         print("Son's Laptop")


# class Grandson(Father,Son):   

#     def car(self):
#         print("Grandson's car")


# g=Grandson()
# g.house()
# g.bike()
# g.laptop()





#Hierarchial Inheritance

# class Institute():

#     def name(self):
#         print("NSTIW Allahabad")

# class Teacher(Institute):
#     pass
# class Student(Institute):
#     pass
# class Housekeeping(Institute):
#     pass


# t=Teacher()
# s=Student()
# h=Housekeeping()

# s.name()
# t.name()
# h.name()

# Classwork

# 02/11/2026

# 1. Student Management System (Single Inheritance)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# class Student(Person):
#     def __init__(self, name, age, roll_no, course):
#         super().__init__(name, age)
#         self.roll_no = roll_no
#         self.course = course

#     def display_student(self):
#         self.display_details()
#         print("Roll No:", self.roll_no)
#         print("Course:", self.course)


# s1 = Student("Shreya", 26, 101, "AIPA")
# s1.display_student()


#2 Bank Account System (Single Inheritance)

# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposit:", amount)


# class SavingAccount(BankAccount):
#     def __init__(self, account_number, balance, interest_rate):
#         super().__init__(account_number, balance)
#         self.interest_rate = interest_rate

#     def calculate_interest(self):
#         interest = self.balance * self.interest_rate / 100
#         print("Account Number:", self.account_number)
#         print("Balance:", self.balance)
#         print("Interest Rate:", self.interest_rate, "%")
#         print("Interest Earned:", interest)


# b1 = SavingAccount(409489, 10000, 5)
# b1.deposit(5000)
# b1.calculate_interest()


#3. Family Assets (Multilevel Inheritance)

# class Grandfather:
#     def house(self):
#         print("Grandfather's  house")


# class Father(Grandfather):
#     def bike(self):
#         print("Father's  bike")


# class Son(Father):
#     def laptop(self):
#         print("Son has a laptop")


# s1 = Son()
# s1.house()
# s1.bike()
# s1.laptop()

#4.Employee Hierarchy (Multilevel Inheritance)

# class Person:
#     def get_name(self):
#         print("Name: Shreya")


# class Employee(Person):
#     def salary(self):
#         print("Salary: 50000")


# class Manager(Employee):
#     def team_size(self):
#         print("Team Size: 3")


# m1 = Manager()
# m1.get_name()
# m1.salary()
# m1.team_size()


#5. College Management System (Hierarchical Inheritance)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Student(Person):
#     def __init__(self, name, age, marks):
#         super().__init__(name, age)
#         self.marks = marks

#     def display(self):
#         print("Student Name:", self.name)
#         print("Age:", self.age)
#         print("Marks:", self.marks)


# class Teacher(Person):
#     def __init__(self, name, age, subject):
#         super().__init__(name, age)
#         self.subject = subject

#     def display(self):
#         print("Teacher Name:", self.name)
#         print("Age:", self.age)
#         print("Subject:", self.subject)


# s1 = Student("Shreya", 22, 85)
# t1 = Teacher("Shailesh", 35, "Python")

# s1.display()
# print("--------------")
# t1.display()


# 6. Vehicle Management System (Hierarchical Inheritance)

# class Vehicle:
#     def start(self):
#         print("Vehicle is starting")


# class Car(Vehicle):
#     def air_condition(self):
#         print("Car has Air Conditioner")


# class Bike(Vehicle):
#     def helmet_required(self):
#         print("Helmet is required")


# class Bus(Vehicle):
#     def passenger_capacity(self):
#         print("Passenger Capacity: 50")


# c1 = Car()
# b1 = Bike()
# bus1 = Bus()

# print("Car:")
# c1.start()
# c1.air_condition()

# print("Bike:")
# b1.start()
# b1.helmet_required()

# print("Bus:")
# bus1.start()
# bus1.passenger_capacity()


# 7. Smart Phone System (Multiple Inheritance)

# class Camera:
#     def take_photo(self):
#         print("Taking Photo")


# class MusicPlayer:
#     def play_music(self):
#         print("Playing Music")


# class SmartPhone(Camera, MusicPlayer):
#     def make_call(self):
#         print("Making a Call")


# s1 = SmartPhone()
# s1.take_photo()
# s1.play_music()
# s1.make_call()


# 8. Working Student (Multiple Inheritance)

# class Student:
#     def study(self):
#         print("Student is studying")


# class Employee:
#     def work(self):
#         print("Employee is working")


# class WorkingStudent(Student, Employee):
#     def manage_time(self):
#         print("Managing Time")


# w1 = WorkingStudent()
# w1.study()
# w1.work()
# w1.manage_time()


# 9. Company Structure (Hybrid Inheritance)

# class Employee:
#     def attendance(self):
#         print("Employee attendance marked")


# class Developer(Employee):
#     def write_code(self):
#         print("Developer is writing code")


# class Tester(Employee):
#     def test_software(self):
#         print("Tester is testing software")


# class TeamLead(Developer, Tester):
#     def manage_team(self):
#         print("Team Lead is managing the team")


# t1 = TeamLead()
# t1.attendance()
# t1.write_code()
# t1.test_software()
# t1.manage_team()


# 10. Educational Institute (Hybrid Inheritance)


# class Person:
#     def display_name(self):
#         print("Name: Shreya")


# class Student(Person):
#     def study(self):
#         print("Student is studying")


# class Teacher(Person):
#     def teach(self):
#         print("Teacher is teaching")


# class Mentor(Student, Teacher):
#     def guide(self):
#         print("Mentor is guiding students")


# m1 = Mentor()
# m1.display_name()
# m1.study()
# m1.teach()
# m1.guide()