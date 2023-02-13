'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file

infile = open('employee_data.csv', 'r')

employee_file = csv.reader(infile, delimiter=',')
next(employee_file)
#create an empty dictionary

employee_dict = dict()

#use a loop to iterate through the csv file
for record in employee_file:
    #check if the employee fits the search criteria
    if record[4] == "CSR":
        if record[3] == "Marketing":
            tempKey = record[1] + " " + record[2]
            employee_dict[tempKey] = float(record[5])

for x in employee_dict:
    print("Manager Name: " + x + " Current Salary: $" + str(employee_dict[x]))

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout
for x in employee_dict:
    employee_dict[x] = employee_dict[x] * 1.1
    print("Manager Name: " + x + " New Salary: $" +
          str(round(employee_dict[x], 2)))
