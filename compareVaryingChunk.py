import csv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from os import listdir
from os.path import isfile

def readCsv():
    labelToCol = {
        'seq' : 'red',
        'par' : 'green',
        'old' : 'blue'
    }

    fig, ax = plt.subplots()

    chunkFolders = ['int_default_chunk_size', 'int_chunk_size_by_24', 'int_chunk_size_by_48', 'int_chunk_size_by_96']
    chunkColorsPar = {
        'int_default_chunk_size' : "#FFB300",
        'int_chunk_size_by_24' : "#803E75",
        'int_chunk_size_by_48' : "#FF6800",
        'int_chunk_size_by_96' : "#A6BDD7"
    }
    chunkColorsOld = {
        'int_default_chunk_size' : "#CEA262",
        'int_chunk_size_by_24' : "#817066",
        'int_chunk_size_by_48' : "#007D34",
        'int_chunk_size_by_96' : "#F6768E"
    }

    for folder_name in chunkFolders:
        inputSizes = []
        seqTime = []
        parTime = []
        oldTime = []
        parRelative = []
        oldRelative = []

        with open('C:\\Users\\targe\\Pictures\\scan_benchmarks\\24cores\\' + folder_name + '\\csv_files\\inclusiveScanCompare.csv') as csvfile:
            valueReader = csv.reader(csvfile)
            first = True
            c = 5
            for row in valueReader:
                N = float(row[0])
                seq = float(row[1])
                par = float(row[2])
                old = float(row[3])

                inputSizes.append(c)
                c += 1
                seqTime.append(seq)
                parTime.append(par)
                oldTime.append(old)

                parRelative.append(seq/par)
                oldRelative.append(seq/old)
            
        ax.set_xticks(range(5, 32, 1))

        ax.plot(inputSizes, parRelative, color=chunkColorsPar[folder_name])
        ax.plot(inputSizes, oldRelative, color=chunkColorsOld[folder_name])

    ax.plot([5, 30], [1, 1], color=labelToCol['seq'])

    ax.set_xlabel('i where the input size is 2^i')
    ax.set_ylabel('Relative speedup to sequential')

    handles = []
    handles.append(mpatches.Patch(color=labelToCol['seq'], label="seq"))
    handles.append(mpatches.Patch(color=chunkColorsPar['int_default_chunk_size'], label="par - default"))
    handles.append(mpatches.Patch(color=chunkColorsPar['int_chunk_size_by_24'], label="par - chunk size by 24"))
    handles.append(mpatches.Patch(color=chunkColorsPar['int_chunk_size_by_48'], label="par - chunk size by 48"))
    handles.append(mpatches.Patch(color=chunkColorsPar['int_chunk_size_by_96'], label="par - chunk size by 96"))
    handles.append(mpatches.Patch(color=chunkColorsOld['int_default_chunk_size'], label="old - default"))
    handles.append(mpatches.Patch(color=chunkColorsOld['int_chunk_size_by_24'], label="old - chunk size by 24"))
    handles.append(mpatches.Patch(color=chunkColorsOld['int_chunk_size_by_48'], label="old - chunk size by 48"))
    handles.append(mpatches.Patch(color=chunkColorsOld['int_chunk_size_by_96'], label="old - chunk size by 96"))

    plt.legend(loc="upper left", handles=handles)
    plt.show()

if __name__ == "__main__":
    readCsv()