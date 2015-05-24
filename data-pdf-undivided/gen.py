import random

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

# for phonecalls and sms only
testdata = []
for u in range(1,7):
    for feature in feature_dir:
        maxinday = max(motherpdf['user' + str(u)][feature][3])
        indexofmaxinday =  motherpdf['user' + str(u)][feature][3].index(maxinday) #day
        day = weekday_dir[indexofmaxinday]

        for hour in range(24):
            if maxinday in motherpdf['user' + str(u)][feature][1][day][hour]:
                indexof_max_featurevalue = motherpdf['user' + str(u)][feature][1][day][hour].index(maxinday)
                feature_value = motherpdf['user' + str(u)][feature][2][indexof_max_featurevalue]
                for i in range(random.randint(1, maxinday)):
                # for i in range(maxinday):
                    testdata.append(('user' + str(u), feature, day, hour, feature_value))
                break


# print testdata