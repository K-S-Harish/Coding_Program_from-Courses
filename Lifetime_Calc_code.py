age = input()
age_limit = 90#assuming that an average person lives for 90 years.
years_left = age_limit-int(age)#converted the age from STR to INT before subtracting
weeks_left = years_left*52#Assuming that there are 52 weeks in a year.
print(f"\nYou have {weeks_left} weeks left in this Lifetime.")