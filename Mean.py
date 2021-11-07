import csv

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
totalH = 0
m = len(WData)
totalW = 0


for i in HData:
    totalH += i
for i in WData:
    totalW += i


meanH = totalH/n
meanW = totalW/n

print("The Averages For Height and Weight Are : ", meanH, "and", meanW)