#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import modules needed
import os
import csv


# In[2]:


# In[2]:

#set everything to 0
total = 0
avchange = 0
increaseprofits = 0
decreaseprofits = 0
PastRevenue = 0
#store the change in revenue
avchangelist = []
#Store months list
Monthslist = []


# In[3]:


# In[3]:


#create the path. This will access the csv in the resources folder
csvpath = os.path.join("Resources", "week_03_Python_homework_PyBank_Resources_budget_data.csv")


# In[4]:


# In[4]:


with open(csvpath) as csvfile:
    #opening csv file and noting the the variables are separated by ,
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #cycles through the csv file, starting at position 0. Here, csv_header will report the titles of each column. 
    csv_header = next(csvreader)
    
    #This will report the first row of actual data for each column.
    firstrow= next(csvreader)
    
    #to conceptualize what csv_header and firstrow represent, you can run the following functions:
    #print(f"Header: {firstrow}")
    #print(f"Header: {csv_header}")
    
    #not sure if needed:
    #currentvalue = int(firstrow[1])
    
    total = int(firstrow[1])
    #now total contains the contents of the second column, first row of the worksheet with revenue data
    
    PastRevenue = int(firstrow[1])
    #Make PastRevenue start on row 2
    
#look through all the rows for info
    for row in csvreader:  
        Monthslist.append(row[0])
        totalmonths = len(Monthslist) + 1
        #adds 1 to the index value (aka the length) of column 0 which is the months column. This updates the monthslist list
    
    #total revenue. 
    #int pulls the actual values of row 1 and adds them. Here, I'm cycling through the values of the revenue column and adding them to get a new total number
        total += int(row[1])
    #  += adds another value with the variables value and assigns the new value to the variable. It's cycling through the revenue column (1)
    
    
    #Revenue change calculation
    
        #should int(row[1]) below be total instead?
        #RevenueChange= int(row[1]) - PastRevenue
        #RevenueChange = total - PastRevenue: this also didn't work!
        #values of column with revenue minus past revenue is the change in revenue
        
        #avchangelist.append(RevenueChange)
        #updating the avchangelist to reflect the new total for revenue change
        avchangelist.append(int(row[1])- PastRevenue)
        
        PastRevenue = int(row[1])
        #this doesn't make sense? 
        
    #average change
    sumprofitloss = sum(avchangelist)
    avchange = (sumprofitloss / len(avchangelist))
    
    #Greatest Increase in Profits Date and the $
    increaseprofits = max(avchangelist)
        #max value in list avchange
    indexincrease = avchangelist.index(increaseprofits)
        #the index of the max value
    dateincrease = Monthslist[indexincrease]
        #the value in the monthslist that shares the same index as the max value of avchangelist
    
    #Greatest Decrease in Profits Date and the $
    decreaseprofits = min(avchangelist)
        #minimum of the average change list
    indexdecrease =avchangelist.index(decreaseprofits)
        #index of the smallest value of average change list
    datedecrease = Monthslist[indexdecrease]
        #the month that corresponds with the index for the smallest average change list value


# In[6]:


# In[5]:

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(totalmonths))
print("Total Profits/ Losses: $" + str(total))
print("Average change in Profit/Losses: " + "$" + str(round(avchange,2)))
#avchange should be -2315.12
print("Greatest Increase in Profits: " + str(dateincrease) + " ($" + str(increaseprofits) + ")")
print("Greatest Increase in Profits: "+ str(datedecrease) + " ($" + str(decreaseprofits) + ")")


# In[7]:


In[6]:

#export text file with results
output = os.path.join("Analysis", "results.txt")
with open(output, 'w') as file:
    text = csv.writer(file)
    text.writerow(["Financial Analysis"])
    text.writerow(["----------------------------"])
    text.writerow(["Total Months: " + str(totalmonths)])
    text.writerow(["Total Profits/ Losses: $" + str(total)])
    text.writerow(["Average change in Profit/Losses: " + str(round(avchange,2))])
    text.writerow(["Greatest Increase in Profits: " + str(dateincrease) + " ($" + str(increaseprofits) + ")"])
    text.writerow(["Greatest Increase in Profits: "+ str(datedecrease) + " ($" + str(decreaseprofits) + ")"])

