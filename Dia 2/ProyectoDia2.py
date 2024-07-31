x = 13
y = 100
name = input("What is your name: ")
sales = input("How many sales have you had: ")
commission = round(int(sales)*x/y, 2)
print(f"The salesman {name} did {sales} sales and the commission is ${commission}")
