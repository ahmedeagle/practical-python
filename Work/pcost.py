import csv

# Open the CSV file and use DictReader
with open('Work/Data/portfolio.csv', 'rt') as f:
    reader = csv.DictReader(f)  # This will handle the header automatically
    cost = 0

    # Loop through each row as a dictionary
    for row in reader:
        shares = int(row['shares'])  # Access 'shares' column and convert to integer
        price = float(row['price'])  # Access 'price' column and convert to float
        cost += shares * price  # Add the cost for this row

    # Print the final total cost
    print(f'Cost: ${cost:0.2f}')
