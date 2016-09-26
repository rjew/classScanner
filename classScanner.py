import urllib2
import time
from twilio.rest import TwilioRestClient
import ssl

def checkIfOpen(url, name, search, occurences):
    context = ssl._create_unverified_context()
    response = urllib2.urlopen(url, context=context)
    webContent = response.read()
    if webContent.count(search) == occurences:
        print name + "Full"
        return False
    else:
        print name + "is OPEN!!!!!!!!!"
        accountSid = "some account" #removed accountSid
        authToken = "some token" #removed authToken
        twilioClient = TwilioRestClient(accountSid, authToken)
        myTwilioNumber = 1111111111 #removed myTwilioNumber 
        destCellPhone = 1111111111 #removed destCellPhone
        myMessage = twilioClient.messages.create(body = name + " is Open!!!", from_=myTwilioNumber, to=destCellPhone)
        return True
        
if __name__ == "__main__":
    cs181Found = False
    cs161Found = False
    ee113daFound = False
    ee180daFound = False
    engr183ewFound = False
    cs181 = 'https://sa.ucla.edu/ro/Public/SOC/Results?t=16F&sBy=classidnumber&id=187787200&btnIsInIndex=btn_inIndex'
    cs161 = 'https://sa.ucla.edu/ro/Public/SOC/Results?t=16F&sBy=classidnumber&id=187696200&btnIsInIndex=btn_inIndex'
    ee113da = 'https://sa.ucla.edu/ro/Public/SOC/Results?t=16F&sBy=classidnumber&id=190378200&btnIsInIndex=btn_inIndex'
    ee180da = 'https://sa.ucla.edu/ro/Public/SOC/Results?t=16F&sBy=classidnumber&id=190783200&btnIsInIndex=btn_inIndex'
    engr183ew = 'https://sa.ucla.edu/ro/Public/SOC/Results?t=16F&sBy=classidnumber&id=186799200&btnIsInIndex=btn_inIndex'
    while True:
        try:
            if not cs181Found:
                cs181Found = checkIfOpen(cs181, 'CS181', "Class Full", 3)
            if not cs161Found:
                cs161Found = checkIfOpen(cs161, 'CS161', "Class Full", 4)
            if not ee113daFound:
                ee113daFound = checkIfOpen(ee113da, 'EE113DA', "Waitlist Full", 2)
            if not ee180daFound:
                ee180daFound = checkIfOpen(ee180da, 'EE180DA', "Full (28)", 2)
            if not engr183ewFound:
                engr183ewFound = checkIfOpen(engr183ew, 'ENGR183EW', "0 capacity", 9)
            print ''
            time.sleep(300)
        except urllib2.URLError as e:
            print e.errno
            print e
            print ''
            time.sleep(60)