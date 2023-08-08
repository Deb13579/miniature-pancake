import csv

dataset_1 = []
dataset_2 = []

file_1 = "stars_2.csv"
with open(file_1, "r", encoding="utf8") as f:
    csvreader = csv.reader(f)
    for i in csvreader: 
        dataset_1.append(i)

with open("data.csv", "r") as f:
    csvreader = csv.reader(f)
    for i in csvreader: 
        dataset_2.append(i)

headers_1 = dataset_1[0]
planet_data_1 = dataset_1[1:]

headers_2 = dataset_2[0]
planet_data_2 = dataset_2[1:]

headers = headers_1 + headers_2
planet_data = []
for i in planet_data_1:
    planet_data.append(i)
for j in planet_data_2:
    planet_data.append(j)
    
with open("Final.csv", "w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)