import csv
fileload = "Pybank/Resources/budget_data.csv"
fileoutput = "Analysis/analysis.txt"

profit = []
monthlychange = []
date = []
count = 0
totalprofit = 0
totalchange = 0 
initial = 0
#better way to do it
with open(fileload, "r") as budget:
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
print("Greatest Increase in Profits: " +str(increasedate)+ " ($" + str(greatestincrease) + ")")
print("Great Decrease in Profits: " +str(decreasedate)+ " ($" + str(greatestdecrease) + ")")
                                                            
with open(fileoutput, 'w') as text:
    text.write("Financial Analysis\n")
    text.write("-----------------------\n")
    text.write("Total Months: " + str(count) + "\n")
    text.write("Total Profits: $"+ str(totalprofit) + "\n")
    text.write("Average Change: $"+ str(totalchange/count) + "\n")
    text.write("Greatest Increase in Profits: " +str(increasedate)+ " ($" + str(greatestincrease) + ")\n")
    text.write("Great Decrease in Profits: " +str(decreasedate)+ " ($" + str(greatestdecrease) + ")\n")
