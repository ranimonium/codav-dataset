import os
import copy

import matplotlib as mpl
mpl.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# from weekdata import *

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

    week_data[ weekday_dir[int(line[2])] ][int(line[3])][ directory.index(line[6]) ] += 1


def phone(type, line, week_data, directory):
    appname(type, line, week_data, directory)

def power(type, line, week_data, directory):
    appname(type, line, week_data, directory)

def sms(type, line, week_data, directory):
    appname(type, line, week_data, directory)

def wificonnected(type, line, week_data, directory):
    appname(type, line, week_data, directory)

# timestamp --> month day weekday hours minutes seconds
fcns = {
    "app-name" :  [appname, "Applications"], # timestamp appname

    "phone-calling" : \
    [phone, "Outgoing Calls"], # timestamp phonenumber
    "phone-ringing" : [phone, "Incoming Calls"], # timestamp phonenumber
    "power-battery" : [power, "Battery Level"], # timestamp batterylevel
    "power-charger" : [power, "Battery Level"], # timestamp sourcetype
    "sms-received" : [sms, "SMS Received"], # timestamp phonenumber
    "sms-sent" : [sms, "SMS Sent"], # timestamp phonenumber
    "wifi-connected" : [wificonnected, "BSSID"], # timestamp bssid
    }

weekday_dir = [
    "Monday", 
    "Tuesday", 
    "Wednesday",
    "Thursday", 
    "Friday", 
    "Saturday", 
    "Sunday"
    ]


def plot3dbar(user, day, day_data, filename, m):
    
    xpos, ypos, zpos = [], [], []

    dx = np.ones(len(xpos))
    dy = np.ones(len(ypos))
    dz = []

    for hourlydata in range(len(day_data)):
        for value in day_data[hourlydata]:
            xpos.append(0 + hourlydata)
            ypos.append(day_data[hourlydata].index(value))
            zpos.append(0)
            dz.append(value)

    nrm=mpl.colors.Normalize(0,m)
    colors=cm.jet(nrm(dz))

    fig = plt.figure()
    ax = Axes3D(fig, azim=45,elev=15)

    plt.ylabel(fcns[filename][1])
    plt.xlabel('Time of the Day (Hours)')
    plt.title(fcns[filename][1] + " on " + day.capitalize() + " - User " + str(user))

    cax,kw=mpl.colorbar.make_axes(ax,shrink=.75,pad=.02) #add colorbar with normalized range
    cb1=mpl.colorbar.ColorbarBase(cax,cmap=cm.jet,norm=nrm)
    
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors)
    plt.show()



for user in range (1,7):



    for filename in fcns.keys():

        # stores your matrices
        week_data = {}
        for day in weekday_dir:
            # stores your matrix for a single day
            # this list contains empty lists that will soon store your 
            # frequency distribution per name
            week_data[day] = [[] for i in range(24)] 


        #### READ DATA ####
        rawdata = [(line.strip()).split(" ") for line in open(cwd + 
            "/data-parsed-pdf/" + str(user) + "/" + filename + ".ssv")]

        # stores contact numbers, ssid, battery level?, app names
        directory = []


        try:
            #### POPULATE DISTRIBUTION FCN ####
            for line in rawdata:
                if "(invalid" in line:
                    break
                fcns[filename][0](filename.split('-')[1], line, week_data, directory)

        except Exception, e:
            print line, e

        if filename == 'power-charger':
            directory = ['disconnected', 'usb', 'ac']
        elif filename == 'power-battery':
            directory = [str(i) for i in range(101)]

        # print week_data
        
        max_per_day = []
        #### NORMALIZE AND PLOT ####
        for day in week_data:
            s = 0
            for d in week_data[day]:
                s += sum(d)

            if s == 0:
                print("S IS 0 -- " + str(user) + " " + filename + " " + day)
                s = 1
            
            m = 0
            for hourlydata in week_data[day]:
                for i in range(len(hourlydata)):
                    hourlydata[i] = float(hourlydata[i])/s
                if max(hourlydata) > m:
                    m = max(hourlydata)

            max_per_day.append(m)
            
            ###  PLOT 3D BAR GRAPH  ###
            # plot3dbar(user, day, week_data[day], filename, m)
        print(str(user) + " print directory " + filename)

        pdfile = open(cwd + "/data-pdf/user" + str(user) + "/pdfdata.py", "w")
        pdfile.write("max_per_day = " + str(max_per_day) + "\n")
        pdfile.write("week_data = " + str(week_data) + "\n")
        pdfile.write( "\n" + "".join(filename.split('-')) + "_directory = " + str(directory) + "\n\n")
        pdfile.close()
        
plt.close()
