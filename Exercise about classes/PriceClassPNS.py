import ModulePNS
#imported class from ModulePNS.py 
#driver code
def createlistPNS():
    objects = list()
    #var used as a counting method for items
    var = 1
    items = eval(input('How many items would you like ?, Must be at least 1: '))
    while items < 1:
        items = eval(input('How many items would you like ?, MUST BE AT LEAST 1: '))
    while items != 0:
        itemname = "blank"
        pounds = 0
        while itemname == "blank":
            print('item','#' + str(var))
            itemname = input('Name of the item: ')
            var += 1
        while pounds <= 0:
            pounds = eval(input('Amount of item in pounds: '))
        items -= 1
        #Creating the object and appending it onto a list
        instance = Module.PricesPNS(itemname, pounds)
        objects.append(instance)
    return objects
#Function to show the list in an ordered manner, for getting attributes i used getattr() and referenced the variables in the class, inside the list are the objects made from before.
def showlistPNS(list):
    totalprice = 0
    print('Here\'s a summary of the items purchased:\n----------------------------\n')
    #Looping through all objects appended into the list from before
    for i in list:
        i.checkitemPNS()
        print('\nitem:', getattr(i, 'dish'))
        print('Amount ordered: ', getattr(i, 'weight'), 'Pounds')
        print('Price per pound: ', '$'+str(getattr(i, 'price')))
        print('Price of order: ', '$'+str(i.totalcostPNS()))
        #total price of all items added together for each object
        totalprice += i.totalcostPNS()
    print('\nTotal Cost: $'+str(totalprice))

    
brother = createlistPNS()
showlistPNS(brother)
