import csv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def readCsv():
    executionColors = {
        "seq": "green",
        "par": "red",
        "stl": "blue",
        "spa": "orange"
    }

    inputSize = []
    executionTimes = {}
    executionTimes["seq"] = []
    executionTimes["par"] = []
    executionTimes["stl"] = []
    executionTimes["spa"] = []

    with open('C:\\Users\\targe\\Documents\\hpx\\build\\examples\\quickstart\\exclusiveComparision.csv') as csvfile:
        valueReader = csv.reader(csvfile)
        for row in valueReader:
            inputSize.append(int(row[0]))

            executionTimes["seq"].append(float(row[1]))
            executionTimes["par"].append(float(row[2]))
            executionTimes["stl"].append(float(row[3]))
            executionTimes["spa"].append(float(row[4]))

    fig, ax = plt.subplots()

    handles = []
    for exec in executionTimes:
        ax.plot(inputSize, executionTimes[exec], color=executionColors[exec])
        handles.append(mpatches.Patch(color=executionColors[exec], label=exec))

    plt.legend(loc="upper right", handles=handles)

    plt.show()

if __name__ == "__main__":
    readCsv()