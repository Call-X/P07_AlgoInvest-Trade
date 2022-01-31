import csv
from itertools import combinations as cbts
import time



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
            action_productivity = float(element["cost"]) * float(element["benefit"]) / 100 
            data_set.append(Dataset(element["name"], (element["cost"]), action_productivity).serialized_dataset())

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

    best_actions_combination = sorted_combinations["action_list"]
    total_investment = sorted_combinations["total_cost"]
    total_profit = sorted_combinations["total_benefit"]
        
    # Reports
    print ("\n The best combination you can get is : \n")
    print("_____________ \n")
    for element in best_actions_combination:
        print(element[0])
    print("_____________")
    print(f"\nFor a total investment of {total_investment}€ \n")
    print(f"You'll get a profit of {round(total_profit, 2)}€ after 2 years")  

if __name__ == "__main__":
    start_time = time.time()
    brute_force_algorithme(500)  # O(n)
    print("\nProgram executed in %s seconds" % (round(time.time() - start_time, 2 )) + "\n")






