#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

#input
print("Welcome to tip calculator")
people = int(input("Enter total number of people to split the tip? : "))
bill = float(input("Enter to bill amount to split?: $"))
tip = int(input("Enter tip percentage you would like to give: "))
#Process
tip_in_percentage = tip / 100
total_tip_amount = tip_in_percentage * bill
total_bill = bill + total_tip_amount
amount_per_person = total_bill / people
final_bill_per_person = "{:.2f}".format(amount_per_person)

#output
print("==============================================")

print(f"Each person should pay:  ${final_bill_per_person}")
