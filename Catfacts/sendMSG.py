import smtplib


class smtpSetup():

    def __init__(self,message,username,password,sendTo,outgoingServer,port):

        self.msg = message
        self.to = sendTo
        self.user = username
        self.pwd = password
        self.outgoingServer = outgoingServer
        self.port = port


    def sendMSG(self):
        smtpserver = smtplib.SMTP(self.outgoingServer, self.port)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(self.user, self.pwd)
        header = 'To:' + self.to + '\n' + 'From: ' + self.user + '\n' + 'Subject:testing \n'
        print header
        print self.msg
        smtpserver.sendmail(self.user, self.to, self.msg)
        print 'done!'
        smtpserver.close()

    def changeMessage(self,message):
        self.msg = message

    def switchReceiver(self,receiver):
        self.to = receiver

    def switchAccount(self,account, password):
        self.user = account
        self.pwd = password

    def printMsg(self):
        print(self.msg)
if __name__ == "__main__":
    message = raw_input("Enter in the message \n")
    message = "you suck"
    username = "mikecolistro@gmail.com"
    password = raw_input("Enter password for: " + `username` + "\n")
    to = "8077081548@sms.rogers.com"
    outgoingServer = "smtp.gmail.com"
    port = "587"
    text = smtpSetup(message, username, password, to, outgoingServer, port)
    i = 0
    for i in range(0,50):
        text.sendMSG()