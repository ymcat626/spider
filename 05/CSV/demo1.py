# coding: utf-8

import csv


with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['1001', 'Mike', 20])
    writer.writerow(['1002', 'Bob', 22])
    writer.writerow(['1003', 'Jordan', 22])
