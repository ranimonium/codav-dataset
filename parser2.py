import os
import copy

cwd = os.getcwd()

filenames = [
    "app-name", # timestamp appname
    "phone-calling", # timestamp phonenumber
    "phone-ringing", # timestamp phonenumber
    # "power-battery" : power, # timestamp batterylevel
    # "power-charger" : power, # timestamp sourcetype
    # "sms-received" : sms, # timestamp phonenumber
    # "sms-sent" : sms, # timestamp phonenumber
    # "wifi-connected" : wificonnected, # timestamp bssid
    ]

for user in range(1,7):
    print "Processing for user ", user

    for filename in filenames:

        print filename
        #### READ DATA ####
        rawdata = [(line.strip()).split(" ") for line in open(cwd + 
            "/data-parsed-pdf/" + str(user) + "/" + filename + ".ssv")]

        fout = open(cwd + "/data-ANN-2/" + str(user) + "/" + filename + ".ssv", "a") 

        directory = []
        for line in rawdata:
            try:
                if line[6] not in directory:
                    directory.append(line[6])
            except Exception, e:
                print e
                break

        fout.write(str(directory) + "\n")
        for line in rawdata:
            try:
                indexlineout = [str(0) for i in range(len(directory))]
                indexlineout[directory.index(line[6])] = str(1)

                minute = '0'
                if int(line[4]) > 30:
                    minute = '1'
                fout.write( str(int(line[2])/6.0) + " " + str(int(line[3])/23.0) + " " + minute + " " + " ".join(indexlineout) + "\n" )
                
            except Exception, e:
                print e

        fout.close()
