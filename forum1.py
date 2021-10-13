import math

# USER INPUT THE NUMERATOR AND DENOMINATOR FOR THE PROGRAM

while True:
    try:
        numerator = eval(input("Enter the numerator (value must be larger than 0): ")) 
        if 0 <= numerator:
            break;
        else:
            print("Please enter a positive number")      
    except ValueError:
        print("Invalid")
    continue
while True:
    try:
        denominator = eval(input("Enter the denominator (value must be larger than 0) : ")) 
        if 0 <= denominator:
            break;
        else:
            print("Please enter a positive number")      
    except ValueError:
        print("Invalid")
    continue

# CHECKING THE LARGEST COMMON DIVISOR FOR TH FRACTION

num2 = math.gcd(numerator, denominator)

#DEFINING THE FRACTION

if numerator < denominator:
# To define if the fraction is proper or improper
    print(numerator, '/', denominator, 'is a proper fraction')
elif numerator >= denominator:
    print(numerator, '/', denominator, 'is an improper fraction')

#REDUCING THE FRACTION

if num2 != 1 :
# Check if the fraction has been reduced or not
    numerator2 = numerator / num2
    denominator2 = denominator / num2
    print('This improper fraction can be reduced to', int(numerator2), '/', int(denominator2))
else:
    print('This improper fraction cannot be reduced any further')

#TO FIND OUT IF THE FRACTION IS A MIXED FRACTION OR A WHOLE NUMBER

if num2 != 1 and denominator2 != 1:
    mixed = numerator2 // denominator2
    numerator3 = numerator2 - denominator2
    print('The mixed number is ',int(mixed), 'and', int(numerator3), '/', int(denominator2))
elif denominator == 1 or denominator2 == 1 :
    if num2 != 1 :
        print('The whole number is', int(numerator2))
    else:
        print('The whole number is', int(numerator))
else:
    mixed = numerator // denominator
    numerator4 = numerator - denominator * mixed
    print('The mixed number is',int(mixed), 'and', int(numerator4), '/', int(denominator))