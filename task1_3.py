'''Module csv providing a function reading csv file
   Module random providing a function returning a random integer in the specified range
'''

from csv import reader
from random import randint

# Генератор библиографических ссылок

output = open('Book_result.txt', 'w', encoding='windows-1251')

with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    file = reader(csvfile, delimiter=";")
    books_data = [i for i in file]
    books_data.pop(0)  # Remove the header row

    for row in range(1, 21):  # Generate 20 bibliographic references
        random_book = books_data[randint(1, len(books_data) - 1)]
        # Format: <Author>. <Title> - <Year>
        print(f'{row}. {random_book[2]}. {random_book[1]} 
        - {random_book[3]}')
        output.write(f'{row}. {random_book[2]}. {random_book[1]} - {random_book[3]}\n')

output.close()
