import csv
from itertools import combinations as cbts

class Dataset():

    dataset_list = []

    def __init__(self, name, cost, benefit):
        self.name = name
        self.cost = cost
        self.benefit = benefit
        self.dataset_list.append(self)


    def serialized_dataset(self):
        dataset = int(self.name, int(float(self.cost)), float(self.benefit))
        return dataset
    
    
    def __repr__(self) -> str:
       return f"{self.name}{self.cost}{self.benefit}"


def brute_force_algorithme():

    data_set = []

    primary_csv_file = './csv_f/Bruteforce.csv'

    with open(primary_csv_file, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for elmnt in reader:
            percentage_per_action = float(elmnt["cost"]) * float(elmnt["benefit "]) / 100
            data_set.append(Dataset(elmnt["name"], elmnt["cost"], percentage_per_action).serialized_dataset)
            

print (brute_force_algorithme())
""" if __name__== "__main__": 
    pass """
    
    
    

