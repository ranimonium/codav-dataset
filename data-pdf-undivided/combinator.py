user = 1

combfile = open("motherpdfdata.py", "a")

content = {}

from user1.pdfdata import *

feature_data = {
    "phonecalling" : [  "Outgoing Calls",  phonecalling_week_data, phonecalling_directory,  phonecalling_max_per_day  ],
    "phoneringing" : [  "Incoming Calls",  phoneringing_week_data, phoneringing_directory,  phoneringing_max_per_day  ],
    "powerbattery" : [  "Battery Level",  powerbattery_week_data, powerbattery_directory,  powerbattery_max_per_day  ],
    "powercharger" : [  "Battery Charger",  powercharger_week_data, powercharger_directory,  powercharger_max_per_day  ],
    "smsreceived" : [  "SMS Received",  smsreceived_week_data, smsreceived_directory,  smsreceived_max_per_day  ],
    "smssent" : [  "SMS Sent",  smssent_week_data, smssent_directory,  smssent_max_per_day  ],
    "wificonnected" : [   "BSSID",  wificonnected_week_data, wificonnected_directory,  wificonnected_max_per_day  ],
}
"""
feature_data = {
    "phonecalling" : [  "Outgoing Calls",  phonecalling_week_data, phonecalling_directory,  phonecalling_max_per_day  ],
    "phoneringing" : [  "Incoming Calls",  phoneringing_week_data, phoneringing_directory,  phoneringing_max_per_day  ],
    "powerbattery" : [  "Battery Level",  powerbattery_week_data, powerbattery_directory,  powerbattery_max_per_day  ],
    "powercharger" : [  "Battery Charger",  powercharger_week_data, powercharger_directory,  powercharger_max_per_day  ],
    "smsreceived" : [  "SMS Received",  smsreceived_week_data, smsreceived_directory,  smsreceived_max_per_day  ],
    "smssent" : [  "SMS Sent",  smssent_week_data, smssent_directory,  smssent_max_per_day  ],
    "wificonnected" : [   "BSSID",  wificonnected_week_data, wificonnected_directory,  wificonnected_max_per_day  ],

        "phonecalling" : [  "Outgoing Calls",  phonecalling_week_data, phonecalling_directory  ],
    "phoneringing" : [  "Incoming Calls",  phoneringing_week_data, phoneringing_directory  ],
    "powerbattery" : [  "Battery Level",  powerbattery_week_data, powerbattery_directory  ],
    "powercharger" : [  "Battery Charger",  powercharger_week_data, powercharger_directory  ],
    "smsreceived" : [  "SMS Received",  smsreceived_week_data, smsreceived_directory  ],
    "smssent" : [  "SMS Sent",  smssent_week_data, smssent_directory  ],
    "wificonnected" : [   "BSSID",  wificonnected_week_data, wificonnected_directory  ],
}
"""
content['user1'] = feature_data

from user2.pdfdata import *

feature_data = {
    "phonecalling" : [  "Outgoing Calls",  phonecalling_week_data, phonecalling_directory,  phonecalling_max_per_day  ],
    "phoneringing" : [  "Incoming Calls",  phoneringing_week_data, phoneringing_directory,  phoneringing_max_per_day  ],
    "powerbattery" : [  "Battery Level",  powerbattery_week_data, powerbattery_directory,  powerbattery_max_per_day  ],
    "powercharger" : [  "Battery Charger",  powercharger_week_data, powercharger_directory,  powercharger_max_per_day  ],
    "smsreceived" : [  "SMS Received",  smsreceived_week_data, smsreceived_directory,  smsreceived_max_per_day  ],
    "smssent" : [  "SMS Sent",  smssent_week_data, smssent_directory,  smssent_max_per_day  ],
    "wificonnected" : [   "BSSID",  wificonnected_week_data, wificonnected_directory,  wificonnected_max_per_day  ],
}
content['user2'] = feature_data

from user3.pdfdata import *

