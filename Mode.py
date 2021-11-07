import csv
from collections import Counter

with open("HeightWeight.csv", newline = '') as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
HData = []
WData = []

for i in range(len(fileData)):
    numH = fileData[i][1]
    HData.append(float(numH))

for i in range(len(fileData)):
    numW = fileData[i][2]
    WData.append(float(numW))

n = len(HData)
dataH = Counter(HData)

m = len(WData)
dataW = Counter(WData)

rangeDataH = {
    "50-60": 0,
    "60-70": 0,
    "70-80": 0
}

rangeDataW = {
    "75-85" : 0,
    "85-95" : 0,
    "95-105" : 0,
    "105-115" : 0,
    "115-125" : 0,
    "125-135" : 0,
    "135-145" : 0,
    "145-155" : 0,
    "155-165" : 0,
    "165-175" : 0,
}


for height,occerence in dataH.items():
    if 50 < height < 60:
        rangeDataH["50-60"] += occerence
    elif 60 < height < 70:
        rangeDataH["60-70"] += occerence
    elif 70 < height < 80:
        rangeDataH["70-80"] += occerence

for height,occerence in dataW.items():
    if 75 < height < 85:
        rangeDataW["75-85"] += occerence
    elif 85 < height < 95:
        rangeDataW["85-95"] += occerence
    elif 95 < height < 105:
        rangeDataW["95-105"] += occerence
    elif 105 < height < 115:
        rangeDataW["105-115"] += occerence
    elif 115 < height < 125:
        rangeDataW["115-125"] += occerence
    elif 125 < height < 135:
        rangeDataW["125-135"] += occerence
    elif 135 < height < 145:
        rangeDataW["135-145"] += occerence
    elif 145 < height < 155:
        rangeDataW["145-155"] += occerence
    elif 155 < height < 165:
        rangeDataW["155-165"] += occerence
    elif 165 < height < 175:
        rangeDataW["165-175"] += occerence


modeRangeH, modeOccH = 0, 0
 
for range, occerence in rangeDataH.items():
    if occerence > modeOccH:
        modeRangeH = [int(range.split("-")[0]), int(range.split("-")[1])]
        modeOccH = occerence

modeH = float((modeRangeH[0] + modeRangeH[1])/2)


modeRangeW, modeOccW = 0, 0
 
for range, occerence in rangeDataW.items():
    if occerence > modeOccW:
        modeRangeW = [int(range.split("-")[0]), int(range.split("-")[1])]
        modeOccW = occerence

modeW = float((modeRangeW[0] + modeRangeW[1])/2)


print("The Mode Of the Height And The Weight Are : ", modeH, "and", modeW)