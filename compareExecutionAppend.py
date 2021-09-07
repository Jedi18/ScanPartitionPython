import csv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def readCsv():
    inputSize = []
    executionTimes = {}
    executionNames = []
    executionColors = {}
    colors = ["brown", "red", "green", "blue", "yellow", "orange"]

    with open('C:\\Users\\targe\\Documents\\hpx\\build\\examples\\quickstart\\exclusiveCompareAppend.csv') as csvfile:
        valueReader = csv.reader(csvfile)
        first = True
        for row in valueReader:
            n = len(row)

            if first:
                for i in range(1, n-1):
                    executionNames.append(row[i])
                    executionTimes[row[i]] = []
                    executionColors[row[i]] = colors[i]
                
                first = False
                continue

            inputSize.append(int(row[0]))

            for i in range(1, n-1):
                val  = float(row[i])
                executionTimes[executionNames[i-1]].append(val)

    fig, ax = plt.subplots()
    for exec_type in executionTimes:
        ax.plot(inputSize, executionTimes[exec_type], color=executionColors[exec_type])

    handles = []
    for exec in executionTimes:
        ax.plot(inputSize, executionTimes[exec], color=executionColors[exec])
        handles.append(mpatches.Patch(color=executionColors[exec], label=exec))

    plt.legend(loc="upper right", handles=handles)
    plt.show()

if __name__ == "__main__":
    readCsv()