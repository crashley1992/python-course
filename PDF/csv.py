import csv 

# open file
data = open('example.csv', encoding='utf-8')
# csv reader
csv_data = csv.reader(data)

# reformat it into a python object list of lists
data_lines = list(csv_data)

# csv the very first row [0] is usually column names
for line in data_lines[:5]:
    print(line)

# will grab from the 10th row and the 3rd column name, so in this case email
data_lines[10][3]

all_emails = []
for line in data_lines[1:15]:
    all_emails.append(line[3])

full_names = []
for line in data_lines[1:]:
    full_names.append(line[1]+ ' ' + line[2])

file_to_output = open('to_save_file.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output,delimiter=',')
csv_writer.writerow(['a','b','c'])
csv_writer.writerow([['1','2', '3'], ['4','5','6']])
file_to_output.close()

f = open('to_save_file.csv', mode='a', newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['1','2','3'])
f.close()