__author__ = 'Michael'
import random

class Contacts():
    def __init__(self,file):
        #file should be formatted so one contact perline should be 0 digits number
        text_file = open(file, "r")
        #read lines to list lines
        self.lines = text_file.readlines()
        #find how many lines there are
        self.x = len(self.lines)
        t = 0
        for t in range(0,self.x -1):
             self.lines[t] = self.lines[t][:-1]

    def printAll(self):
        t = 0
        for t in range(0,self.x):
            print(self.lines[t])

    def getAll(self):
        return self.lines

    def getIndex(self,i):
        return self.lines[i]

    def search(self,string):
        t = 0
        for t in range(0,self.x):
            if string == self.lines[t]:
                return True

    def searchIndex(self,string):
        t = 0
        for t in range(0,self.x):
            if string == self.lines[t]:
                return t

    def pickRand(self):
        #create a random number
        self.randnum = random.randint(0,self.x)
        msg = self.lines[self.randnum]
        return msg

if __name__ == "__main__":
    contacts = Contacts("contacts.txt")
    print contacts.pickRand()
    string = '8072521717'
    print contacts.search(string)
    print contacts.searchIndex(string)