#!/usr/bin/env python

import sys
from operator import itemgetter

#
# This program simply represents the identity function.
#


change = 0

rows = []
rowsNumbers = []


top20 = []
mintuple = []

for line in sys.stdin:
    adjacency_row = []

    # split string input
    node_id, value = line.split("\t")


    # split into list
    value_list = value.split(',')
    # make list of values floats
    for i in range(len(value_list)):
        adjacency_row.append(float(value_list[i]))
    
    

    # get ranks
    new = adjacency_row[0]
    old = adjacency_row[1]

    # make row for sorting/finding top 20
    rowI = [node_id, new]

    if len(top20) != 20:
        top20.append(rowI)

        if mintuple == []:
            mintuple = rowI

        elif mintuple[1] > rowI[1]:
            mintuple = rowI

    elif mintuple[1] < rowI[1]:
        top20.remove(mintuple)
        top20.append(rowI)
        mintuple = rowI

        # get new min
        for j in top20:
            if j[1] < mintuple[1]:
                mintuple = j


    neighbors = ''
    for i in range(len(adjacency_row)):
        if i > 1:
            neighbors += ',' + str(adjacency_row[i])

    # keep track in case we need to keep going
    final_row = 'NodeId:' + node_id + '\t' + \
                            str(new) + ',' + str(old) + neighbors
                            

    # for printing
    rows.append(final_row)
    rowsNumbers.append(rowI)

    # accumulate the change
    change += abs(new - old)


# once we read in all the output, determine if we stop
if change < 10:
    
    sys.stderr.write(str(change))
    top20 = sorted(top20, key=itemgetter(1))[::-1]

    for i in range(len(top20)):
        sys.stdout.write("FinalRank:" + str(top20[i][1]) + '\t' + \
                            str(top20[i][0]) + '\n')

else:
    # output so we can restart
    for line in rows:
        sys.stdout.write(line + '\n')
