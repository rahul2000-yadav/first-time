income=int(input("Enter the income:"))
if income<=150000:
    print("Not tax")
elif income<=300000:
    Amount=income-income*0.1
    print(f"Salary is{Amount} after 10% tax cut down")
elif income<=500000:
    Amount=income-income*0.2
    print(f"Salary is{Amount} after 20% tax cut down")
elif income>500000:
    Amount=income-income*0.3
    print(f"Salary is{Amount} after 30% tax cut down")
