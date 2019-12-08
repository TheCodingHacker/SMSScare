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
            4) Prositite Order Fake SMS Scare
            5) Console Online Account Suspend SMS Scare
            6) Relationship Advice SMS Troll
            7) Reveal Prank

        """)
    smschoice=input("Enter a number: ")
    if(smschoice == "1"):
        bankscare()
    if(smschoice == "2"):
        orderscare()
    if(smschoice == "3"):
        phscare()
    if(smschoice == "4"):
        prossms()
    if(smschoice == "5"):
        consuspend()
    if(smschoice == "6"):
        relatadvice()
    if(smschoice == "7"):
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
    message= "Hello, " + name + ". " + "All messages you have recieved from this number were a prank, Please contact: " + yname + " as he was the one who executed this prank!"
    smssendus(number, message)

def revealuk():
    print("Reveal the prank!")
    name=input("Enter Target Name:")
    number=input("Enter Number (Incl. Country Code ex. +44 for UK): ")
    message= "Hello, " + name + ". " + "All messages you have recieved from this number were a prank, Please contact: " + yname + " as he was the one who executed this prank!"
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

def prossms():
    print("""

        Prosititute Fake SMS Scare

        1) US Send
        2) UK Send

    """)
    choice=input("Choose a number: ")
    if(choice == "1"):
        prossmsuk()
    if(choice == "2"):
        prossmsus()

def prossmsus():
    print("Prostitute Fake SMS Scare US Send")
    name=input("Enter Target Name: ")
    number=input("Enter Number (Incl. Country Code ex. +1 for US): ")
    prosname=input("Enter Prostitute's Name: ")
    message="Hey " + name + " its " + prosname + " I am on the way to your house now, dont have too much fun without me. I cant wait to see you. Love you"
    smsendus(number, message)

def prossmsuk():
    print("Prostitute Fake SMS Scare UK Send :: This Module uses a normal telephone number for functionality!")
    name=input("Enter Target Name: ")
    number=input("Enter Number (Incl. Country Code ex. +44 for UK): ")
    prosname=input("Enter Prostitute's Name: ")
    message="Hey " + name + " its " + prosname + " I am on the way to your house now, dont have too much fun without me. I cant wait to see you. Love you"
    smsenduk(number, message, "+441452260494")


def consuspend():
    print("""

        Console Fake SMS Scare!

        Choose a Console Provider

        1) PS4
        2) XBOX

    """)
    choice=input("Choose a number: ")
    if(choice == "1"):
        ps4send()
    if(choice == "2"):
        xboxsend()

def ps4send():
    print("""

        PS4 Account Suspension SMS Scare

        1) US Send
        2) UK Send

    """)
    choice=input("Choose a number: ")
    if(choice == "1"):
        ps4ussend()
    if(choice == "2"):
        ps4uksend()

def xboxsend():
    print("""

        Xbox Account Suspension SMS Scare

        1) US Send
        2) UK Send

    """)
    choice=input("Choose a number: ")
    if(choice == "1"):
        xboxussend()
    if(choice == "2"):
        xboxuksend()

def ps4ussend():
    print("""

        PS4 Account Suspension SMS Scare - US Setup

    """)
    name=input("Enter Target Name: ")
    number=input("Enter Number (Incl. Country Code ex. +1 for US): ")
    reason=input("Enter Ban Reason: ")
    days=input("Enter Ban Length (In Days): ")
    message="Hello, " + name + ": Your PS4 Account has been suspended for " + reason + " this ban will persist for " + days + " days. In the future please refrain from breaking the Sony Rules and Guidelines!"
    smssendus(number, message)

def ps4uksend():
    print("""

        PS4 Account Suspension SMS Scare - UK Setup

    """)
    name=input("Enter Target Name: ")
    number=input("Enter Number(Incl. County Code ex. +44 for UK): ")
    sonynum="SONYPLAYSTAT"
    reason=input("Enter Ban Reason: ")
    days=input("Enter Ban length (In Days): ")
    message="Hello, " + name + ": Your PS4 Account has been suspended for " + reason + " this ban will persist for " + days + " days. In the future please refrain from breaking the Sony Rules and Guidelines!"
    smsenduk(number, message, sonynum)


def xboxussend():
    print("""

        Xbox Account Suspension SMS Scare - US Setup

    """)
    name=input("Enter Target Name: ")
    number=input("Enter number(Incl. Country Code ex. +44 for UK): ")
    reason=input("Enter Ban Reason: ")
    days=input("Enter Ban Length (In Days): ")
    message="Hello, " + name + ": Your Xbox Account has been suspended for " + reason + " this ban will persist for " + days + " days. In the future please refrain from breaking the Microsoft Rules and Guidelines!"
    smssendus(number, message)

def xboxuksend():
    print("""

        Xbox Account Suspension SMS Scare - UK Setup

    """)
    name=input("Enter Target Name: ")
    number=input("Enter number(Incl. Country Code ex. +44 for UK): ")
    reason=input("Enter Ban Reason: ")
    days=input("Enter Ban Length (In Days): ")
    xboxnum="MICROSOFTGB"
    message="Hello, " + name + ": Your Xbox Account has been suspended for " + reason + " this ban will persist for " + days + " days. In the future please refrain from breaking the Microsoft Rules and Guidelines!"
    smssenduk(number, message, xboxnum)

def relatadvice():
    print("""

        Relationship Advice SMS troll

        1) US Send
        2) UK Send

    """)
    choice=input("Choose a number: ")
    if(choice == "1"):
        relatadviceus()
    if(choice == "2"):
        relatadviceuk()


def relatadviceus():
    name=input("Enter Target Name: ")
    number=input("Enter Number(Incl. County Code ex. +44 for UK): ")


def smssenduk(number, message, num):
    client = Client("" , "")
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
