#27/oct/26
#1.Practical
# Age Verification System
 
# try:
#     user_age = int(input("Enter your age: "))

#     if user_age < 0 or user_age > 120:
#         raise ValueError("Age is out of range")

#     print("Age verified successfully")

# except ValueError as error:
#     print("Invalid age:", error)

# 2.Practical
# Product Price Manager

# try:
#     item_cost = int(input("Enter product price: "))

#     if item_cost < 0:
#         raise ValueError("Price cannot be negative")

#     print("Valid price:", item_cost)

# except ValueError as error:
#     print("Price error:", error)

# # 3.
# # Tuple Element Access


# places = ("Varanasi", "Bhopal", "Patna",
#           "Agra", "Jaipur", "Indore", "Ranchi")

# try:
#     index_no = int(input("Enter city position (0-6): "))
#     print("Selected city:", places[index_no])

# except IndexError:
#     print("Error: Position does not exist")

# except ValueError:
#     print("Enter a valid integer")


#  4.
# Contact Information Lookup

# phone_book = {
#     "Deepa": "9123405678",
#     "Kavya": "9876123405",
#     "Shreya": "9012345678"
# }

# try:
#     contact = input("Enter contact name: ")
#     print("Mobile number:", phone_book[contact])

# except KeyError:
#     print("Contact is not available")

# 5.
# File Writing Opration 


# try:
#     file_name = input("Enter file name: ")
#     message = input("Enter your message: ")

#     with open(file_name, "w") as output_file:
#         output_file.write(message)

#     print("Data saved successfully")

# except PermissionError:
#     print("You do not have permission to write this file")

# except OSError as error:
#     print("File error:", error)


# 6.
#Valid Roll Number Input


# while True:
#     try:
#         roll_no = int(input("Enter student roll number: "))

#         if roll_no <= 0:
#             print("Roll number must be positive")
#             continue

#         print("Accepted roll number:", roll_no)
#         break

#     except ValueError:
#         print("Please enter numbers only")


# 7.
# Custom Exception for Voting Eligibility


# class VotingAgeError(Exception):
#     pass

# try:
#     voter_age = int(input("Enter voter age: "))

#     if voter_age < 18:
#         raise VotingAgeError("Minimum age is 18")

#     print("Eligible for voting")

# except VotingAgeError as error:
#     print("Error:", error)

# except ValueError:
#     print("Enter age as an integer")

# 8.
#Bank Account Deposit Validation


# try:
#     deposit = int(input("Enter deposit amount: "))

#     if deposit <= 0:
#         raise ValueError("Deposit must be above zero")

#     print("Amount deposited:", deposit)

# except ValueError as error:
#     print("Deposit error:", error)

# 9.
# Shopping Cart Quantity Check


# try:
#     item_quantity = int(input("Enter item quantity: "))

#     if item_quantity < 1:
#         raise ValueError("Quantity should be at least 1")

#     print("Items added:", item_quantity)

# except ValueError as error:
#     print("Error:", error)


# 10 .
#Password Strength Validato


# try:
#     user_password = input("Create a password: ")

#     if len(user_password) < 8:
#         raise ValueError("Use at least 8 characters")

#     print("Password accepted")

# except ValueError as error:
#     print("Password error:", error)

# 11 .
# Student Grade Calculator

# try:
#     science = int(input("Enter Science marks: "))
#     english = int(input("Enter English marks: "))
#     computer = int(input("Enter Computer marks: "))

#     score_list = [science, english, computer]

#     if any(mark < 0 or mark > 100 for mark in score_list):
#         raise ValueError("Marks must be between 0 and 100")

#     total_score = sum(score_list)
#     percentage = total_score / 3

#     print("Total marks:", total_score)
#     print("Percentage:", round(percentage, 2), "%")

# except ValueError as error:
#     print("Invalid input:", error)

# 12 .
# ATM PIN Verification


# class InvalidPINError(Exception):
#     pass

# saved_pin = "4826"

# try:
#     for attempt_no in range(3):
#         entered_pin = input("Enter ATM PIN: ")

#         if entered_pin == saved_pin:
#             print("PIN verified")
#             break
#         else:
#             print("Incorrect PIN")

#     else:
#         raise InvalidPINError("All three attempts failed")

# except InvalidPINError as error:
#     print("Error:", error)

# 13 .
# Email Address Validator


# try:
#     email_id = input("Enter your email: ")

#     if "@" not in email_id or "." not in email_id:
#         raise ValueError("Email must contain @ and .")

#     print("Email accepted")

# except ValueError as error:
#     print("Invalid email:", error)

# 14 .
# Division of List Elements

# values = [12, 24, 36, 0, 48]

# try:
#     first_pos = int(input("Enter numerator index: "))
#     second_pos = int(input("Enter denominator index: "))

#     answer = values[first_pos] / values[second_pos]
#     print("Division result:", answer)

# except IndexError:
#     print("Error: Index is out of range")

# except ZeroDivisionError:
#     print("Error: Cannot divide by zero")

# except ValueError:
#     print("Please enter integer indexes")

# 15 .
#Username Availability Checker


# class UsernameTakenError(Exception):
#     pass

# registered_users = ["Deepa24", "Shreya07", "Peehu15"]

# try:
#     new_user = input("Choose a username: ")

#     if new_user in registered_users:
#         raise UsernameTakenError("Username already exists")

#     print("Username is unavailable")

# except UsernameTakenError as error:
#     print("Error:", error)


# 16 .
# Electricity Bill Calculator

# try:
#     consumed_units = int(input("Enter electricity units: "))

#     if consumed_units < 0:
#         raise ValueError("Units cannot be negative")

#     total_bill = consumed_units * 6

#     print("Total electricity bill: Rs.", total_bill)

# except ValueError as error:
#     print("Invalid units:", error)

# 17 .
# Student Record Search

# student_data = {
#     211: {"name": "Shreya", "trade": "AIPA"},
#     212: {"name": "Deepa", "trade": "COPA"},
#     213: {"name": "Siwani", "trade": "AIPA"}
# }

# try:
#     search_id = int(input("Enter student ID: "))
#     print("Record:", student_data[search_id])

# except KeyError:
#     print("Student record not found")

# except ValueError:
#     print("Student ID must be numeric")

# 18 .
# Mobile Number Validation

# try:
#     mobile_no = input("Enter 10-digit mobile number: ")

#     if not mobile_no.isdigit() or len(mobile_no) != 10:
#         raise ValueError("Mobile number must have 10 digits")

#     print("Mobile number accepted")

# except ValueError as error:
#     print("Validation error:", error)

# 18 .
# Online Ticket Booking

# class SeatLimitError(Exception):
#     pass

# seats_left = 20

# try:
#     requested = int(input("How many tickets do you need? "))

#     if requested < 1:
#         raise ValueError("At least one ticket is required")

#     if requested > seats_left:
#         raise SeatLimitError("Requested tickets exceed available seats")

#     seats_left -= requested

#     print("Tickets booked successfully")
#     print("Seats remaining:", seats_left)

# except SeatLimitError as error:
#     print("Booking error:", error)

# except ValueError as error:
#     print("Invalid quantity:", error)

# 20 .
# Number Range Validator


# try:
#     entered_number = int(input("Enter a number from 1 to 50: "))

#     if not 1 <= entered_number <= 50:
#         raise ValueError("Number is outside the allowed range")

#     print("Accepted number:", entered_number)

# except ValueError as error:
#     print("Invalid number:", error)
