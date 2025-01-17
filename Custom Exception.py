class AgeTooLow(Exception):

    def __init__(self, age):
        self.age = age
        super().__init__(f"Age {age} is too low. Minimum age is 18")

def check_age(age):
    if age < 18:
        raise AgeTooLow(age)
    else:
        print(f"Age {age} is valid.")

try:
    age = int(input("Enter your age: "))
    check_age(age)

except AgeTooLow as e:
    print(e)