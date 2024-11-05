# Python compound interest calculation

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0 :
        print("Principle can't be less then or equal to zero")


while rate <= 0:
    rate = float(input("Enter the interset rate: "))
    if rate <= 0 :
        print("Rate can't be less then or equal to zero")


while time <= 0:
    time = int(input("Enter the time: "))
    if time <= 0 :
        print("Time can't be less then or equal to zero")


total = principle * pow(1 + rate/100,time)

print(f"Balance After {time} years : {total} Rs")