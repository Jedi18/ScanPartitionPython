import csv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def readCsv():
    arr = []
    with open('C:\\Users\\targe\\Documents\\hpx\\build\\examples\\quickstart\\exclusiveOutput.csv') as csvfile:
    #with open('exclusiveOutput.csv') as csvfile:
        valueReader = csv.reader(csvfile)
        minval = -1
        for row in valueReader:
            if row[2] == '0' or row[3] == '0':
                continue

            if minval == -1:
                minval = int(row[2])
            else:
                minval = min(minval, int(row[2]))

            arr.append(row)

    fig, ax = plt.subplots()

    ax.set_yticks(np.arange(33))

    functocolor = {
        1 : 'green',
        2 : 'blue',
        3 : 'red'
    }
    handles = [mpatches.Patch(color='green', label='Stage 1'),
        mpatches.Patch(color='blue', label='Stage 2'),
        mpatches.Patch(color='red', label='Stage 3')]
    plt.legend(loc="lower right", handles=handles)

    for row in arr:
        func = int(row[0])
        id = int(row[1])
        start = int(row[2]) - minval
        width = int(row[3]) - int(row[2])
        ax.broken_barh([(start, width)],(id, 1), facecolor=functocolor[func])

    plt.show()

if __name__ == "__main__":
    readCsv()