# Question3
temp = eval(input("Enter the temperature in fahrenheit: "))
while not -58 <= temp <= 41:
    print("Temperature must be between -58F and 41F")
    temp = eval(input("Please re-enter the temperature in fahrenheit: "))
wind = eval(input("Enter the wind speed miles per hour: "))
while not wind >= 2:
    print("Speed must be greater than or equal to 2")
    wind = eval(input("Please re-enter the wind speed miles per hour: "))
wind_chill = print(f"The wind chil index is {round((35.74+(0.6215*temp))-(35.75*pow(wind,0.16))+(0.4275*temp*pow(wind,0.16)),3)}")
