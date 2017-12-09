#!/usr/bin/env python

'''
Created on Dec 7, 2017

@author: tuxy
'''
import csv
import sys
import argparse

parser = argparse.ArgumentParser(description='Process to convert USD to Euro in CSV, \
    Example:./cctest1.py -i input/sample.csv -o output/outcome2.csv --f 1 --m 1.8')
parser.add_argument('-i','--input', help='Input file path')
parser.add_argument('-o', '--output', help='Output file path')
parser.add_argument('-f', '--field', type = int, help='Convert CSV field N, Use intger.')
parser.add_argument('-m', '--multiplier', type = float, help='Multiply currency value by N for the current conversion rate, Use float.')
args = parser.parse_args()

input_file = args.input
output_file = args.output
multiplier = args.multiplier
field = args.field

def cconvert1(input_file, output_file, multiplier, field):

    with open(input_file,'rb') as incsv:
        with open(output_file, 'w') as outcsv:
            reader = csv.reader(incsv)
            csvwriter = csv.writer(outcsv)
        
            for row in reader:
                try:
                    oldprice = float(row[field])
                    newprice = oldprice * multiplier
                    print (str(oldprice) + ' to ' + str(newprice))
                    rowtemp = str(float(row[field]) *multiplier)
                    # Need to write a process to replace "." with ","
                    row[field] = rowtemp.replace('.',',',1)
                    csvwriter.writerows([row])
                    print (row)
                except ValueError:
                    csvwriter.writerows([row])
                    print (row[field])
             
            print (row)       
        incsv.close()
        
cconvert1(input_file, output_file, multiplier, field)