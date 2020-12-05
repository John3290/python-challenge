#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import modules needed
import os
import csv


# In[2]:


#set everything to 0
total = 0
avchange = 0
increaseprofits = 0
decreaseprofits = 0
PastRevenue = 0
RevenueChange = 0
#store the change in revenue
avchangelist = []
#Store months list
Monthslist = []


# In[3]:


#create the path
csvpath = os.path.join("Resources", "week_03_Python_homework_PyBank_Resources_budget_data.csv")


# In[4]:


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    firstrow=next(csvreader)
    currentvalue = int(firstrow[1])
    total = int(firstrow[1])
   
#look through all the rows for info

    for row in csvreader:  
        Monthslist.append(row[0])
        totalmonths = len(Monthslist) + 1
    
    #total revenue. int pulls the actual values of row 1 and adds them
        total += int(row[1])
    
    
    #Revenue change calculation
        
        RevenueChange= int(row[1]) - PastRevenue
        avchangelist.append(RevenueChange)
        PastRevenue= int(row[1])
        
    #average change
        sumprofitloss = sum(avchangelist)
        avchange = (sumprofitloss / (totalmonths-1))
    
    #Greatest Increase in Profits Date and the $
        increaseprofits = max(avchangelist)
        indexincrease = avchangelist.index(increaseprofits)
        dateincrease = Monthslist[indexincrease]
    
    #Greatest Decrease in Profits Date and the $
        decreaseprofits = min(avchangelist)
        #minimum of the average change list
        indexdecrease =avchangelist.index(decreaseprofits)
        #index of the smallest value of average change list
        datedecrease = Monthslist[indexdecrease]
        #the month that corresponds with the index for the smallest average change list value


# In[5]:


print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(totalmonths))
print("Total Profits/ Losses: $" + str(total))
print("Average change in Profit/Losses: " + str(round(avchange,2)))
print("Greatest Increase in Profits: " + str(dateincrease) + " ($" + str(increaseprofits) + ")")
print("Greatest Increase in Profits: "+ str(datedecrease) + " ($" + str(decreaseprofits) + ")")


# In[6]:


# export text file with results
output = os.path.join("Analysis", "results.txt")
with open(output, 'w') as file:
    text = csv.writer(file)
    text.writerow("Financial Analysis")
    text.writerow("----------------------------")
    text.writerow("Total Months: " + str(totalmonths))
    text.writerow("Total Profits/ Losses: $" + str(total))
    text.writerow("Average change in Profit/Losses: " + str(round(avchange,2)))
    text.writerow("Greatest Increase in Profits: " + str(dateincrease) + " ($" + str(increaseprofits) + ")")
    text.writerow("Greatest Increase in Profits: "+ str(datedecrease) + " ($" + str(decreaseprofits) + ")")


# In[ ]:




