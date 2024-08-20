def check_my_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older")
    print("Valid")



try:
    check_my_age(8)
except ValueError as e:
    print(f"Error: {e}")


