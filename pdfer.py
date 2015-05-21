import os
import copy

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

cwd = os.getcwd()


def appname(type, line, week_data, directory):

    # if name not in directory
    if line[6] not in directory:
        # add name to directory list
        directory.append(line[6])
        # and for each day of the week
        for day in week_data.keys():
            # and for each hour of the day
            for h in range(24):
                # add a  0 to allow space for the frequency of the name
                week_data[day][h].append(0)

    # then we increment it by one
    # print week_data
    # print int(line[2])
    # print weekday_dir[ int(line[2]) ]
    # print line[3]
    # print directory.index(line[6])
    # print week_data[ weekday_dir[int(line[2])] ][int(line[3])]
    # print week_data[ weekday_dir[int(line[2])] ][int(line[3])][ directory.index(line[6]) ]
    week_data[ weekday_dir[int(line[2])] ][int(line[3])][ directory.index(line[6]) ] += 1


def phone(type, line, week_data, directory):
    pass

def power(type, line, week_data, directory):
    pass

def sms(type, line, week_data, directory):
    pass

def wificonnected(type, line, week_data, directory):
    pass






# timestamp --> month day weekday hours minutes seconds

fcns = {
    "app-name" : appname, # timestamp appname
    # "phone-calling" : phone, # timestamp phonenumber
    # "phone-ringing" : phone, # timestamp phonenumber
    # "power-battery" : power, # timestamp batterylevel
    # "power-charger" : power, # timestamp sourcetype
    # "sms-received" : sms, # timestamp phonenumber
    # "sms-sent" : sms, # timestamp phonenumber
    # "wifi-connected" : wificonnected, # timestamp bssid
    }

weekday_dir = [
    "monday", "tuesday", "wednesday",
    "thursday", "friday", "saturday", "sunday"
    ]



for user in range (1,7):

    # stores your matrices
    week_data = {}
    for day in weekday_dir:
        # stores your matrix for a single day
        # this list contains empty lists that will soon store your 
        # frequency distribution per name
        week_data[day] = [[] for i in range(24)] 


    # stores contact numbers, ssid, battery level?, app names
    directory = []


    for filename in fcns.keys():

        #### READ DATA ####
        rawdata = [(line.strip()).split(" ") for line in open(cwd + 
            "/data-parsed-pdf/" + str(user) + "/" + filename + ".ssv")]

        # try:

        #### POPULATE DISTRIBUTION FCN ####
        for line in rawdata:
            fcns[filename](filename.split('-')[1], line, week_data, directory)
        # except Exception, e:
            # print line, e

        print week_data
        
        #### PLOT 3D BAR GRAPH ####
        

        
plt.close()
