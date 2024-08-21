

rent = int(input("enter you flat rent:"))
food = int(input("enter the amount of food ordered:"))
electricity_spend= int(input("enter the total of electricity spend :"))
charge_per_unit = int(input("enter the charge per unti="))

person = int(input("enter the persons living in the room :"))

total_bill=electricity_spend*charge_per_unit
output = (rent+food+electricity_spend+charge_per_unit)//person
print(output)