# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename,select=None) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)
        if select:
            headers = [headers[i] for i in select]
        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            record = dict(zip(headers, row))
            records.append(record)
    return records

portfolio = parse_csv('Work/Data/portfolio.csv')  
print(portfolio)  
