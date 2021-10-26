# Question 2
def calc_weight_on_planet(Weight, Grav=23.1):
    Mass = Weight / 9.8
    Weight_on_grav = Mass * Grav
    print(Weight_on_grav)

calc_weight_on_planet(120)
