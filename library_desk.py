# Practical 1: College Library Desk
# Python Basics and Operators

# Taking member details from user
name = input("Enter Member Name: ")
age = int(input("Enter Member Age: "))
books = int(input("Enter Borrowed Books: "))
student = input("Are you  a Student? (yes/no): ").lower() == "yes"

late_fee = 50.0
books += 1
check_name ='a' in name.lower()

eligible = (student is True) and (age > 17) and (books < 5)


# Displaying formatted membership summary
print("\n-----Collage library Desk ---")

print("Student Name:", name)
print(" Age:", age)
print("Books Borrowed:", books)
print("Student Status:", student)
print("Fine :", late_fee)
print("Student:" "Yes" if student else "No")
print("Contains letter 'a':", check_name)
print("Eligible:", "eligible" if eligible else "Not Eligible")