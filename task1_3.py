'''Module csv providing a function reading csv file
   Module random providing a function returning a random integer in the specified range
'''

from csv import reader
from random import randint

# Генератор библиографических ссылок 

# Open the output file
with open('Book_result.txt', 'w', encoding='windows-1251') as output:
    # Open and read the CSV file
    with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
        file = reader(csvfile, delimiter=";")
        books_data = [row for row in file]
        books_data.pop(0)  # Remove the header row

        # Generate 20 random bibliographic references
        for row_num in range(1, 21):
            random_book = books_data[randint(1, len(books_data) - 1)]
            # Format: <Author>. <Title> - <Year>
            reference = f"{row_num}. {random_book[2]}. {random_book[1]} - {random_book[3]}"
            print(reference)
            output.write(reference + "\n")
