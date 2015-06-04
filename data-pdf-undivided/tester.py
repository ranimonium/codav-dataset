from gen import *
from motherpdfdata import *

feature_dir = [
    # "phonecalling",
    # "phoneringing",
    # "powerbattery",
    # "powercharger",
    # "smsreceived",
    # "smssent",
    # "wificonnected"
    "appname",
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
    try:
        if testline[0] in testpdf.keys():
            indexinline = findhourandvalue(testline)
            if indexinline == -1:
                testpdf[testline[0]][testline[1]][testline[2]].append([testline[3],testline[4],1])
            else:
                testpdf[testline[0]][testline[1]][testline[2]][indexinline][2] += 1
        else:
            print "lol"
            testpdf[testline[0]][testline[1]][testline[2]] = [testline[3],testline[4],1]
            
    except Exception, e:
        pass

print testpdf['user1']['appname']['Monday']



#### COMPARE TESTPDF WITH MOTHERPDF ####

def init_score_dict(score_perfeature_inaday, tohour=False):
    for u in range(1,7):
        score_perfeature_inaday['user' + str(u)] = {}
        for day in weekday_dir:
            score_perfeature_inaday['user' + str(u)][day] = {}
            for feature in feature_dir:
                score_perfeature_inaday['user' + str(u)][day][feature] = 0

score_perfeature_inaday = {}
init_score_dict(score_perfeature_inaday)

def printvalues(score_perfeature_inaday, hour=""):
    for u in range(1,7):
        print "USER ", u
        for day in weekday_dir:
            print "\t", day
            for feature in feature_dir:
                print "\t\t", feature, hour, score_perfeature_inaday['user' + str(u)][day][feature]

def getconfidencelevel(score_perfeature_inaday, hour=""):
    weights = []
    for u in range(1,7):
        print "USER ", u
        for day in weekday_dir:
            print "\t", day
            
            denom = 0.0
            for feature in feature_dir:
                # if score_perfeature_inaday['user' + str(u)][day][feature] < 0:
                denom += abs(score_perfeature_inaday['user' + str(u)][day][feature]) 

            totalscore = 0
            for feature in feature_dir:
                score = (score_perfeature_inaday['user' + str(u)][day][feature]/denom)
                print '\t\tScore', feature,score
                # print score
                totalscore += score
            print "\t\t\t\t\tCONFIDENCE LEVEL:", totalscore

