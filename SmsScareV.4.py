from twilio.rest import Client
from datetime import date
import random
import time

def main():
    print("""

        Welcome to Coder's and Geral's SMS Scare Software


        1) Send an SMS
        2) Credits
        3) Exit

    """)
    choice=input("Enter a number: ")
    if(choice == "1"):
        sms()
    if(choice == "2"):
        credits()
    if(choice == "3"):
        exit(0)

def sms():
    print("""

            SMS Scare

            1) Bank One Time Code Scare
            2) Fake Order
            3) PH Premium Fake SMS Scare
            4) Reveal Prank

        """)
    smschoice=input("Enter a number: ")
    if(smschoice == "1"):
        bankscare()
    if(smschoice == "2"):
        orderscare()
    if(smschoice == "3"):
        phscare()
    if(smschoice == "4"):
        reveal()

def credits():
    print("This program was made by Coder and Geral.")
    print("If you would like to contact us, you can reach us at our discord. https://discord.gg/CdnDyXJ")
    time.sleep(15)
    main()

def bankscare():
    print("""

        Bank Scare!

        1) US Send
        2) UK Send

    """)
    choice=input("Enter a number: ")
    if(choice == "1"):
        codescareus()
    if(choice == "2"):
        codescare()

def codescare():
    print("Bank One Time Code Scare!")
    number=input("Enter Number (Incl. Country Code ex. +44 For UK): ")
    bank=input("Enter Bank Name: ")
    banknum=input("Enter Number (10 LETTER BANK NAME ex. NATWESTENGB: ")
    message="Your one-time passcode is " + str(random.randint(111111,999999)) + ". Do not share this code with anyone. If you did not request a code, Please contact the bank immediately!"
    print("Sending Message!")
    smssenduk(number, message, banknum)

def codescareus():
    print("Bank One Time Code Scare!")
    number=input("Enter Number (Incl. Country Code ex. +1 For US): ")
    bank=input("Enter Bank Name: ")
    message="Your one-time passcode is " + str(random.randint(111111,999999)) + ". Do not share this code with anyone. If you did not request a code, Please contact the bank immediately!"
    print("Sending Message!")
    smssendus(number, message)

def orderscare():
    print("SMS Fake Order!")
    print("""

        1) US Send
        2) UK Send

        """)
    fakenum=input("Choose a country: ")
    if(fakenum == "1"):
        fakeordersetupus()
    if(fakenum == "2"):
        fakeordersetupuk()

def fakeordersetupus():
    print("Fake Order US Setup!")
    providor=input("Enter Shipping Provider: ")
    item=input("Enter Item: ")
    number=input("Enter Number (Incl. Country Code ex. +1 For US): ")
    name=input("Targets Name: ")
    date=input("Enter Delivery Date (6 Digit ex. 12/07/19): ")
    message="Hello " + name + ", Your order of: " + item + " will be delivered on the: " + date + ". Thank you for shipping with " + providor + " Order ID: " + str(random.randint(111111,999999))
    smssendus(number, message)

def fakeordersetupuk():
    print("Fake Order UK Setup!")
    providor=input("Enter Shipping Provider: ")
    item=input("Enter Item: ")
    number=input("Enter Number (Incl. Country Code ex. +44 For UK): ")
    provnum=input("Enter Number (10 LETTER PROVIDER NAME ex. UPSENDELIV: ")
    name=input("Targets Name: ")
    date=input("Enter Delivery Date (6 Digit ex. 07/12/19): ")
    message="Hello " + name + ", Your order of: " + item + " will be delivered on the: " + date + ". Thank you for shipping with " + providor + " Order ID: " + str(random.randint(111111,999999))
    smssenduk(number, message, provnum)

def phscare():
    print("""

        SMS Fake PH Premium Order!

        1) US Send
        2) UK Send

          """)
    phchoice=input("Enter Number: ")
    if(phchoice == "1"):
        phpremus()
    if(phchoice == "2"):
        phpremuk()

def phpremus():
    print("PH Prem Order Setup!")
    name=input("Enter Target Name: ")
    today = date.today()
    number=input("Enter Number (Incl. Country Code ex. +1 For US): ")
    message = "Hello " + name + ", Your PornHub Premium Subscription was Sucessfully Renewed Today! (" + str(today) + "), Head over to https://pornhub.com to check out our newest premium content!"
    smssendus(number, message)

def phpremuk():
    print("PH Prem Order Setup UK!")
    name=input("Enter Target Name: ")
    today = date.today()
    number=input("Enter Number (Incl. Country Code ex. +44 For UK): ")
    phnum=input("Enter Number (10 LETTER PROVIDER NAME ex. PORNHUBNUM: ")
    message = "Hello " + name + ", Your PornHub Premium Subscription was Sucessfully Renewed Today! (" + str(today) + "), Head over to https://pornhub.com to check out our newest premium content!"
    smssenduk(number, message, phnum)

def reveal():
    print("""

        Reveal the Prank!

        1) US
        2) UK

        """)
    choice=input("Choose a number: ")
    if(choice == "1"):
        revealus()
    if(choice == "2"):
        revealuk()

def revealus():
    print("Reveal the prank!")
    name=input("Enter Target Name: ")
    yname=input("Enter Your Name: ")
    number=input("Enter Number (Incl. Country Code ex. +1 For US): ")
    message= "Hello, " + name + ". " + "All messages you have recieved from this numer were a prank, Please contact: " + yname + " as he was the one who executed this prank!"
    smssendus(number, message)

def revealuk():
    print("Reveal the prank!")
    name=input("Enter Target Name:")
    number=input("Enter Number (Incl. Country Code ex. +44 for UK):")
    message= "Hello, " + name + ". " + "All messages you have recieved from this numer were a prank, Please contact: " + yname + " as he was the one who executed this prank!"
    def sender():
        print("""

        What way would you like to send the message?

        1) 10 Digit Word
        2) Preset Number

        """)
        choice=input("Choose a number: ")
        if(choice == 1):
            word=input("Enter Number to Send from (10 LETTER NAME ex. PORNHUBPREM): ")
            smssenuk(number,message,word)
        if(choice == 2):
            #Change the UK Number Below
            smssenuk(number,message,"+441452260494")

def smssenduk(number, message, num):
    client = Client("", "")
            #Client("Account SID", "API Token")
    message = client.messages \
                    .create(
                         body=message,
                         from_=num,
                         to=number
                     )
    print(message.sid)

def smssendus(number, message):
    client = Client("", "")
            #Client("Account SID", "API Token")
    message = client.messages \
                    .create(
                         body=message,
                         # Change the number below
                         from_='+17072025135',
                         to=number
                     )

    print(message.sid)

main()
