import csv
import time


actions = []
dataset1 = "./csv_f/dataset2_Python+P7.csv"

#extact dataset from csv file
with open (dataset1) as csv_file:
    csv_list = list(csv.reader(csv_file))
    for action in csv_list[1:]:
        #dont take actions <= 0
        if float(action[1]) <= 0 or float(action[2]) <= 0:
            pass
        else:
            action_productivity = round(float(action[1]) * float(action[2])) / 100
            actions.append([action[0], round(float(action[1])), action_productivity ])

def optimized_algorithm(wallet_cost, actions):
    number_of_actions = len(actions)
    #create en empty matrix
    matrix = [[0 for x in range(wallet_cost + 1)] for x in range(len(actions) +1)]
    #look over the actions 
    for i in range(1, len(actions) + 1):
        #for each action cost look over the wallet cost
        for w in range(1, wallet_cost + 1):
            #if the action cost in treatment is under the capacity of wallet
            if actions[i-1][1] <= w:
                #Put in the matrix the max between the action cost of the previous line and the current action cost + 
                # the optimized solution minus the cost of the action situated on the previous line
                matrix[i][w] = max(actions[i-1][2] + matrix[i-1][w-actions[i-1][1]], matrix[i-1][w])
                #if the cost of the last action is too hight and cant be stock in the wallet take the last optimized solution
            else:
                matrix[i][w] = matrix[i-1][w]
    
    w = wallet_cost
    n = number_of_actions
    final_combination = []

    while w >= 0 and n >= 0:
        #if the last solution is not the optimized solution continue to add the action of the previous line in the final combination
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