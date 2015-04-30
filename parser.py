import os
from datetime import date


cwd = os.getcwd()
outdir = "/data-parsed_ANN/"
folders = {
"":"", 
# "app": ["pid","recent"], 
# "audio": ["ringermode", "volume", "maxvolume"], 
# "hf": ["app", "locked"], 
# "phone": ["activeoperator", "roaming", "servicestate","celllocation", "signal", 
        # "sim", "idle", "ringing"], 
# "power": ["battery", "charger"], 
# "screen": ["brightness", "power"],
"sms": ["sms"]
# "sms": ["sent","received"],
# "wifi": ["connected", "scancomplete", "scan", "state"]

}


def makeDirs(user):
  for folder in folders:
    # print "HNGGHH", folder
    if not os.path.exists(cwd + outdir + str(user) + "/" + folder):
      os.makedirs(cwd + outdir + str(user) + "/" + folder)

def createOutFiles(user):
  userout = cwd + outdir + str(user) + "/"
  outfiles = {
    # 'airplane' : open( userout + "airplane.ssv", 'a'),
  }

  # print folders
  for folder in folders:
    for outfile in folders[folder]:
      outfiles[outfile] = open(userout + folder + "/" + outfile + ".ssv", 'a')

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


  smslines = []

  prevlineinvalid = False
  #process each line from <user>.csv
  for line in open("dataset_raw/" + str(user) + ".csv", 'r'):
  # for line in open("samplelines.csv", 'r'):
    


    if '(invalid date)' in line:
      if prevlineinvalid:
        break
      prevlineinvalid = True
      continue
    else:
      prevlineinvalid = False
    # line exploded by semicolon; parses date, fields, and values, 
    line_exbysemi = line[:-1].split(';')

    #string to be printed out; contains just timestamp yet
    timestamp = processTimeStamp(line_exbysemi)


    ############## PARSE PER FIELD ##############
    

    substr_exbybar = line_exbysemi[3].split('|')

      
    if "sms" in line_exbysemi[3]:
      if substr_exbybar[1] in ["sent","received"]:
        
        smslines.append((str(["sent","received"].index(substr_exbybar[1])) + "," + 
                  timestamp + ','.join(line_exbysemi[4].split(',')[:2])).split(',')) 


    # if len(smslines) > 10: # for testing
    #   break


  numlist = []
  maxlength = -1
  for l in smslines:
    try:
      if int(l[5]) > maxlength:
        maxlength = int(l[5])
    except IndexError, e:
      pass
    # print l
    if l[4] not in numlist:
      numlist.append(l[4])

  print numlist
  outfiles["sms"].write(str(numlist) + '\n')

  for l in smslines:
    length = 0
    if maxlength != -1:
      length = int(l[5])/(maxlength*1.00)
    
    indexlineout = [str(0) for i in range(len(numlist))]
    indexlineout[numlist.index(l[4])] = str(1)
    # print (  ' '.join(l[:4]) + ' ' + str(length) + ' ' + ' '.join(indexlineout)  + '\n')
    outfiles["sms"].write(  ' '.join(l[:4]) + ' ' + str(length) + ' ' + ' '.join(indexlineout) + '\n')


  for o in outfiles:
    outfiles.get(o).close()
