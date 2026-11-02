# #28/10/26

# # OPPS Concept

# class Aipa:
#     def __init__(self,name,roll_no,trade,marks): #__init__= constructor
#         self.name=name
#         self.roll_no=roll_no
#         self.trade=trade
#         self.marks=marks

# std1=Aipa("Khushi","1","AIPA",90)
# std2=Aipa("Arsh",2,"AIPA",90)

# print(std1.name)
# print(std1.roll_no)
# print(std1.trade)
# print(std1.marks)

# print(std2.name)
# print(std2.roll_no)
# print(std2.trade)
# print(std2.marks)


# class Student:
#     def __init__(self,name,roll_no,trade,marks): #contructor
#         self.name=name
#         self.roll_no=roll_no
#         self.trade=trade
#         self.marks=marks

    # def display_details(self):
    #     print("Name:",self.name)
    #     print("Roll No:",self.roll_no)
    #     print("Trade:",self.trade)
    #     print("Marks:",self.marks)

#     def check_result(self):
#         if self.marks >=40:
#             print("Pass")
#         else:
#             print("Fail")

#     def percentage(self,total_marks):
#         return (self.marks/total_marks)*100

# student1=Student("Anushka",1,"AIPA",76)
# student2=Student("Shreya",2,"AIPA",87)

# student1.display_details()
# student1.check_result()
# print(student1.percentage(100), "%")
# student2.display_details()
# student2.check_result()




# class Car:
#     def __init__(self, brand, model, color, price, speed):
#         self.brand = brand
#         self.model = model
#         self.color = color
#         self.price = price
#         self.speed = speed

#     def display_details(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Color:", self.color)
#         print("Price:", self.price)
#         print("Speed:", self.speed)

#     def check_price(self):
#         if self.price >= 2000000:
#             print("Expensive Car")
#         else:
#             print("Budget Car")

#     def check_speed(self):
#         if self.speed >= 200:
#             print("Highest Speed")
#         elif self.speed >= 80:
#             print("Average Speed")
#         else:
#             print("Low Speed")

#     def discount(self, discount_percentage):
#         return self.price - (self.price * discount_percentage / 100)


# car1 = Car("BMW", "X6", "White", 5000000, 110)
# car2 = Car("Mahindra", "Thar", "Black", 1500000, 110)

# car1.display_details()
# car1.check_price()
# car1.check_speed()
# print("Price after discount:", car1.discount(20))

# car2.display_details()
# car2.check_price()
# car2.check_speed()
# print("Price after discount:", car2.discount(10))