import csv
import time
from xml.etree import ElementInclude 

actions = []
dataset1 = "./csv_f/dataset1_Python+P7.csv"

with open (dataset1) as csv_file:
    csv_list = list(csv.reader(csv_file))
    for action in csv_list[1:]:
        if float(action[1]) <= 0 or float(action[2]) <= 0:
            pass
        else:
            action_productivity = round(float(action[1]) * float(action[2])) / 100
            actions.append([action[0], round(float(action[1])), action_productivity ])

def optimized_algorithm(wallet_cost, elements):
    number_of_elements = len(elements)
    matrix = [[0 for x in range(wallet_cost + 1)] for x in range(len(elements) +1)]

    for i in range(1, len(elements) + 1):
        for w in range(1, wallet_cost + 1):
            if elements[i-1][1] <= w:
                matrix[i][w] = max(elements[i-1][2] + matrix[i-1][w-elements[i-1][1]], 
                matrix[i-1][w])
            else:
                matrix[i][w] = matrix[i-1][w]