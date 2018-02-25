import csv
import os
import sys

input_file = os.path.join('raw_data','election_data_2.csv')

class Logger(object):
    def __init__(self, filename = os.path.join('raw_data','output.txt')):
        self.terminal = sys.stdout
        self.log = open(filename, "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

logger = Logger()

with open(input_file,'r',newline='') as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')

    next(csvreader,None)

    ids = []
    counties = []
    candidates = []

    for row in csvreader:
        ids.append(row[0])
        counties.append(row[1])
        candidates.append(row[2])

logger.write('Election Results \n -------------------------\n')

total_votes = len(ids)

logger.write('Total Votes: ' + str(total_votes) + '\n----------------------\n')

for candidate in set(candidates):
    logger.write(candidate)
    count = candidates.count(candidate)
    logger.write(": " + str(count/total_votes))
    logger.write(' (' + str(count) + ')')
    logger.write('\n')



