# # ZeroDivisionError
# def divide(a,b):
#     try:
#         result = a / b
#         print(result)
#     except ZeroDivisionError as e:
#         print("Do not divide by Zero")

# divide(10,2)
# divide(10,0)

# User Input 

# try: 
#     number = int(input("Enter a number: "))
# except ValueError as e:
#     print(type(e))
#     print({e})

# Files 

# try:
#     with open("blablalba.txt",'r') as file: 
#         content = file.read()
#         print(content)
# except Exception as e:
#     print(e)

# Finally , Else 

try: 
    number = int(input("Enter a number: ")) # ValueError
    result = 100 / number #ZeroDivisionError
    # Check for exeptions
except ValueError:
    print("Enter a number please")
except ZeroDivisionError:
    print("Cant enter 0")
except Exception as e:
    print(e)
    # If there are no exceptions
else: 
    print(result)
    # Always Runs
finally:
    print("Completed")

