
#Mod 3 Challenge PyBank
# going through to find:
# total number of months in the dataset
# the total amount of profit and loss
# the changes in profit and loss over 
# the greatest increase of proft
# the greatest decrease 

import csv
import os


 #set file
file_path = os.path.join("Resources", "budget_data.csv")

with open(file_path) as file:
    reader = csv.reader(file) 
    next(reader)#skipping header row


    #variables
    counter = 0 #months
    totalrev = 0
    revchange = []
    gincrease = ['',0]
    gdecrease = ['',0]
    previousrev = 0
    

    #finding the total number of months (counter)
    #finding the total revenue

    for row in reader: #reading each row
        counter = counter + 1
        date = row[0] # dates
        rev = int(row[1]) #revenue of one row
        totalrev = totalrev + rev #towal revenue

        #changes of rev
        currentchange = rev - previousrev #this months proft from last month
        if counter > 1: #saving all change EXCEPT for the very first month
            revchange.append(currentchange)
        if currentchange > gincrease[1]:
            gincrease = [date, currentchange]
        elif currentchange <gdecrease[1]:
            gdecrease = [date, currentchange]
        previousrev = rev #new profit 
    
    avgchange = sum(revchange)/len(revchange)


    #printing Fiancial Analysis statement 
    printstatement = f'''
    
    Financial Analysis
    
    ------------------

    Total Months:{counter}
    Total:{totalrev}
    Average Cahnge: ${avgchange:.2f}
    Greatest Increase in Profits: {gincrease[0]} (${gincrease[1]})
    Greatesr Decrease in Profits: {gdecrease[0]} (${gdecrease[1]})
    '''
    print(printstatement)    

#creating an output file
output_path = os.path.join("analysis","Financial_Analysis.txt")
with open(output_path, "w") as outfile:
    outfile.write(printstatement)