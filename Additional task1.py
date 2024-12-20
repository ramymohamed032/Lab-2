'''Module providing a function reading csv file'''

from csv import reader

# (List of all unique publishers)

publishers = []
with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    file = reader(csvfile, delimiter=';')
    books_data = [i for i in file]
    books_data.pop(0)  # Remove the header row


    # Collect publishers from the specified column
    for row in books_data:
        publishers.append(row[4])  # Assuming publisher is in column index 4

# Display each unique publisher
print("Unique Publishers:")
for publisher in set(publishers):
    print(publisher)
