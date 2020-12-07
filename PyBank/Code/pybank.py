import os
import csv
data = []
total = 0
count = 0
max = 0
min = 0

pybank_csv = os.path.join('..','Resources','budget_data.csv')
with open(pybank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)    
    for data in csvreader:
        total = total+ int(data[1])
        if int(data[1]) > max:
            max = int(data[1])
            max_row = data[0]
        if int(data[1]) < min:
            min = int(data[1])
            min_row = data[0] 
        if count == 0:
            first = data[1] 
        last = data[1]
        count =count +1
avgchg = (float(first) - float(last))/ (count - 1) 
print("Financial Analysis")
print("--------------------------") 
print(f"Total Months: {count}")
print(f"Total: ${total}")
print(f"Average Change: ${round(avgchg,2)}")
print(f"Greatest Increase in Profits: {max_row} (${max})")
print(f"Greatest Decrease in Profits: {min_row} (${min})")
output = os.path.join("..","Output","analysis.csv")
with open(output, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)    
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["--------------------------"]) 
    csvwriter.writerow(["Total Months:", count])
    csvwriter.writerow(["Total: $",total])
    csvwriter.writerow(["Average Change: $",round(avgchg,2)])
    csvwriter.writerow(["Greatest Increase in Profits:",max_row,(max)])
    csvwriter.writerow(["Greatest Decrease in Profits:",min_row,(min)])