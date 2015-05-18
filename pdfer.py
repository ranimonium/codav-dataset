import os
import copy
import matplotlib.pyplot as plt

cwd = os.getcwd()

# for user in range (1,7):
for user in range (4,5):

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
        timeofday_dir_list.append(str(float(i/23.0))[:12])

    weekday_dir = {
        str(float(0/6.0)) : "Monday",
        str(float(1/6.0)) : "Tuesday",
        str(float(2/6.0)) : "Wednesday",
        str(float(3/6.0)) : "Thursday",
        str(float(4/6.0)) : "Friday",
        str(float(5/6.0)) : "Saturday",
        str(float(6/6.0)) : "Sunday",
    }

    # template for 
    data_dict = {}
    for i in range(7):
        data_dict[ weekday_dir[str(float(i/6.0))] ] = [0 for j in range(24)]

    data_list = [copy.deepcopy(data_dict), copy.deepcopy(data_dict)]  # ["sent","received"]

    # counts the number of sms recv/sent during the particular time of day and day of week
    for line in rawdata:
        data_list[ int(line[0]) ][ weekday_dir[line[1]] ][ timeofday_dir_list.index( str(line[2] )[:12]) ] += 1
    
    print data_list
    # generate normalized distribution function
