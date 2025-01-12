# report.py
#
# Exercise 2.4

import csv

def read_portfolio(fileName):
    total_cost = 0
    profiles = []
    with open(fileName, 'rt') as f:
        reader = csv.DictReader(f)
        for row in reader:
            profiles.append((row['name'], row['shares'], row['price']))
            total_cost += int(row['shares']) * float(row['price'])
            #profiles.append(row)
            #shares = int(row['shares'])
            #price = float(row['price'])
            #total_cost += shares * price

    return profiles , total_cost

#_, total_cost = read_portfolio("Work/Data/portfolio.csv")
#print(total_cost)


def check(x):
    x.append(10)
    print(x)

x=[1,2,3]
check(x)
print(x)


def read_prices(filename):
    '''
    Read prices from a CSV file of name,price data
    '''
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices

