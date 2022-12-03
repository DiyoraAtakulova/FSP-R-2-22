# csv для удобной записи базы данных, хранит данные в виде таблицы
# можно разделить с помощью делителя (,)


import csv

with open('people.csv', 'r') as file:
    # reader = csv.reader(file)
    for row in csv.reader(file):
        # print(row)
        pass


# with open('employee_birthday.txt') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',') # delimiter работает с символами
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t {row[0]} works in the {row[1]} department, and was born in {row[2]}')
#             line_count += 1
#     print(f'Processed {line_count} lines')


# with open('employee_file.csv', mode='w', newline='', encoding='utf-8') as emp_file:
#     emp_writer = csv.writer(emp_file, delimiter=',')
#     emp_writer.writerow(['john smith', 'accounting', 'november'])
#     emp_writer.writerow(['erica', 'it', 'march'])

# with open('protogonist.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file, delimiter='\t')
#     writer.writerow(['SN', 'Movie', 'Protogonist']) # header-ы
#     writer.writerow([1, 'Lord of the rings', 'Frodo Baggins'])
#     writer.writerow([2, 'Harry Potter', 'Harry Potter'])


# with open('employee_birthday.txt') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         # print(row)
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}')
#             line_count += 1
#     print(f'Processed {line_count} lines')


with open('players.csv', 'w', newline='') as file:
    fieldnames = ['player_name', 'fide_rating']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader() # записывает первую строчку - header
    writer.writerow({'player_name': 'Magnus Carlsen', 'fide_rating': 2870})
    writer.writerow({'player_name': 'Fabiano Caruano', 'fide_rating': 2822})
    writer.writerow({'player_name': 'Ding Liren', 'fide_rating': 2801})
    # writer.writerow({fieldnames[0]: 'Mag CC', fieldnames[1]: 2811})

# csv.DictWriter(f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)