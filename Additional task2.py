'''Module for processing books-en.csv and currency.xml based on Variant 5 requirements'''

from csv import reader
import xml.etree.ElementTree as ET

# Part 1: Processing books-en.csv

# Lists to store top 20 books by download count
top_books_downloads = [0] * 20
top_books_name = [""] * 20
top20_books = [""] * 20

# Open and read the CSV file
with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    file = reader(csvfile, delimiter=';')
    books_data = [row for row  in file]
    books_data.pop(0)  # Remove the header row

    # Find top 20 books based on download count
    for row in range(20):
        for book in books_data:
            # Check if the book's download count is higher and if it hasn't been added to top_books_name
            if int(book[5]) > top_books_downloads[row] and book[1] not in top_books_name:
                top_books_downloads[row] = int(book[5])
                top_books_name[row] = book[1]

        # Store the result in top20_books
        top20_books[row] = f"{top_books_name[row]} - {top_books_downloads[row]} downloads"

# Display the top 20 books
print("Top 20 Most Popular Books:")
for idx, book in enumerate(top20_books, 1):
    print(f"{idx}. {book}")


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
