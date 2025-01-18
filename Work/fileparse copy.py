# fileparse.py

import csv


 #1- read as string 
#with open("Work/Data/portfolio.csv") as lines:
    #for line in lines:
        #print(line)  # Prints one row (as a string) at a time

#2- read as dictionary 
#rows = csv.DictReader(lines)
#Each row is converted into a dictionary, where:
#The keys are the column names from the CSV header.
#The values are the corresponding values in that row.

def parse_csv(lines, select=None, types=None):
    '''
    Parse a CSV file into a list of dictionaries, with optional column selection and type conversion.
    - lines: An iterable (e.g., file object or list of strings)
    - select: A list of column names to include (default: all columns)
    - types: A list of types to convert the columns (must match order of select, if used)
    '''
    rows = csv.DictReader(lines)

   # {'name':'ahmed','pricce':4004}
    # Filter columns if select is provided
    if select:
        select = set(select)  # Convert to a set for faster lookups
        rows = [{key: row[key] for key in select} for row in rows]
        ## alternative way to get the dictionalry of specific columns only
        # filtered_rows = []
        # for row in rows:
        #         keys=[]
        #         values=[]
        #         for key, value in row.items():
        #             if key in select:
        #                 keys.append(key)
        #                 values.append(value)
        #         filtered_rows.append(dict(zip(keys, values)))                                 
                        
    # Apply type conversion if types is provided
    if types:
        for row in rows:
            for key, func in zip(select, types):
                row[key] = func(row[key])

    return rows
