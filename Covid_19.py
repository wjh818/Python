import csv
f = open('CONVENIENT_global_confirmed_cases.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
  print(line)
f.close()