import os
from datetime import date


cwd = os.getcwd()
outdir = "/data-parsed-pdf/"
folders = {
"":"", 
"app": ["name"], 
"phone": ["ringing", "calling"], 
"power": ["battery", "charger"],
"sms": ["sent","received"],
"wifi": ["connected"]

}


def makeDirs(user):
  for folder in folders:
    # print "HNGGHH", folder
    if not os.path.exists(cwd + outdir + str(user)):
      os.makedirs(cwd + outdir + str(user))

def createOutFiles(user):
  userout = cwd + outdir + str(user) + "/"
  outfiles = {}

  # print folders
  for folder in folders:
    for outfile in folders[folder]:
      outfiles[outfile] = open(userout + folder + "-" + outfile + ".ssv", 'a')
      # print userout + folder + "/" + outfile + ".ssv"

  return outfiles

def processTimeStamp(line_exbysemi):
  timestamp = line_exbysemi[2]

  if "invalid" not in line_exbysemi[2]:
    timestamp = line_exbysemi[2].split('T')
    day = timestamp[0].split('-')
    time = timestamp[1].split('.')[0].split(':')

    #reused variable
    timestamp = (day[1] + " " + day[2] + " " + 
      str(date(int(day[0]), int(day[1]), int(day[2])).weekday()) + " " + 
      time[0] + " " + time[1] + " " + time[2] )

  return timestamp + " "



#iterate from user 1 to 6
for user in range(1,7):
  print "Processing data from User", user 
  
  makeDirs(user)  
  outfiles = createOutFiles(user)

  count = 0
  #process each line from <user>.csv
  for line in open("dataset_raw/" + str(user) + ".csv", 'r'):
  # for line in open("samplelines.csv", 'r'):
  
    # line exploded by semicolon; parses date, fields, and values, 
    line_exbysemi = line.split(';')

    #string to be printed out; contains just timestamp yet
    timestamp = processTimeStamp(line_exbysemi)


    ############## PARSE PER FIELD ##############
    

    substr_exbybar = line_exbysemi[3].split('|')

    if "app|" in line_exbysemi[3]:

      if len(substr_exbybar) > 2 and substr_exbybar[2] in ["name"]:
        outfiles['name'].write(timestamp + line_exbysemi[4])


    elif "phone|" in line_exbysemi[3]:

      if substr_exbybar[1] in ["ringing","calling"]:
        outfiles[substr_exbybar[1]].write(timestamp + 
          ' '.join(line_exbysemi[4].split(',')))

    elif "sms" in line_exbysemi[3]:
      if substr_exbybar[1] in ["sent","received"]:
        outfiles[substr_exbybar[1]].write(timestamp + 
          ' '.join(line_exbysemi[4].split(',')))


    elif "power|" in line_exbysemi[3]:

      if "battery" == substr_exbybar[1] and substr_exbybar[2] == "level" :
        outfiles[substr_exbybar[1]].write(timestamp + line_exbysemi[4])
      if "charger" == substr_exbybar[1]:
        outfiles[substr_exbybar[1]].write(timestamp + line_exbysemi[4])
        

    elif "wifi" in line_exbysemi[3]:

      if substr_exbybar[1] in ["connected"] and substr_exbybar[3] == "ssid":
        outfiles[substr_exbybar[1]].write(timestamp + substr_exbybar[2] + "\n")


  for o in outfiles:
    outfiles.get(o).close()