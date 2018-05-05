import csv

files = "budget_data_1.csv" 

with open(files) as row:
    reader = csv.reader(row)

    next(reader) 
    total_revenue = []
    date = []
    change = []

    for row in reader:

        total_revenue.append(float(row[1]))
        date.append(row[0])

    print("Financial Analysis")
    print("--------------------")
    print("Total Months:", len(date))
    print("Total Revenue:", sum(total_revenue))

    for i in range(1,len(total_revenue)):
        change.append(total_revenue[i] - total_revenue[i-1])   
        avg_rev_change = sum(change)/len(change)

        max_change = max(change)

        min_change = min(change)

        max_change_date = str(date[change.index(max(change))])
        min_change_date = str(date[change.index(min(change))])
    print("Average Revenue Change:", round(avg_rev_change))
    print("Greatest Increase in Revenue:", max_change_date,"($", max_change,")")
    print("Greatest Decrease in Revenue:", min_change_date,"($", min_change,")")


