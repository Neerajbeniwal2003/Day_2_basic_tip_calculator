print("welcome to the tip calculator:)")
total_bill=int(input("enter your total bill amount? $"))
per=int(input("How much tip would you like to give? 10,12 or 15 :"))
people=int(input("How many people to split the bill?:"))

total_with_tip=round(((per/100)*total_bill+total_bill)/people,2)

print(f'Each person should pay:{total_with_tip} $')
