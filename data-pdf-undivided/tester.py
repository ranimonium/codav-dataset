from gen import *
from motherpdfdata import *

feature_dir = [
    "phonecalling",
    "phoneringing",
    "powerbattery",
    "powercharger",
    "smsreceived",
    "smssent",
    "wificonnected",
]

weekday_dir = [
    "Monday", 
    "Tuesday", 
    "Wednesday",
    "Thursday", 
    "Friday", 
    "Saturday", 
    "Sunday"
    ]


#### BUILD TEST PDF ####

testpdf = {}

## READY CONTENTS
for i in range(1,7):
    testpdf['user' + str(i)] = {}
    for feature in feature_dir:
        testpdf['user' + str(i)][feature] = {}
        for day in weekday_dir:
            testpdf['user' + str(i)][feature][day] = []

#finds the index of the value in the pdf to be used in getting the value in directory
def findhourandvalue(testline):
    # print testline
    # print "first line:", testpdf[testline[0]][testline[1]][testline[2]]
    for line in testpdf[testline[0]][testline[1]][testline[2]]:

        if line[0] == testline[3] and line[1] == testline[4]:
            return testpdf[testline[0]][testline[1]][testline[2]].index(line)
    return -1        

## BUILDS TESTPDF FROM TESTDATA
for testline in testdata:
    if testline[0] in testpdf.keys():
        indexinline = findhourandvalue(testline)
        if indexinline == -1:
            testpdf[testline[0]][testline[1]][testline[2]].append([testline[3],testline[4],1])
        else:
            testpdf[testline[0]][testline[1]][testline[2]][indexinline][2] += 1
    else:
        print "lol"
        testpdf[testline[0]][testline[1]][testline[2]] = [testline[3],testline[4],1]

# print testpdf['user1']['phonecalling']['Monday']

#### COMPARE TESTPDF WITH MOTHERPDF ####

# print testpdf

for u in range(1,7):
    for feature in feature_dir:
        for day in weekday_dir:
            for hourlydata in testpdf['user' + str(u)][feature][day]:
                [hour, value, newnumtime] = hourlydata
                indexatdirectory = motherpdf['user' + str(u)][feature][2].index(value)
                origvalue = motherpdf['user' + str(u)][feature][1][day][hour][indexatdirectory]
                print u, feature, day, hour, newnumtime, origvalue, (1 - abs(float(newnumtime - origvalue)/origvalue))

#index of shit
# [hour, value, numberoftimes] = testpdf['user1']['phonecalling']['Monday'][0]
# indexatdirectory = motherpdf['user1']['phonecalling'][2].index(value)
# origvalue = motherpdf['user1']['phonecalling'][1]['Monday'][hour][indexatdirectory]

# print numberoftimes, origvalue
# print (1 - abs(float(numberoftimes - origvalue)/origvalue))