feature_data = {
    "phonecalling" : [  "Outgoing Calls",  phonecalling_week_data, phonecalling_directory,  phonecalling_max_per_day  ],
    "phoneringing" : [  "Incoming Calls",  phoneringing_week_data, phoneringing_directory,  phoneringing_max_per_day  ],
    "powerbattery" : [  "Battery Level",  powerbattery_week_data, powerbattery_directory,  powerbattery_max_per_day  ],
    "powercharger" : [  "Battery Charger",  powercharger_week_data, powercharger_directory,  powercharger_max_per_day  ],
    "smsreceived" : [  "SMS Received",  smsreceived_week_data, smsreceived_directory,  smsreceived_max_per_day  ],
    "smssent" : [  "SMS Sent",  smssent_week_data, smssent_directory,  smssent_max_per_day  ],
    "wificonnected" : [   "BSSID",  wificonnected_week_data, wificonnected_directory,  wificonnected_max_per_day  ],
}

content['user3'] = feature_data

from user4.pdfdata import *

feature_data = {
    "phonecalling" : [  "Outgoing Calls",  phonecalling_week_data, phonecalling_directory,  phonecalling_max_per_day  ],
    "phoneringing" : [  "Incoming Calls",  phoneringing_week_data, phoneringing_directory,  phoneringing_max_per_day  ],
    "powerbattery" : [  "Battery Level",  powerbattery_week_data, powerbattery_directory,  powerbattery_max_per_day  ],
    "powercharger" : [  "Battery Charger",  powercharger_week_data, powercharger_directory,  powercharger_max_per_day  ],
    "smsreceived" : [  "SMS Received",  smsreceived_week_data, smsreceived_directory,  smsreceived_max_per_day  ],
    "smssent" : [  "SMS Sent",  smssent_week_data, smssent_directory,  smssent_max_per_day  ],
    "wificonnected" : [   "BSSID",  wificonnected_week_data, wificonnected_directory,  wificonnected_max_per_day  ],
}

content['user4'] = feature_data

from user5.pdfdata import *

feature_data = {
    "phonecalling" : [  "Outgoing Calls",  phonecalling_week_data, phonecalling_directory,  phonecalling_max_per_day  ],
    "phoneringing" : [  "Incoming Calls",  phoneringing_week_data, phoneringing_directory,  phoneringing_max_per_day  ],
    "powerbattery" : [  "Battery Level",  powerbattery_week_data, powerbattery_directory,  powerbattery_max_per_day  ],
    "powercharger" : [  "Battery Charger",  powercharger_week_data, powercharger_directory,  powercharger_max_per_day  ],
    "smsreceived" : [  "SMS Received",  smsreceived_week_data, smsreceived_directory,  smsreceived_max_per_day  ],
    "smssent" : [  "SMS Sent",  smssent_week_data, smssent_directory,  smssent_max_per_day  ],
    "wificonnected" : [   "BSSID",  wificonnected_week_data, wificonnected_directory,  wificonnected_max_per_day  ],
}

content['user5'] = feature_data

from user6.pdfdata import *

feature_data = {
    "phonecalling" : [  "Outgoing Calls",  phonecalling_week_data, phonecalling_directory,  phonecalling_max_per_day  ],
    "phoneringing" : [  "Incoming Calls",  phoneringing_week_data, phoneringing_directory,  phoneringing_max_per_day  ],
    "powerbattery" : [  "Battery Level",  powerbattery_week_data, powerbattery_directory,  powerbattery_max_per_day  ],
    "powercharger" : [  "Battery Charger",  powercharger_week_data, powercharger_directory,  powercharger_max_per_day  ],
    "smsreceived" : [  "SMS Received",  smsreceived_week_data, smsreceived_directory,  smsreceived_max_per_day  ],
    "smssent" : [  "SMS Sent",  smssent_week_data, smssent_directory,  smssent_max_per_day  ],
    "wificonnected" : [   "BSSID",  wificonnected_week_data, wificonnected_directory,  wificonnected_max_per_day  ],
}

content['user6'] = feature_data

combfile.write("motherpdf = {}\n")
for user in content:
	combfile.write("motherpdf['" + user + "'] = " + str(content[user]) + "\n")
combfile.close()