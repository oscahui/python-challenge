import os
import csv
data = []
count = 0
count_khan = 0
count_correy = 0
count_li = 0
count_tooley = 0

pypoll_csv = os.path.join('..','Resources','election_data.csv')
with open(pypoll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for data in csvreader:
        count = count +1
        if (data[2]) == "Khan":
            count_khan = count_khan +1
        if (data[2]) == "Correy":
            count_correy = count_correy +1
        if (data[2]) == "Li":
            count_li = count_li +1
        if (data[2]) == "O'Tooley":
            count_tooley = count_tooley +1
    per_khan = count_khan/count*100
    per_correy = count_correy/count*100
    per_li = count_li/count*100
    per_tooley = count_tooley/count*100
    list1 = (count_khan, count_correy, count_li,count_tooley)
    winner = max(list1)
    if winner == count_khan:
        winner_name = "Khan"
    elif winner == count_correy:
        winner_name = "Correy"
    elif winner ==count_li:
        inner_name = "Li"
    else:
        winner_name = "O'Tooley"
            
    print("Election Results")
    print("-----------------")
    print(f"Total Votes: {count}")
    print("-----------------")    
    print(f"Khan: {round(per_khan,2)}% ({count_khan})")
    print(f"Correy: {round(per_correy,2)}% ({count_correy})")
    print(f"Li: {round(per_li,2)}% ({count_li})")
    print(f"O'Tooley: {round(per_tooley,2)}% ({count_tooley})")
    print("-----------------")
    print("Winner: "+winner_name)
    output = os.path.join("..","Output","analysis.csv")
    with open(output, 'w') as csvfile:
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(["Election Results"])
        csvwriter.writerow(["-----------------"])
        csvwriter.writerow(["Total Votes: {count}"])
        csvwriter.writerow(["-----------------"])    
        csvwriter.writerow(["Khan:", round(per_khan,2),(count_khan)])
        csvwriter.writerow(["Correy:", round(per_correy,2),(count_correy)])
        csvwriter.writerow(["Li:", round(per_li,2), (count_li)])
        csvwriter.writerow(["O'Tooley:", round(per_tooley,2), (count_tooley)])
        csvwriter.writerow(["-----------------"])
        csvwriter.writerow(["Winner: ", winner_name])
    

