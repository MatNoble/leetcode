import pandas as pd
import math

def mean(numberList):
    if len(numberList) == 0:
        return float('nan')
    floatNums = [float(x) for x in numberList]
    return sum(floatNums) / len(numberList)

def save_data(nx_list, error, filetitle):
    output_file = open(filetitle, "a")
    order = []
    output_file.write("---------------- \n")
    print("---------------- \n")
    for i in range(0, len(nx_list)):
        if i+1 < len(nx_list):
            order.append(math.log(error[i]/error[i+1])/math.log(2))
        if len(order) == (len(nx_list)-1):
            order.append(mean(order))
        print("M = %5d   %12.4e   %.2f \n"
              % (nx_list[i], error[i], round(order[i], 2)))
        output_file.write("M = %5d  %12.4e   %.2f \n"
                          % (nx_list[i], error[i], round(order[i], 2)))

def save_data_t(dt_list, error, filetitle):
    output_file = open(filetitle, "a")
    order = []
    output_file.write("---------------- \n")
    print("---------------- \n")
    for i in range(0, len(dt_list)):
        if i+1 < len(dt_list):
            order.append(math.log(error[i]/error[i+1])/math.log(2))
        if len(order) == (len(dt_list)-1):
            order.append(mean(order))
        print("dt = %.2f   %12.4e   %.2f \n"
              % (dt_list[i], error[i], round(order[i], 2)))
        output_file.write("dt = %.2f  %12.4e   %.2f \n"
                          % (dt_list[i], error[i], round(order[i], 2)))

def read_data():
    data_file = open("./data.txt", "r")
    data_list = data_file.readlines()
    data_file.close()
    d = pd.DataFrame(columns=["A", "B", "C"])
    for record in data_list:
        all_values = record.split(' ')
        dit = {"A": float(all_values[0]), "B": float(all_values[1]),
               "C": float(all_values[2])}
        d = d.append(dit, ignore_index=True)
    return d
