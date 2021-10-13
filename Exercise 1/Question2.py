# Question2
speed = eval(input("Enter the plane's Speed in m/s: "))
accel = eval(input("Enter the plane's acceleration in m/s**2: "))
formula = pow(speed,2)/(accel*2)
print(f"The minimum runway length needed for this airplane is {round(formula,4)} meters")
