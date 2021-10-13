import math
# Loop so that program can run again immediately if need be
program = 0
while program == 0:
    # Inputs
    Numerator = eval(input("Enter a Numerator, Value must be > 0 : "))
    while Numerator <= 0:
        Numerator = eval(input("Please re-enter a Numerator, Value must be > 0 : "))
    Denominator = eval(input("Enter a Denominator, Value must be > 0 : "))
    while Denominator <= 0:
        Denominator = eval(input("Please re-enter a Denominator, Value must be > 0 : "))
    # Driver
    gcd = math.gcd(Numerator, Denominator)
    gcdn = Numerator//gcd; gcdd = Denominator//gcd; whole = Numerator//Denominator
    if Denominator > Numerator:
        print(f"{Numerator}/{Denominator} is a proper fraction.")
        if gcd == 1:
            print("This proper fraction cannot be reduced any further.")
        else:
            print(f"The proper fraction can be reduced further to become: {gcdn}/{gcdd}")
    else:
        gcc = math.gcd(gcdn,gcdd)
        print(f"{Numerator}/{Denominator} is an improper fraction.")
        if gcd == 1 and Denominator > 1:
            print(f"The improper fraction cannot be reduced any further.\nThe mixed number is {whole} and {gcdn-(whole*gcdd)}/{gcdd}")
        elif gcd == 1:
            print(f"The improper fraction cannot be reduced any further.\nThe whole number is {whole}")
        elif gcc ==1 and gcdd > 1:
            print(f"The improper fraction can be reduced further to become: {gcdn}/{gcdd}\nThe mixed number is {whole} and {gcdn - (whole * gcdd)}/{gcdd}")
        else:
            print(f"The improper fraction can be reduced further to become: {gcdn}/{gcdd}\nThe whole number is {whole}")
    end = (input("Do you want to do another fraction (y/n): "))
    if end == "y":
        continue
    elif end == "n":
        break
    else:
        print("Ill take that as a no\nEnding program...")
        break

