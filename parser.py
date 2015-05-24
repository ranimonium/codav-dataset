import os
from datetime import date


cwd = os.getcwd()
outdir = "/data-parsed-ANN-phonecalls/"
folders = {
# "":"", 
# "app": ["name"], 
"phone": ["calls"], 
# "power": ["battery", "charger"],
# "sms": ["sent","received"],
# "wifi": ["connected"]

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
    timestamp = ( str( (date(int(day[0]), int(day[1]), int(day[2])).weekday())/6.0 ) + "," + 
      str(int(time[0])/23.0) + "," + str(0 if int(time[1]) < 30 else 1 ) )

  return timestamp + ","


#iterate from user 1 to 6
for user in range(1,7):
  print "Processing data from User", user 
  
  makeDirs(user)  
  outfiles = createOutFiles(user)

  # count = 0
  calllines = []

  #process each line from <user>.csv
  for line in open("dataset_raw/" + str(user) + ".csv", 'r'):
  # for line in open("samplelines.csv", 'r'):
    # count += 1
    # if count > 150:
    #   break

    if "(invalid date)" in line:
      if len(calllines) < 5:
        continue
      break
    # line exploded by semicolon; parses date, fields, and values, 
    line_exbysemi = line.split(';')

    #string to be printed out; contains just timestamp yet
    timestamp = processTimeStamp(line_exbysemi)

    ############## PARSE PER FIELD ##############
    

    substr_exbybar = line_exbysemi[3].split('|')

    if "phone|" in line_exbysemi[3]:

      if substr_exbybar[1] in ["ringing","calling"]:
        # print line
        calllines.append((str(["ringing","calling"].index(substr_exbybar[1])) + "," + 
                  timestamp + ','.join(line_exbysemi[4].split(',')[:2])).split(',')) 

      # if len(calllines) > 5: # for testing
      #   break

  numlist = []
  for l in calllines:
    print l
    try:
      if l[4] not in numlist:
        numlist.append(l[4])
    except Exception, e:
      print e

  # print numlist
  outfiles['calls'].write(str(numlist))

  for l in calllines:
    
    indexlineout = [str(0) for i in range(len(numlist))]
    indexlineout[numlist.index(l[4])] = str(1)
    # print (' '.join(l[:4]) + ' ' + ' '.join(indexlineout) + "\n")
    outfiles['calls'].write(  ' '.join(l[:4]) + ' ' + ' '.join(indexlineout) + "\n")

  for o in outfiles:
    outfiles.get(o).close()