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
HData.sort()

m = len(WData)
WData.sort()


if n%2 == 0:
    mH1 = HData[n//2]
    mH2 = HData[n//2 - 1]
    medianH = (mH1 + mH2)/2
else:
    medianH = HData[n//2]

if m%2 == 0:
    mW1 = WData[m//2]
    mW2 = WData[m//2 - 1]
    medianW = (mW1 + mW2)/2
else:
    medianW = WData[m//2]


print("The Medians For Height And Weight Are : ", medianH, "and", medianW)