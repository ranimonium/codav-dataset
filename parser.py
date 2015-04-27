import os
from datetime import date


cwd = os.getcwd()
outdir = "/data-parsed_ANN/"
folders = {
"":"", 
"app": ["pid","recent"], 
"audio": ["ringermode", "volume", "maxvolume"], 
"hf": ["app", "locked"], 
"phone": ["activeoperator", "roaming", "servicestate","celllocation", "signal", 
        "sim", "idle", "ringing"], 
"power": ["battery", "charger"], 
"screen": ["brightness", "power"],
"sms": ["sent","received"],
"wifi": ["connected", "scancomplete", "scan", "state"]

}


def makeDirs(user):
  for folder in folders:
    # print "HNGGHH", folder
    if not os.path.exists(cwd + outdir + str(user) + "/" + folder):
      os.makedirs(cwd + outdir + str(user) + "/" + folder)

def createOutFiles(user):
  userout = cwd + outdir + str(user) + "/"
  outfiles = {
    'airplane' : open( userout + "airplane.ssv", 'a'),
  }

  # print folders
  for folder in folders:
    for outfile in folders[folder]:
      outfiles[outfile] = open(userout + folder + "/" + outfile + ".ssv", 'a')
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
for user in range(2,3):
  print "Processing data from User", user 
  
  # if not os.path.exists(cwd + outdir + str(user)):
  #   os.makedirs(cwd + outdir + str(user))

  makeDirs(user)  
  outfiles = createOutFiles(user)

  #process each line from <user>.csv
  for line in open("dataset_raw/" + str(user) + ".csv", 'r'):
  # for line in open("samplelines.csv", 'r'):
    
    # line exploded by semicolon; parses date, fields, and values, 
    line_exbysemi = line.split(';')

    #string to be printed out; contains just timestamp yet
    timestamp = processTimeStamp(line_exbysemi)


    ############## PARSE PER FIELD ##############
    

    substr_exbybar = line_exbysemi[3].split('|')

      
    if line_exbysemi[3] == "airplane":
      outfiles['airplane'].write(timestamp + line_exbysemi[4])


    elif "app|" in line_exbysemi[3]:
        
      #---- pid
      if substr_exbybar[1].isdigit():
        outfiles['pid'].write(timestamp + substr_exbybar[1] + 
          " " + substr_exbybar[2] + " " + line_exbysemi[4])

      if "recent" in line_exbysemi[3]:
        outfiles['recent'].write(timestamp + substr_exbybar[2] + 
          " " + line_exbysemi[4])
        # 138394;42017750;2013-01-27T01:03:55.592+0000;app|recent|0;com.cyanogenmod.trebuchet/.Launcher


    elif "audio|" in line_exbysemi[3]:
      if "ringermode" == substr_exbybar[1]:
        outfiles[substr_exbybar[1]].write(timestamp + line_exbysemi[4])
        
      if "volume" == substr_exbybar[1] or "maxvolume" == substr_exbybar[1]:
        outfiles[substr_exbybar[1]].write(timestamp + substr_exbybar[2] + 
          " " + line_exbysemi[4])
        # store in (substr_exbybar[2] + ".csv") line_exbysemi[4]


    elif "hf|" in line_exbysemi[3]:
      if substr_exbybar[1] in ["locked","app"]:
        outfiles[substr_exbybar[1]].write(timestamp + line_exbysemi[4])


    elif "phone|" in line_exbysemi[3]:
      if substr_exbybar[1] in ["servicestate","roaming","activeoperator"]:
        outfiles[substr_exbybar[1]].write(timestamp + line_exbysemi[4])
      if substr_exbybar[1] in ["celllocation", "signal", "sim"]:
        outfiles[substr_exbybar[1]].write(timestamp + substr_exbybar[2] + 
          " " + line_exbysemi[4])
      if substr_exbybar[1] in ["idle","ringing"]:
        outfiles[substr_exbybar[1]].write(timestamp + 
          ' '.join(line_exbysemi[4].split(',')))


    elif "power|" in line_exbysemi[3]:
      if "battery" == substr_exbybar[1]:
        outfiles[substr_exbybar[1]].write(timestamp + substr_exbybar[2] + 
          " " + line_exbysemi[4])
      if "charger" == substr_exbybar[1]:
        outfiles[substr_exbybar[1]].write(timestamp + line_exbysemi[4])

    elif "screen" in line_exbysemi[3]:
      if "brightness" == substr_exbybar[1]:
        outfiles[substr_exbybar[1]].write(timestamp + substr_exbybar[2] + 
          " " + line_exbysemi[4])
      if "power" == substr_exbybar[1]:
        outfiles[substr_exbybar[1]].write(timestamp + line_exbysemi[4])

      
    elif "sms" in line_exbysemi[3]:
      if substr_exbybar[1] in ["sent","received"]:
        outfiles[substr_exbybar[1]].write(timestamp + 
          ' '.join(line_exbysemi[4].split(',')))


    elif "wifi" in line_exbysemi[3]:
      if substr_exbybar[1] in ["scan", "connected"]:
        outfiles[substr_exbybar[1]].write(timestamp + substr_exbybar[2] + 
          " " + substr_exbybar[3] + " " + line_exbysemi[4])
        # store substr_exbybar[2] (bssid), substr_exbybar[3] (field), line_exbysemi[4](value)
      elif substr_exbybar[1] in ["scancomplete","state"]:
        outfiles[substr_exbybar[1]].write(timestamp + line_exbysemi[4])



  for o in outfiles:
    outfiles.get(o).close()
