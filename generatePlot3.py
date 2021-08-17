import csv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def readCsv():
    value_dict = {}
    minval = -1
    maxChunk = 0
    chunkDifference = -1

    with open('C:\\Users\\targe\\Documents\\hpx\\build\\examples\\quickstart\\exclusiveOutputAlterAvg.csv') as csvfile:
        valueReader = csv.reader(csvfile)
        for row in valueReader:
            if minval == -1:
                minval = int(float(row[3]))
            else:
                minval = min(minval, int(float(row[3])))

            if chunkDifference == -1:
                chunkDifference = int(row[2])-int(row[1])
            maxChunk = max(maxChunk, int(row[2]))
            chunk_key = (int(row[1]), int(row[2]))
            
            if chunk_key not in value_dict:
                value_dict[chunk_key] = []

            value_dict[chunk_key].append([int(row[0]), int(float(row[3])), int(float(row[4]))])

    fig, ax = plt.subplots()
    ax.set_yticks(range(0, maxChunk+1, chunkDifference))
    ax.set_ylabel("Chunk extent")
    ax.set_xlabel("Time")

    functocolor = {
        1 : 'red',
        2 : 'blue',
        3 : 'orange'
    }
    handles = [mpatches.Patch(color='red', label='Stage 1'),
        mpatches.Patch(color='blue', label='Stage 2'),
        mpatches.Patch(color='orange', label='Stage 3')]
    plt.legend(loc="upper right", handles=handles)

    for key in value_dict:
        for val in value_dict[key]:
            if val[1] == 0 or val[2] == 0:
                continue

            start = val[1] - minval
            width = val[2]
            ax.broken_barh([(start, width)], (key[0], key[1]-key[0]), facecolor=functocolor[val[0]], edgecolor='black')

    plt.gca().invert_yaxis()
    plt.show()

if __name__ == "__main__":
    readCsv()