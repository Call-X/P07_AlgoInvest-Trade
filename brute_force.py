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


def brute_force_algorithme(money_wallet):
    
    data_set = []
    combinations = []

    primary_csv_file = './csv_f/Bruteforce.csv'

    with open(primary_csv_file, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for element in reader:
            """ print(','.join(element)) """
            action_productivity = float(element["cost"]) * float(element["benefit"]) / 100 
            """ print(percentage_per_action) """
            data_set.append(Dataset(element["name"], (element["cost"]), action_productivity).serialized_dataset())
            """ print(data_set) """

    for i in range(1, len(data_set) + 1):
        for combination in cbts(data_set, i):
            for element in combination:
                if element[1] <= 0:
                    pass
                
                elif sum(element[1] for element in combination) <= money_wallet:
                    combinations.append(combination)
                    """ print(combinations) """
                

    sorted_combinations = sorted(combinations, key=lambda element: element[3])
    print(sorted_combinations)
            
brute_force_algorithme(500)