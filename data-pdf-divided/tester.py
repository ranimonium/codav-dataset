from gen import *
from motherpdfdata import *

feature_dir = [
    # "phonecalling",
    # "phoneringing",
    "powerbattery",
    "powercharger",
    # "smsreceived",
    # "smssent",
    "wificonnected"
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

# print testpdf['user1']['phonecalling']['Monday']

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
    # weight = 1.0/len(feature_dir)
    # for u in range(1,7):
    #     print "USER ", u
    #     for day in weekday_dir:
    #         print "\t", day
    #         totalscore = 0
    #         for feature in feature_dir:
    #             score = score_perfeature_inaday['user' + str(u)][day][feature] 
    #             totalscore += score*weight
    #             print "\t\t", feature, hour, score*weight
    #         print "CONFIDENCE LEVEL:", totalscore

for u in range(1,7):
    for feature in feature_dir:
        # print feature
        
        for day in weekday_dir:

            try:
                for hourlydata in testpdf['user' + str(u)][feature][day]:
                    
                    score_perfeature_inaday_perhour = {}
                    init_score_dict(score_perfeature_inaday_perhour)

                    [hour, testval, newnumtime] = hourlydata
                    indexatdirectory = motherpdf['user' + str(u)][feature][2].index(testval)
                    orignumtime = motherpdf['user' + str(u)][feature][1][day][hour][indexatdirectory]
                    
                    maxfeature_ina_day = motherpdf['user' + str(u)][feature][3][weekday_dir.index(day)] #max in a feature for a day

                    # DIVIDES ORIGNUM AND NEWNUM BY MAX OF THE DAY
                    # divvalue_orig = float(orignumtime)/maxfeature_ina_day
                    # divvalue_newnumtime = float(newnumtime)/maxfeature_ina_day
                    
                    divvalue_orig = float(orignumtime)
                    divvalue_newnumtime = float(newnumtime)

                    # threshold = divvalue_orig/3
                    # print divvalue_orig, divvalue_newnumtime, threshold
                    
                    threshold = maxfeature_ina_day/float(10)

                    score = 0
                    if divvalue_orig >= maxfeature_ina_day/float(2):
                        score = 1
                    elif divvalue_orig >= maxfeature_ina_day/float(5):
                        score = 0.5
                    elif divvalue_orig >= maxfeature_ina_day/float(10):
                        score = 0.25
                    # elif divvalue_orig < maxfeature_ina_day/float(10):
                        # score = -0.25
                    elif divvalue_orig < maxfeature_ina_day/float(5):
                        score = -0.25
                    elif divvalue_orig < maxfeature_ina_day/float(2):
                        score = -0.125


                    score_perfeature_inaday['user' + str(u)][day][feature] += score
                    score_perfeature_inaday_perhour['user' + str(u)][day][feature] += score

                    # printvalues(score_perfeature_inaday_perhour, hour)

            except Exception, e:
                pass

# printvalues(score_perfeature_inaday)
getconfidencelevel(score_perfeature_inaday)


