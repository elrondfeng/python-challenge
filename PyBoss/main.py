import os
import csv
from datetime import datetime

def convert_name(name=''):
    first_last = name.split(' ')
    return first_last


def convert_dob(dob):
    dob_in = dob
    return datetime.strptime(dob_in, '%Y-%m-%d').strftime('%m/%d/%Y')


def convert_ssn(ssn):
    if len(ssn) == 11:
        return 'xxx-xx-' + ssn[-4:]


us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


def convert_state(state):
    return us_state_abbrev[state]

def convert_all(row):
    first_last=convert_name(row[1])
    return row[0]+','+first_last[0] + ',' + first_last[1] + ',' + convert_dob(row[2])+','+convert_ssn(row[3])+ ',' + convert_state(row[4])


####### start process file

input_files = []
input_files.append(os.path.join('raw_data', 'employee_data1.csv'))
input_files.append(os.path.join('raw_data', 'employee_data2.csv'))

output_file = open(os.path.join('raw_data','output.txt'), 'w')
output_file.write('Emp ID,First Name,Last Name,DOB,SSN,State\n')

for i in range(2):
    input_file = input_files[i]
    with open(input_file,'r',newline='') as csvfile:

        csvreader = csv.reader(csvfile,delimiter=',')

        #skip header
        next(csvreader,None)

        for row in csvreader:
            output_file.write(convert_all(row)+'\n')

output_file.close()