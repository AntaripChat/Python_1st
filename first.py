# write a program - take input from user 1 - 10

num = int(input("Enter any number between 1 - 10: "))

while num < 1 or num > 10:
    num = int(input("Your Number Not Between 1 - 10: "))
print(f"Your Number Is {num}") 

