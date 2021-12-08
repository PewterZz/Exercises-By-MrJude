class PricesPNS:
# Initialization of all the variables, private variables are set to none as to not disturb the normal parameter
    def __init__(self, dish, weight, price=None, total=None):
        self.dish = dish
        self.weight = weight
        self.price = price
        self.total = total


# I placed getter methods in the class instead of getattr() for better practice
    def getdishPNS(self):
        return self.dish

    def getweightPNS(self):
        return self.weight

    def getpricePNS(self):
        return self.price

    def gettotalPNS(self):
        return self.total

#function of if statements to check for the price of the item
    def __PriceListPNS(self):
        if self.dish == 'Dry Cured Iberian Ham':
            self.price = 177.80
        elif self.dish == 'Wagyu Steaks':
            self.price = 450.00
        elif self.dish == 'Matsutake Mushrooms':
            self.price = 272.00
        elif self.dish == 'Kopi Luwak Coffee':
            self.price = 306.50
        elif self.dish == 'Moose Cheese':
            self.price = 487.20
        elif self.dish == 'White Truffles':
            self.price = 3600.00
        elif self.dish == 'Blue Fin Tuna':
            self.price = 3603.00
        elif self.dish == 'Le Bonnotte Potatoes':
            self.price = 270.81
        else:
            self.price = 0.00
#extra function to call the private function inside the class and check the prices
    def checkitemPNS(self):
        self.__PriceListPNS()

#calculating function
    def totalcostPNS(self):
        self.__PriceListPNS()
        cost = self.weight * self.price
        return cost
