import csv
with open('source.txt') as s:
    source = s.read()
    source = source.split('\n')
    print(type(source),source)

source_table = [['producer','model','fuel','price'],[source[0],source[1],source[2],source[3]]]
print(source_table)

with open('source_to_csv.csv', 'w') as f:
    writer = csv.writer(f,delimiter = ';')
    writer.writerows(source_table)
