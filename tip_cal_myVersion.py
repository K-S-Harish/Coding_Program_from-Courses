#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")
amount = float(input("What was the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
head_count = int(input("How many people to split the bill? "))
tip_per_indv = (amount*(tip_percentage/100))/head_count
amount_per_indv = (amount/head_count) + (tip_per_indv)
#--- We print the amount and round it of to 2 decimal points.
#--- Remember the decimal points can be adjusted the value of ".2f" to .3f,.4f....etc
print(f"Each person should pay: ${amount_per_indv:.2f}")
