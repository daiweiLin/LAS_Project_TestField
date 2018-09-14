# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 21:45:28 2018

@author: Lin Daiwei
"""

import csv

if __name__ == '__main__':
    with open("csv_test.csv", 'a') as csvFile:
        writer = csv.writer(csvFile)
        row = ['4', ' Danny', ' New York']
        writer.writerow(row)

    

