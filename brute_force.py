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
            final_combination = {
                "action_list": [], 
                "total_cost": 0,
                "total_benefit" : 0,   
            }
            for element in combination:
                    
                if  (final_combination["total_cost"] + element[1]) <= money_wallet:
                    final_combination["action_list"].append(element)
                    final_combination["total_cost"] += element[1]
                    final_combination["total_benefit"] += element[2]
                    combinations.append(final_combination)
                              
    sorted_combinations = max(combinations, key=lambda combination: combination["total_benefit"])
    print(sorted_combinations)
            
brute_force_algorithme(500)
