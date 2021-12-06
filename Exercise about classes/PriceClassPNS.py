import ModulePNS

def createlistPNS():
    objects = list()
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
        instance = Module.PricesPNS(itemname, pounds)
        objects.append(instance)
    return objects

def showlistPNS(list):
    totalprice = 0
    print('Here\'s a summary of the items purchased:\n----------------------------\n')
    for i in list:
        i.checkitemPNS()
        print('\nitem:', getattr(i, 'dish'))
        print('Amount ordered: ', getattr(i, 'weight'), 'Pounds')
        print('Price per pound: ', '$'+str(getattr(i, 'price')))
        print('Price of order: ', '$'+str(i.totalcostPNS()))
        totalprice += i.totalcostPNS()
    print('\nTotal Cost: $'+str(totalprice))

brother = createlistPNS()
showlistPNS(brother)
