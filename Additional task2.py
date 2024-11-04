'''Module for processing books-en.csv and currency.xml based on Task 5 requirements'''

from csv import reader
import xml.etree.ElementTree as ET

# Part 1: Processing books-en.csv

# Open and read the CSV file with no limitations
with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    file = reader(csvfile, delimiter=';')
    books_data = [i for i in file]
    books_data.pop(0)  # Remove the header row

# Display the first few rows for verification (Optional)
print("Sample data from books-en.csv (no limitations):")
for i, row in enumerate(books_data[:5], 1):  # Displaying first 5 rows as an example
    print(f"{i}. {row}")

# Part 2: Processing currency.xml

# Initialize lists for CharCode and Value
char_codes = []
values = []

# Parse the XML file and populate the lists
tree = ET.parse('currency.xml')
root = tree.getroot()

for valute in root.findall('Valute'):
    # Extract CharCode and Value for each currency
    char_code = valute.find('CharCode').text
    value = valute.find('Value').text.replace(',', '.')  # Replace commas for float conversion
    
    char_codes.append(char_code)
    values.append(float(value))

# Display the lists
print("CharCodes:", char_codes)
print("Values:", values)
