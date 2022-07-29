try:
    age = int(input("enter your age: "))
    income = 20000
    risk = income / age
    print(age)
    print(risk)
except ZeroDivisionError:
    print("cannot divided by zero")
except ValueError:
    print("enter valid age")