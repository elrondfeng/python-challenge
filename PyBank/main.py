import os
import csv
from datetime import datetime
from dateutil import relativedelta

input_file_path = os.path.join('raw_data', 'budget_data_2.csv')

total_month = 0
total_revenue = 0
total_change = 0
max_increase = 0
max_decrease = 0
max_increase_date = None
max_decrease_date = None

current_date = None
current_revenue = None

def get_date(input):
    if(len(input)==6):
        return datetime.strptime(input, '%b-%y')
    elif(len(input)==8):
        return datetime.strptime(input,'%b-%Y')
    else:
        return NotImplemented

with open(input_file_path, 'r', newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader,None)

    first_record = next(csvreader,None)

    if (first_record == None):
        print("no record found in the file")
        quit(1)

    current_date = get_date(first_record[0])
    current_revenue = int(first_record[1])
    total_revenue = current_revenue

    for row in csvreader:

        pre_date = current_date
        pre_revenue = int(current_revenue)

        current_date = get_date(row[0])
        current_revenue = int(row[1])

        month_distance = relativedelta.relativedelta(current_date,pre_date)

        total_month = total_month + month_distance.months
        total_revenue = total_revenue + current_revenue
        total_change = total_change + (current_revenue - pre_revenue)
        if( max_increase < (current_revenue - pre_revenue)):
            max_increase = (current_revenue - pre_revenue)
            max_increase_date = current_date
        if( max_decrease < (pre_revenue - current_revenue)):
            max_decrease = (pre_revenue - current_revenue)
            max_decrease_date = current_date

# print out the result

print('\nFinancial Analysis\n----------------------------')
print('Total Months : ' + str(total_month))
print('Total Revenue : $' + str(total_revenue))
print('Average Revenue Change: $' + str(total_change/total_month))
print('Greatest Increase in Revenue: ' + str(max_increase_date) + '  ' + str(max_increase))
print('Greatest Decrease in Revenue: ' + str(max_decrease_date) + '  ' + str(max_decrease))

output_file_path = os.path.join('raw_data','result.txt')

with open(output_file_path,'w') as text_file:
    text_file.write('\nFinancial Analysis\n----------------------------')
    text_file.write('\nTotal Months : ' + str(total_month))
    text_file.write('\nTotal Revenue : $' + str(total_revenue))
    text_file.write('\nAverage Revenue Change: $' + str(total_change/total_month))
    text_file.write('Greatest Increase in Revenue: ' + str(max_increase_date) + '  ' + str(max_increase))
    text_file.write('Greatest Decrease in Revenue: ' + str(max_decrease_date) + '  ' + str(max_decrease))
