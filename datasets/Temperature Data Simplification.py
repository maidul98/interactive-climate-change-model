#!/usr/bin/env python
# coding: utf-8
import csv
import numpy as np

with open('GlobalLandTemperaturesByCountry.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

data = data[1:]
countries = []

noBlanksData = list(filter(lambda x: x[1] != '' , data))

for datapoint in noBlanksData:
    datapoint[0] = int(datapoint[0][0:4])
    datapoint[1] = float(datapoint[1])
    countries.append(datapoint[3])
    
countries = list(dict.fromkeys(countries))

temperatureDataFiltered = list(filter(lambda x: x[0] >= 1880 and x[0] <= 2013, noBlanksData))

cleanedTempData = []

for i in range(1880,2014):
    for country in countries:
        tempPerYearPerCountry = list(filter(lambda x: x[0] == i and x[3] == country, temperatureDataFiltered))
        if(tempPerYearPerCountry == []):
            cleanedTempData.append([country+str(i), ''])
        else:
            numeratorList = list(zip(*tempPerYearPerCountry))[1]
            averageTemp = sum(numeratorList)/len(tempPerYearPerCountry)
            cleanedTempData.append([country+str(i), averageTemp])

with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(cleanedTempData)

