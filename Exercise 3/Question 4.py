# Question 4
def calc_new_height():
    width = float(input("Enter your current width: "))
    height = float(input("Enter your current height: "))
    desire = float(input("Enter your desired width: "))
    curras = height/width
    needhei = curras * desire

    print("The corresponding height is: ", needhei)
    return needhei

calc_new_height()
