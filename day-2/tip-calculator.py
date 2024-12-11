print('Welcome to the tip calculator!')
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give (10,12,15): "))
num_people = int(input("How many people to split the bill? "))
total_tip = total_bill * (tip_percent / 100)
bill_per_person = (total_bill + total_tip) / num_people
print(round(bill_per_person, 2))


