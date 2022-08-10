#!/usr/bin/python3
import csv
import math
from collections import defaultdict
import itertools


input_file = "Play_Tennis_Data_Set.csv"
output = "Rules_out.txt"

class AprioriAlg(object):
    def __init__(self, support, confidence):
        self.support = support
        self.confidence = confidence

    def groupItemsSet(self, labels, m):
        return set([label1.union(label2) for label1 in labels for label2 in labels
                    if len(label1.union(label2)) == m])

    def getCells(self, data):
        cells = set()
        for line in data:
            for cell in line:
                cells.add(frozenset([cell]))

        return cells
    
    def getData(self, file_path):
        data = []
        with open(file_path,'r') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                cells = []
                for cell in line:
                    cells.append(cell)
                    
                data.append(cells)

        headers = data[0]
        data = data[1:]
        pairs = []

        for transaction in data:
            r = set([(header, cell)
        for header, cell in zip(headers, transaction)])
            pairs.append(r)
        return pairs


    def getRules(self, r):
        rules = dict()
        for i, read in self.freq.items():
            for cell in read:
                if r.issubset(cell) and len(cell) > 1:
                    cell = cell.difference(r)
                    item_supp = self.getSupport(cell)
                    conf = item_supp / self.getSupport(cell)
                    if conf >= self.confidence:
                        rules[cell] = (item_supp, conf)
        return rules

    def alg(self, file_path):
        data = self.getData(file_path)
        cells = self.getCells(data)
        count =defaultdict(int)
        m = 1

        self.length = len(data)
        self.items = cells

        cur_freq= self.itemSup(data, cells,count, self.support)
        freq = dict()
        
        while cur_freq != set():
            
            freq[m] =cur_freq
            m = 1 +m
            upd = self.groupItemsSet(cur_freq, m)
            cur_freq = self.itemSup(data, upd, count, self.support)
            
        self.count = count
        self.freq = freq
        return count, freq


    
    def itemSup(self, data, cells, freq, support):
        itemSet = set()
        local = defaultdict(int)
        for cell in cells:
            freq[cell] += sum([1 for trans in data if cell.issubset(trans)])
            local[cell] += sum([1 for trans in data if cell.issubset(trans)])

        n = len(data)
        for cell, count in local.items():
            itemSet.add(cell) if float(count)/n >= support else None

        return itemSet

    def getSupport(self, cell):
        return self.count[cell] / self.length


if __name__ == '__main__':

    support = float(input("Enter Support : "))
    confidence = float(input("Enter Confidence : "))

    AprioriAlg = AprioriAlg(support, confidence)
    count, freq = AprioriAlg.alg(input_file)
    fileOut = open(output, "w")
    fileOut.write("Support={}\nConfidence={}\n\n".
                   format(support, confidence))
    fileOut.write("Rules:\n")
    index = 1

    #print rules
    for r in AprioriAlg.items:
        rules = AprioriAlg.getRules(r)
        for key, read in rules.items():
            keyList = list(key)[0]
            rList = list(r)[0]
            fileOut.write("Rule#{}: {{{} = {}}} => {{{} = {}}}".format(index, keyList[0], keyList[1], rList[0], rList[1]))
            fileOut.write("(Support = %.2f, Confidence = %.2f)\n\n" %(read[0], read[1]))
            index += 1
