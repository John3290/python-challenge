#!/usr/bin/env python
# coding: utf-8

# In[1]:


#total votes
#percentage of votes each person won (total number of votes they got)
#Winner based on popular vote


import os 
import csv


# In[2]:


#set everything to 0
Candidates = [] 
unicandidate = []
khan = []
correy = []
Li = []
Otooley = []
count = 0


# In[3]:


#Create path
csvpath = os.path.join("Resources", "week_03 Python_homework_PyPoll_Resources_election_data.csv")


# In[4]:


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    
    for row in csvreader:
        #counts the rows in the csv file that will help up understand all of the possible candidates listed across the worksheet
        count += 1
        #this asdd in all of the candidate variables from row 2 of the csv to the Candidates list
        Candidates.append(row[2])
    #for every entry in the candidate list
    for p in Candidates:
        #if the entry (p) is unique, therefor, not in the unicandidate list, add it in
        if p not in unicandidate:
            unicandidate.append(p)
    


# In[5]:


#this will add the number of votes for each name of a candidate for a list assigned just for that candidates votes     
for votes in Candidates:
   if votes == "Khan":
       khan.append(votes)
   elif votes == "Correy":
       correy.append(votes)
   elif votes == "Li":
       Li.append(votes)
   elif votes == "O'Tooley":
       Otooley.append(votes)


# In[6]:


#Percentages for candidates
#takes the length of the Khan list, which includes every vote for Khan, and divides it by the total votes, for example. Round was used to only include a few decimal places
khanpercent = round((len(khan))/count*100, 3)
correypercent = round((len(correy))/count*100, 3)
lipercent = round((len(Li))/count*100, 3)
otoolpercent = round((len(Otooley))/count*100, 3)


# In[7]:


# winner calculations
#This compares the percentages of each candidate, calculated above. If Khan's % was higher than all others, for example, then winner would be equal to candidate 0 in the unicandidate list, which is Khan.
if int(khanpercent) > int(correypercent) & int(khanpercent) > int(lipercent) & int(khanpercent) > int(otoolpercent):
    winner = unicandidate[0]
        
elif int(correypercent) > int(khanpercent) & int(correypercent) > int(lipercentlipercent) & int(correypercent) > int(otoolpercent):
    winner = unicandidate[1]
        
elif int(lipercent) > int(khanpercent) & int(lipercent) > int(correypercent) & int(lipercent) > int(otoolpercent):
    winner = unicandidate[2]
        
elif int(otoolpercent) > int(khanpercent) & int(otoolpercent) > int(correypercent) & int(otoolpercent) > int(lipercent):
    winner = unicandidate[3]


# In[8]:


#How to check the index number for the candidate for the above calculations
#for (num, item) in enumerate(unicandidate):
    #print(num,item)


# In[9]:


# Print
print("Election Results")
print("--------------------")
print("Total Votes: " + str(count))
print("--------------------")
print("Khan: " + str(khanpercent) + "% " +  "(" + str(len(khan)) + ")")
print("Correy: " + str(correypercent) + "% " + "(" + str(len(correy)) + ")")
print("Li: " + str(lipercent) + "% " + "(" + str(len(Li)) + ")")
print("O'Tooley: " + str(otoolpercent) + "% " + "(" + str(len(Otooley)) + ")") 
print("------------------")
print("Winner: " + winner)
print("---------------------")


# In[10]:


#exporting to .txt
output = os.path.join("Analysis", "PollResults.txt")
with open(output, 'w') as file:
    text = csv.writer(file)
    text.writerow(["Election Results"])
    text.writerow(["-------------------"])
    text.writerow(["Total Votes: " + str(count)])
    text.writerow(["-------------------"])
    text.writerow(["Khan: " + str(khanpercent) + "% " +  "(" + str(len(khan)) + ")"])
    text.writerow(["Correy: " + str(correypercent) + "% " + "(" + str(len(correy)) + ")"])
    text.writerow(["Li: " + str(lipercent) + "% " + "(" + str(len(Li)) + ")"])
    text.writerow(["O'Tooley: " + str(otoolpercent) + "% " + "(" + str(len(Otooley)) + ")"])
    text.writerow(["-----------------"])
    text.writerow(["Winner: " + winner])
    text.writerow(["--------------------"])

