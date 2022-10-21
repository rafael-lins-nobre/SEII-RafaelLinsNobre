# Novamente nesse exercicio eu nao sei porque o python nao reconhece o names.csv como
# estando no mesmo diretorio, entao adiciono sempre o "/py15/" antes

import csv

# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
# 
#     with open('new_names.csv', 'w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='-')
# 
#         for line in csv_reader:
#             csv_writer.writerow(line)

with open('py15/names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        
        fieldnames = ['first_name', 'last_name']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)