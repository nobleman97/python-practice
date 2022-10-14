# print("hello")

# name = input('What is your name?\n')
# print("Hello",  name)

# ---
# greeting = "Welcome to my first Calculator"

# print(greeting);

# totalBill = input("What is Your Toatl Bill? $")
# people = input("How many people will split this? ")
# tip = input("How much Percent tip to give? ")

# answer = (float(totalBill) + (float(totalBill) * (float(tip) / 100))) / float(people)

# print(f"Each Person would have to pay ${round(answer, 2)}")
# ---

# Days in weeks

# convert age to days and subtract from days in 90 year, convvert back to week
week = 7;
# daysInAYear = 365;
weeksInAYear = 52;
ageLimit = 90;

weekLimit = (ageLimit * weeksInAYear)

age = input("What is your current age? \n")
age = int(age)

ageInWeeks = age * weeksInAYear;

print(f"total weeks lived is {ageInWeeks}\n")
print(f"You have {weekLimit - ageInWeeks} weeks left to live\n")

print("Spend them wisely")




