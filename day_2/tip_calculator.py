#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tips calculator!")
total_bill = float(input("What is the total billed amount? $"))
tips_percent = int(input("How many percent of tips you would like to give? 10, 12, or 15? "))
total_person = int(input("How many people would like to split the bill? "))

bill_with_tips_per_person = (total_bill / total_person) * (tips_percent / 100 + 1)
print(f"Bill for each person are: ${bill_with_tips_per_person:.2f}")
