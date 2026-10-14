# Read marks.csv and calculate average marks for each student.
import csv
with open('marks.csv', 'r', newline='') as file:
    for row in csv.DictReader(file):
        marks = [int(row['Mark1']), int(row['Mark2']), int(row['Mark3'])]
        print(row['Name'], 'Average:', round(sum(marks) / len(marks), 2))
