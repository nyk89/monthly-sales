# import csv

# def to_usd(my_price):
#     """
#     Converts a numeric value to usd-formatted string, for printing and display purposes.
#     Param: my_price (int or float) like 4000.444444
#     Example: to_usd(4000.444444)
#     Returns: $4,000.44
#     """
#     return f"${my_price:,.2f}" #> $12,000.71

# csv_file_path = "/Users/kellylynch/Desktop/Monthly-Sales/data/sales-201710.csv" # a relative filepath

# with open(csv_file_path, "r") as csv_file: # "r" means "open the file for reading"
#     reader = csv.DictReader(csv_file) # assuming your CSV has headers
#     # reader = csv.reader(csv_file) # if your CSV doesn't have headers
#     for row in reader:
#         print(row["product"], row["unit price"])

import os
import csv

def to_usd(my_price):
  # return "${0:,.2f}".format(my_price)
  return f"${my_price:,.2f}"

#
# INFO INPUTS
#

CSV_FILENAME = "sales-201803.csv"

csv_filepath = os.path.join("data", CSV_FILENAME)

rows = []

with open(csv_filepath, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for od in reader:
        rows.append(dict(od)) # ideally we would transform all the prices from strings to floats here

# print(rows[0])
#> {'date': '2018-03-01', 'product': 'Button-Down Shirt', 'unit price': '65.05', 'units sold': '2', 'sales price': '130.10'}

# float(rows[0]["sales price"])
#> 130.10

sales_prices = [float(row["sales price"]) for row in rows] # list comprehension for mapping purposes!

total_sales = sum(sales_prices)

month = "MARCH" # TODO: get from file name or date values
year = 2018 # TODO: get from file name or date values

#
# INFO OUTPUTS
#

print("-------------------------")
print(f"SALES REPORT!")
print("-------------------------")
print(f"MONTH: {month} {year}")
print(f"TOTAL SALES: {to_usd(total_sales)}")