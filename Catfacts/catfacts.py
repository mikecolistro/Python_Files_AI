import smtplib
import random
import sendMSG
import time
from sendMSG import *


#def __init__(self,message,username,password,sendTo,outgoingServer,port):

#open catfacts text file
text_file = open("catfacts.txt", "r")
#read lines to list lines
lines = text_file.readlines()
#find how many lines there are
x = len(lines)
#create a random number
randnum = random.randint(0,x)
#open file with all the gateways
sms_file = open("smsgateways.txt","r")
#read gateways into list smsgateways
smsgateways = sms_file.readlines()

#assign to value
to = '8076205022@txt.bell.ca'
gmail_user = 'catfactstbay@gmail.com'
gmail_pwd = 'catfacts'
randnum = 18
msg = lines[randnum]
text_file.close()
sms_file.close()
outgoingServer = "smtp.gmail.com"
port = 587

print"We got here"

smsMSG = smtpSetup(msg, gmail_user, gmail_pwd, to, outgoingServer, port)
newMsg = []
"""
if len(msg) > 130:
    i = 0
    x = 0
    y = 130
    for i in range(len(msg)/ 130):
        newMsg[i] = msg[x:-(y + x)]
        x = x + y
        print newMsg[i]
i = 0
for i in range(len(newMsg)):
    print(newMsg[i])
"""
"""
x = 130
y = 130
i = 0
testFlag = True
while testFlag:
    if msg[x] != " ":
        x = x - 1
    else:
        break
newMsg.append(msg[:x])
for i in range(len(msg)/130):
    while testFlag:
        if x + x < len(msg):
            if msg[x+x] != " ":
                x = x - 1
            else:
                break
        else:
            break
    newMsg.append(msg[x:x+x])
    x = x + 130
for i in range(len(newMsg)):
    if i != 0:
        #smsMSG.sendMSG()
        smsMSG.printMsg()
    smsMSG.changeMessage(newMsg[i])
    time.sleep(3)
"""

fd = "The term puss is the root of the principal word for cat in the Romanian term pisica and the root of secondary words in Lithuanian (puz) and Low German puus. Some scholars suggest that puss could be imitative of the hissing sound used to get a cats attention. As a slang word for the female pudenda, it could be associated with the connotation of a cat being soft, warm, and fuzzy."
chars = []
for line in fd:
   for c in line:
       chars.append(c)
print(chars)
newList = []
i = 0
j = 0
print(chars[i])
print(len(chars))
randomFlag = True
print(chars[:1])
while randomFlag:
    newList.append(chars[i][0])
    if i == 130:
        randomFlag = False
    i = i + 1
   # if len(newList[j])  == 130:
    #    j = j + 1
print(newList)
#smsMSG.sendMSG()
#smsMSG.printMsg()
#print(msg[x:x+x])
#smsMSG.sendMSG()
#message = msg
#username = gmail_user
#password = gmail_pwd
#sendTo = to
#outgoing
