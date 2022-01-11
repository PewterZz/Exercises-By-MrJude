import csv
import statistics as st
import pygal
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'activity.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    
    print(headerRow)
    
    wr = open("newActivityKuDataSet.csv","w")
    wr.write(str(headerRow[0])+","+str(headerRow[1])+","+str(headerRow[2]))
    wr.write("\n")
    
    n=0
    for row in reader:
        if(row[0] == 'NA'):
            row[0] = 0
            n+=1
        wr.write(str(row[0])+","+str(row[1])+","+str(row[2]))
        wr.write("\n")
    
    wr.close()
    print("The total numbers of missing values in the dataset is: ",n)
    
newFile = 'newActivityKuDataSet.csv'
with open(newFile) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    
    dictDate = {}   #stores number of steps per day
    dictInterval = {} #stores number of steps per 5 min interval
    
    for row in reader:
        steps = row[0]
        date = row[1]
        interval = int(row[2])

        dictDate.setdefault(str(date), [])
        dictDate[str(date)].append(int(steps))
            
        dictInterval.setdefault(interval,[])
        dictInterval[interval].append(int(steps))



    listAvePerIntervalday = []
    listAvePerIntervalend = []
    listAvePerInterval = []
    listDaysofWeekend = []
    listDaysofWeekday = []


    for i in dictDate.keys():
        year = int(i[0:4])
        month = int(i[5:7])
        day = int(i[8:10])
        d = datetime(year, month, day)
        if d.weekday() > 4:
            Week = "WeekEnd"
            listDaysofWeekend.append(i)
            listAvePerIntervalend.append(st.mean(dictDate.get(i)))
        else:
            Week = "WeekDay"
            listDaysofWeekday.append(i)
            listAvePerIntervalday.append(st.mean(dictDate.get(i)))



    fig = plt.figure(dpi=80, figsize=(20, 6))
    plt.plot(listDaysofWeekend, listAvePerIntervalend, c='blue')
    plt.title("Average Daily Activity")
    plt.xlabel("Time Interval")
    plt.ylabel("Average number of steps taken in weekend")
    fig.autofmt_xdate()

    fig2 = plt.figure(dpi=80, figsize=(20, 6))
    plt.plot(listDaysofWeekday, listAvePerIntervalday, c='blue')
    plt.title("Average Daily Activity")
    plt.xlabel("Time Interval")
    plt.ylabel("Average number of steps taken in weekday")
    fig.autofmt_xdate()

    plt.show()
