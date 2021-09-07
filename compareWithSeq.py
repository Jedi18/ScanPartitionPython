import csv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def readCsv():
    labelToCol = {
        'seq' : 'red',
        'par' : 'blue',
        'old' : 'green'
    }

    fig, ax = plt.subplots()

    inputSizes = []
    seqTime = []
    parTime = []
    oldTime = []

    parRelative = []
    oldRelative = []

    with open('C:\\Users\\targe\\Documents\\scan_benchmarks\\exclusiveCompare.csv') as csvfile:
        valueReader = csv.reader(csvfile)
        first = True
        for row in valueReader:
            N = float(row[0])
            seq = float(row[1])
            par = float(row[2])
            old = float(row[3])

            inputSizes.append(N)
            seqTime.append(seq)
            parTime.append(par)
            oldTime.append(old)

            parRelative.append(seq/par)
            oldRelative.append(seq/old)
    
    ax.plot(inputSizes, parRelative, color=labelToCol['par'])
    ax.plot(inputSizes, oldRelative, color=labelToCol['old'])

    handles = []
    handles.append(mpatches.Patch(color=labelToCol['par'], label="Par relative to Seq"))
    handles.append(mpatches.Patch(color=labelToCol['old'], label="Old relative to Seq"))

    plt.legend(loc="upper right", handles=handles)
    plt.show()

if __name__ == "__main__":
    readCsv()