import csv
filepath = "Pybank/Resources/budget_data.csv"

#we want to open the file, after having shown the path.
fileopen = open(filepath, "r")
#print(fileopen.read())
profit = []
monthlychange = []
date = []
count = 0
totalprofit = 0
totalchange = 0 
initial = 0
#better way to do it
with open(filepath, "r") as budget:
    reader = csv.reader(budget, delimiter=",")
    header = next(reader)
    for row in reader:
        count = count + 1
        profit.append(row[1])
        totalprofit = totalprofit + int(row[1])
        date.append(row[0])
        finalprofit = int(row[1])
        monthlychangeprofit = finalprofit - initial 
        monthlychange.append(monthlychangeprofit)
        totalchange = totalchange + monthlychangeprofit
        initial = finalprofit
        greatestincrease = max(monthlychange)
        greatestdecrease = min(monthlychange)
        increasedate = date[monthlychange.index(greatestincrease)]
        decreasedate = date[monthlychange.index(greatestdecrease)]
        
print("Financial Analysis")
print("-----------------------")
print("Total Months: " + str(count))
print("Total Profits: $"+ str(totalprofit))
print("Average Change: $"+ str(totalchange/count))
#Ask what is going on with a negative average for a positive total?
print("Greatest Increase in Profits: " +str(increasedate)+ " ($" + str(greatestincrease) + ")")
print("Great Decrease in Profits: " +str(decreasedate)+ " ($" + str(greatestdecrease) + ")")
                                                                
