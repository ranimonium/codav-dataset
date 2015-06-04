import os
import matplotlib as mpl
mpl.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# from user1.pdfdata import *
# user = 1

# from user2.pdfdata import *
# user = 2

# from user3.pdfdata import *
# user = 3

# from user4.pdfdata import *
# user = 4

from user5.pdfdata import *
user = 5

# from user6.pdfdata import *
# user = 6

cwd = os.getcwd()

weekday_dir = [
    "Monday", 
    "Tuesday", 
    "Wednesday",
    "Thursday", 
    "Friday", 
    "Saturday", 
    "Sunday"
    ]

feature_data = {
    # "appname" : [  "Applications",  appname_max_per_day,  appname_week_data  ],
    "phonecalling" : [  "Outgoing Calls",  phonecalling_max_per_day,  phonecalling_week_data  ],
    "phoneringing" : [  "Incoming Calls",  phoneringing_max_per_day,  phoneringing_week_data  ],
    # "powerbattery" : [  "Battery Level",  powerbattery_max_per_day,  powerbattery_week_data  ],
    # "powercharger" : [  "Battery Charger",  powercharger_max_per_day,  powercharger_week_data  ],
    "smsreceived" : [  "SMS Received",  smsreceived_max_per_day,  smsreceived_week_data  ],
    "smssent" : [  "SMS Sent",  smssent_max_per_day,  smssent_week_data  ],
    # "wificonnected" : [   "BSSID",  wificonnected_max_per_day,  wificonnected_week_data  ],
}


def plot3dbar(user, day, day_data, filename, m):
    
    xpos, ypos, zpos = [], [], []
    dz = []

    for hourlydata in range(len(day_data)):
        for value in day_data[hourlydata]:
            xpos.append(0 + hourlydata)
            ypos.append(day_data[hourlydata].index(value))
            zpos.append(0)
            dz.append(value)


    dx = np.ones(len(xpos))
    dy = np.ones(len(ypos))
    # print dx, dy, dz

    nrm=mpl.colors.Normalize(0,m)
    colors=cm.jet(nrm(dz))

    fig = plt.figure()
    ax = Axes3D(fig)
    if filename == "appname":
        ax = Axes3D(fig, azim=40,elev=25)
    # ax = fig.add_subplot(111, projection='3d')

    plt.ylabel(feature_data[filename][0])
    plt.xlabel('Time of the Day (Hours)')
    plt.title(feature_data[filename][0] + " on " + day.capitalize() + " - User " + str(user))

    cax,kw=mpl.colorbar.make_axes(ax,shrink=.75,pad=.02) #add colorbar with normalized range
    cb1=mpl.colorbar.ColorbarBase(cax,cmap=cm.jet,norm=nrm)
    
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors)
    # plt.show()
    plt.savefig(cwd + "/fig/" + str(user) + "-" + filename + "-" + day + ".png")
    plt.close(fig)

# plot3dbar(user, 'Monday', feature_data['phonecalling'][2]['Monday'], 'phonecalling', feature_data['phonecalling'][1][0])
# plot3dbar(user, 'Monday', data, 'phonecalling', feature_data['phonecalling'][1][0])


for day in weekday_dir:
    for feature in feature_data:
        plot3dbar(user, day, feature_data[feature][2][day], feature, feature_data[feature][1][0])


"""
import os
import matplotlib as mpl
mpl.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

from user2.pdfdata import *
user = 2

cwd = os.getcwd()

weekday_dir = [
    "Monday", 
    "Tuesday", 
    "Wednesday",
    "Thursday", 
    "Friday", 
    "Saturday", 
    "Sunday"
    ]


feature_data = {
    # "appname" : [  "Applications",  appname_max_per_day,  appname_week_data  ],
    "phonecalling" : [  "Outgoing Calls",  phonecalling_max_per_day,  phonecalling_week_data  ],
    "phoneringing" : [  "Incoming Calls",  phoneringing_max_per_day,  phoneringing_week_data  ],
    "powerbattery" : [  "Battery Level",  powerbattery_max_per_day,  powerbattery_week_data  ],
    "powercharger" : [  "Battery Charger",  powercharger_max_per_day,  powercharger_week_data  ],
    "smsreceived" : [  "SMS Received",  smsreceived_max_per_day,  smsreceived_week_data  ],
    "smssent" : [  "SMS Sent",  smssent_max_per_day,  smssent_week_data  ],
    "wificonnected" : [   "BSSID",  wificonnected_max_per_day,  wificonnected_week_data  ],
}


def plot3dbar(user, day, day_data, filename, m):
    
    xpos, ypos, zpos = [], [], []
    dz = []

    for hourlydata in range(len(day_data)):
        for value in day_data[hourlydata]:
            xpos.append(0 + hourlydata)
            ypos.append(day_data[hourlydata].index(value))
            zpos.append(0)
            dz.append(value)


    dx = np.ones(len(xpos))
    dy = np.ones(len(ypos))
    # print dx, dy, dz

    nrm=mpl.colors.Normalize(0,m)
    colors=cm.jet(nrm(dz))

    fig = plt.figure()
    ax = Axes3D(fig)
    # ax = Axes3D(fig, azim=45,elev=15)
    # ax = fig.add_subplot(111, projection='3d')

    plt.ylabel(feature_data[filename][0])
    plt.xlabel('Time of the Day (Hours)')
    plt.title(feature_data[filename][0] + " on " + day.capitalize() + " - User " + str(user))

    cax,kw=mpl.colorbar.make_axes(ax,shrink=.75,pad=.02) #add colorbar with normalized range
    cb1=mpl.colorbar.ColorbarBase(cax,cmap=cm.jet,norm=nrm)
    
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors)
    plt.savefig(cwd + "/fig/" + str(user) + "-" + filename + "-" + day + ".png")
    plt.close(fig)
    # plt.show()

plot3dbar(user, 'Monday', feature_data['phonecalling'][2]['Monday'], 'phonecalling', feature_data['phonecalling'][1][0])
# plot3dbar(user, 'Monday', data, 'phonecalling', feature_data['phonecalling'][1][0])


for day in weekday_dir:
    for feature in feature_data:
        plot3dbar(user, day, feature_data[feature][2][day], feature, feature_data[feature][1][0])



"""