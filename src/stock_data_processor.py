"""
The Stock Portfolio Data Processing Challenge involves
building a Python program that extracts and processes
stock-related data using sequence unpacking techniques.
The program must handle various data formats,
including simple and nested tuples, strings representing transaction logs,
and messy records with irrelevant fields.
Tasks include unpacking stock portfolio entries, parsing transaction strings,
extracting nested company and address details, cleaning inconsistent data,
and implementing error handling for unpacking mismatches.
The goal is to demonstrate proficiency in unpacking diverse
iterable structures, ensuring clean, structured, and meaningful
output from raw financial data inputs.
"""

# Basic unpacking
stock_record = [
    ("AAPL", 100, 150.25, (2023, 3, 15)),
    ("GOOGL", 50, 2800.50, (2023, 4, 20)),
]

record1, record2 = stock_record

print(record1)
print(record2)
print("-" * 40)


# Unpack a iterable of type string
transaction_log = "BSSBBS"

try:
    a, b, c, d, e, f = transaction_log
    print(a)
    print("-" * 40)
except ValueError as e:
    print("Number of variables should match the length of sequence: ", e)

# Handle nested company info
company_info = ("TECH", ("AAPL", "Apple Inc.", ("Cupertino", "CA", 95014)), 150.25)

try:
    sector, company_tuple, stock_price = company_info
    symbol, company_name, address = company_tuple
    print(f"Sector: {sector}")
    print(f"Symbol: {symbol}")
    print(f"Company Name: {company_name}")
    print(f"Address: {address}")
    print("-" * 40)
except ValueError as e:
    print(e)

# Extract relevant fields
messy_data = ("MSFT", "ignore_this", 75, "also_ignore", 300.15, (2023, 5, 10))

try:
    symbol, _, shares, _, price, date = messy_data
    print(f"Symbol: {symbol}")
    print(f"Shares: {shares}")
    print(f"Price: {price}")
    print(f"Date: {date}")
    print("-" * 40)
except ValueError as e:
    print(e)
