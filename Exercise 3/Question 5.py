# Question 5
def convert_temp():
    fahrenheit = eval(input("Enter a temperature in fahrenheit: "))
    celsius = convert_to_celsius(fahrenheit)
    kelvin =  convert_to_kelvin(celsius)
    print("The temperature in Fahrenheit is: ", fahrenheit)
    print("The temperature in Celsius is: ", celsius)
    print("The temperature in Kelvin is: ", kelvin)

def convert_to_celsius(fahrenheit):
    celsius = 5/9 * (fahrenheit-32)
    return celsius

def convert_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

convert_temp()
