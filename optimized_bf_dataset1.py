import csv

import time

actions = []
dataset1 = "./csv_f/dataset1_Python+P7.csv"

with open (dataset1) as csv_file:
    csv_list = list(csv.reader(csv_file))
    for action in csv_list[1:]:
        #exclude negative or 0 value action
        if float(action[1]) <= 0 or float(action[2]) <= 0:
            pass
        else:
            action_productivity = round(float(action[1]) * float(action[2])) / 100
            actions.append([action[0], round(float(action[1])), action_productivity ])

def optimized_algorithm(wallet_cost, actions):
    number_of_actions = len(actions)
    matrix = [[0 for x in range(wallet_cost + 1)] for x in range(len(actions) +1)]

    for i in range(1, len(actions) + 1):
        for w in range(1, wallet_cost + 1):
            if actions[i-1][1] <= w:
                matrix[i][w] = max(actions[i-1][2] + matrix[i-1][w-actions[i-1][1]], 
                matrix[i-1][w])
            else:
                matrix[i][w] = matrix[i-1][w]
    
    w = wallet_cost
    n = number_of_actions
    final_combination = []
    
    while w >= 0 and n >= 0:
        if matrix[n][w] != matrix[n-1][w]:
            final_combination.append(actions[n-1])
            w -= actions[n-1][1]
        n -= 1
    

    actions_names = [x[0] for x in final_combination]
    total_investment = sum([(x[1]) for x in final_combination])
    total_profit = sum([(x[2]) for x in final_combination])

    print("\n For the better investment you need to buy this list of actions : \n")
    print("--------------------- \n")
    for actions_names in final_combination: 
        print(actions_names[0])
    print("\n --------------------- \n")
    print(f"")
    print(f"\n For a total investment of {total_investment}€")
    print(f"\n You will win : {round(total_profit, 2)}€")
    print(
    f"\n That means that your return on investment is :  {round(total_profit / total_investment * 100, 2)} % \n")

if __name__ == "__main__":
    start_time = time.time()
    optimized_algorithm(500, actions)
    print("\n Program executed in %s seconds \n" % (round(time.time() - start_time, 2)))