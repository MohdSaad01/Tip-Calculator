print("Welcome to the tip calculator)")

Bill = float(input("What was the total bill? $"))

Tip= int(input("What percentage tip would you like to give? 10 12 15 !"))

Total_bill=Tip/100*Bill+Bill

people =int(input("How many people to split the bill? "))

Total_amount=Total_bill/people
Payable=round(Total_amount,2)

print(f"Each person should pay:{Payable}")