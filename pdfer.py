import os
import copy

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

cwd = os.getcwd()

# for user in range (1,7):
for user in range (1,7):

    #### PARSE AND FORMAT DATA ####

    rawdata = [line.strip() for line in open(cwd + "/data-parsed_ANN-sms/" + str(user) + "/sms/sms.ssv")]

    directory = rawdata[0]
    rawdata = [line.split(" ") for line in rawdata[1:]]

    #### OPEN OUTPUT FILES ####
    # fsent = open(cwd + "/data-parsed_PDF-sms-1/" + str(user) + "_sent.ssv","w")
    # frecv = open(cwd + "/data-parsed_PDF-sms-1/" + str(user) + "_recv.ssv","w")

    #### REBUILD DATASET ####

    #lists times of day in decimal form
    #serves as directory for the index and the times of day
    #format of day in "rawdata" : x/23.0 ; x -> hour of the day
    timeofday_dir_list = []
    for i in range(24):
        timeofday_dir_list.append(str(float(i/23.00))[:12])
    # print timeofday_dir_list

    weekday_dir = {
        str(float(0/6.0)) : "monday",
        str(float(1/6.0)) : "tuesday",
        str(float(2/6.0)) : "wednesday",
        str(float(3/6.0)) : "thursday",
        str(float(4/6.0)) : "friday",
        str(float(5/6.0)) : "saturday",
        str(float(6/6.0)) : "sunday",
    }

    # template for 
    data_dict = {}
    for i in range(7):
        data_dict[ weekday_dir[str(float(i/6.0))] ] = []

    data_list = [copy.deepcopy(data_dict), copy.deepcopy(data_dict)]  # ["sent","received"]

    # counts the number of sms recv/sent during the particular time of day and day of week
    for line in rawdata:
        # data_list[sent or recv][day of week]
        # data_list[ int(line[0]) ][ weekday_dir[line[1]] ].append( str(line[2] )[:12])
        data_list[ int(line[0]) ][ weekday_dir[line[1]] ].append(timeofday_dir_list.index( str(line[2] )[:12]))
        # print line[1], str(line[2])
    # generate normalized distribution function
    # print data_list[0]["Monday"]

    smstypes = ["sent","recv"]
    smscolors = ["green","violet"]
    for smstype in range(len(data_list)):
        for day in weekday_dir.values():
            data = data_list[smstype][day]
            
            fig, ax = plt.subplots()

            try:
                hist, bins, a = plt.hist(data, bins=[i for i in range(24)], color=smscolors[smstype], normed=True)
                ax.set_xticks(bins)

                plt.ylim([0,1])
                plt.xlim([0,24])

                plt.title("SMS " + smstypes[smstype].capitalize() + " on " + day.capitalize() + " - User " + str(user))
                plt.ylabel("Probability")
                plt.xlabel("Hours")

                plt.savefig(cwd + "/data-parsed_PDF-sms-1/fig/1.0/" + str(user) + "-" + smstypes[smstype] + "-" + day + ".png")
                plt.close(fig)
                print "Saved: " + str(user) + "-" + smstypes[smstype] + "-" + day + ".png"
            except Exception, e:
                print e
            # finally:
            #     continue
plt.close()
