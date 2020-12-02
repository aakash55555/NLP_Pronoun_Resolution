import csv
from collections import defaultdict
import json

def readCSV(filePath, delimiter=","):
    with open(filePath, 'r', newline='') as csvfile:
        csvData = csv.reader(csvfile, delimiter=delimiter)
        data = []
        for d in csvData:
            a = [float(i) for i in d]
            data.append(a)
    
    return data

def read_features_csv(file_path, delimiter=","):
    with open(file_path, 'r', newline='') as csvfile:
        csv_data = csv.reader(csvfile, delimiter=delimiter)
        data = []
        for d in csv_data:
            a = [i for i in d]
            data.append(a)
    
    return data

def writeCSV(data, fileName):
    with open(fileName + ".csv", 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        for t in data:
            spamwriter.writerow([x for x in t])

def write_csv_from_dict(data, file_name):
    with open(file_name, "a", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for key, value in data.items():
            csv_writer.writerow([key, value])

def write_json(json_data, file_name):
    with open(file_name, 'w') as json_file:
        json.dump(json_data, json_file)

def read_json(file_name):
    with open(file_name, 'r') as json_file:
        return json.load(json_file)