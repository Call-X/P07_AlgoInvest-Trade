import csv
import time
from itertools import combinations as cbts


class Dataset:

    dataset_list = []

    def __init__(self, name, cost, benefit):
        self.name = name
        self.cost = cost
        self.benefit = benefit
        self.dataset_list.append(self)


    def serialized_dataset(self):
        dataset = self.name, int(float(self.cost)), float(self.benefit)
        return dataset
    
    
    def __repr__(self):
       return f"{self.name}{self.cost}{self.benefit}"


def brute_force_algorithme():

    data_set = []
    combinations = []

    primary_csv_file = './csv_f/Bruteforce.csv'

    with open(primary_csv_file, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for element in reader:
            """ print(','.join(element)) """
            percentage_per_action = float(element["cost"]) * float(element["benefit"]) / 100 
            """ print(percentage_per_action) """
            data_set.append(Dataset(element["name"], (element["cost"]), percentage_per_action).serialized_dataset())
            """ print(data_set) """
    j = 0         
    j = j + 1
    for i in range(0, len(data_set)-j):
        if data_set[i] > data_set[i+1]:
            data_set[i], data_set[i+1] = data_set[i+1], data_set[i]
            for element in combinations:
                if element[2] <= 1:
                    pass
                

    return data_set
print(brute_force_algorithme())
