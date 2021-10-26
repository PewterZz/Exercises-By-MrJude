import math

def Frange(Start, Stop = None, Inc = None):
    if Stop == None:
        start = str(Start)
        length = len(start)
        floats = length - len(str(math.floor(Start))) - 1
        ranger = (Start - math.floor(Start)) * (10 ** floats)
        count = 0
        rangers = float(str(math.floor(Start)) + str(ranger))
        while count < rangers:
            print((count) / (10 ** floats), end=", ")
            count += 1
    elif Stop != None and Inc != None:
        start = str(Start)
        length = len(start)
        floats = length - len(str(math.floor(Start))) - 1
        ranger = (Start - math.floor(Start)) * (10 ** floats)
        rangers = float(str(math.floor(Start)) + str(ranger))
        stop = str(Stop)
        length2 = len(stop)
        floats2 = length2 - len(str(math.floor(Stop))) - 1
        ranger2 = (Stop - math.floor(Stop)) * (10 ** floats2)
        rangers2 = float(str(math.floor(Stop)) + str(ranger2))
        inc = str(Inc)
        length3 = len(inc)
        floats3 = length3 - len(str(math.floor(Inc))) - 1
        ranger3 = (Inc - math.floor(Inc)) * (10 ** floats3)
        rangers3 = float(str(math.floor(Inc)) + str(ranger3))

        while rangers < rangers2:
            print((rangers) / (10 ** floats2), end=", ")
            rangers += rangers3

    else:
        stop = str(Stop)
        length2 = len(stop)
        floats2 = length2 - len(str(math.floor(Stop))) - 1
        ranger2 = (Stop - math.floor(Stop)) * (10 ** floats2)
        rangers2 = float(str(math.floor(Stop)) + str(ranger2))
        start = str(Start)
        length = len(start)
        floats = length - len(str(math.floor(Start))) - 1
        ranger = (Start - math.floor(Start)) * (10 ** floats2)
        rangers = float(str(math.floor(Start)) + str(ranger))


        while rangers < rangers2:
            print((rangers) / (10 ** floats2), end=", ")
            rangers += 1

Frange(1.0,5.0,0.1)
