# Code version: 0.0.1 
# Build from: 09.02.2021 00:01
# Created By Mittod
#-----------------------------------------------------------------------------------------------------------------------------------#
#   TO DO:                                                                                                                          #
#       -- Header ASCCI                                                                                                             #
#       -- More settings, like a a lot of adresses email to send. Timer, custom text, custom SMTP, something else.                  #
#       -- GITHUB                                                                                                                   #
#       -- Crossplatform                                                                                                            #
#-----------------------------------------------------------------------------------------------------------------------------------#


import json
import random
from colorama import init
from colorama import Fore, Back, Style
from os import system, name, path 
import smtplib
import time

class message:
    def __init__(self, frommail, tomail, objectmessage, text):
        self.frommail = frommail
        self.tomail = tomail 
        self.objectmessage = objectmessage
        self.text = text  #locate to file or text --> ? 
    def check(self):
        print(Fore.GREEN + '\nFrom: ' + Fore.WHITE + self.frommail, Fore.GREEN + '\nTo: ' + Fore.WHITE + self.tomail, Fore.GREEN + '\nObject: ' + Fore.WHITE + self.objectmessage, Fore.GREEN + '\nText: ' + Fore.WHITE + self.text)
        main()
 
class SMTP_server:
    def __init__(self, name, port, login, pwd, delay):
        self.name = name
        self.port = port
        self.login = login
        self.pwd = pwd
        self.delay = delay

    def check(self):
        print(Fore.GREEN + '\nSMPT Server: '+ Fore.WHITE+ self.name, Fore.GREEN +'\nSMTP Server port: '+ Fore.WHITE+ str(self.port),Fore.GREEN +'\nSMTP Server login: '+ Fore.WHITE + self.login,Fore.GREEN +'\nSMTP Server password: '+ Fore.WHITE + self.pwd + Fore.WHITE)
        main()

server = SMTP_server("yandex.com", 485, "", "", "")
message = message('', '', '', '')

banner_1 = '''{0}
                           .oMc
                        .MMMMMP
                      .MM888MM
....                .MM88888MP
MMMMMMMMb.         d8MM8tt8MM
 MM88888MMMMc `:' dMME8ttt8MM
  MM88tt888EMMc:dMM8E88tt88MP
   MM8ttt888EEM8MMEEE8E888MC
   `MM888t8EEEM8MMEEE8t8888Mb
    "MM88888tEM8"MME88ttt88MM
     dM88ttt8EM8"MMM888ttt8MM
     MM8ttt88MM" " "MMNICKMM"
     3M88888MM"      "MMMP"
      "MNICKM"
 {1}'''.format(Fore.MAGENTA, Fore.WHITE)

banner_2 = '''{0}
            ._                                            ,
             (`)..                                    ,.-')
              (',.)-..                            ,.-(..`)         
               (,.' ,.)-..                    ,.-(. `.. )                    
                (,.' ..' .)-..            ,.-( `.. `.. )                     
                 (,.' ,.'  ..')-.     ,.-( `. `.. `.. )                      
                  (,.'  ,.' ,.'  )-.-('   `. `.. `.. )                       
                   ( ,.' ,.'    _== ==_     `.. `.. )                        
                    ( ,.'   _==' ~  ~  `==_    `.. )                     
                     \  _=='   ----..----  `==_   )                     
                  ,.-:    ,----___.  .___----.    -..                        
              ,.-'   (   _--====_  \/  _====--_   )  `-..                 
          ,.-'   .__.'`.  `-_I0_-'    `-_0I_-'  .'`.__.  `-..     
      ,.-'.'   .'      (          |  |          )      `.   `.-..  
  ,.-'    :    `___--- '`.__.    / __ \    .__.' `---___'    :   `-..      
-'_________`-____________'__ \  (O)  (O)  / __`____________-'________`-     
                            \ . _  __  _ . /                               
                             \ `V-'  `-V' |                                 
                              | \ \ | /  /                                 
                               V \ ~| ~/V                                   
                                |  \  /|                                    
                                 \~ | V             - SCRIPT CREATED BY MITTOD             
                                  \  |                                        
                                   VV {1}'''.format(Fore.RED, Fore.WHITE)

def do_banner():
    banner = random.choice([banner_1, banner_2])
    print(banner)

do_banner()
def check_emails():
    if path.exists("mail.json"):
        f = open('mail.json',)
        data = json.load(f)
        print('')
        mailnumber = 0
        print('There is', len(data['mails']), 'adresses: ') 
        for i in data['mails']:
            mailnumber += 1
            if not i['wasUsed']:
                print(Fore.GREEN, '[',mailnumber,']', i['email'],  Fore.WHITE)
            else: 
                print(Fore.RED,'[',mailnumber,']',  i['email'],  Fore.WHITE)
            if (mailnumber >= 3) and (len(data['mails']) - mailnumber != 0):
                print(Fore.LIGHTGREEN_EX, 'And', len(data['mails']) - mailnumber, 'more...' + Fore.WHITE)
                break
        f.close()
    else:
        create_db()
        check_emails()
    main()

def validate_emails():
    valide = []
    f = open('mail.json')
    data = json.load(f)
    i = 0
    for i in data['mails']:
        if i['wasUsed'] == False:
            valide.append(i)
    return valide



def send_email():
    valide = validate_emails()
    i = 0
    for i in range(0, len(valide)):
        try: 
            smtpObj = smtplib.SMTP_SSL('smtp.yandex.com', 465)
            smtpObj.ehlo()
            smtpObj.login('an0n.q@yandex.ru','ekyokolaosjxrrbj')
            message = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (server.login, 'blueheadmtd@ya.ru', '', 'email_text')
            smtpObj.sendmail("an0n.q@yandex.ru","blueheadmtd@ya.ru", message)
            smtpObj.quit()
            print(Fore.GREEN, 'Сообщение отправлено!', Fore.WHITE)
        except:
            print(smtplib.SMTPResponseException)
            print(Fore.RED + "None" + Fore.WHITE)
    main()

def clear():
    if name == 'nt':
        system('cls')
    else: 
        system('clear')
    main()
    
def set_smtp():
    try:
        server.name = input(Fore.GREEN + '\nSet Server name: '+ Fore.WHITE)
        server.login = input(Fore.GREEN + '\nSet Login: '+ Fore.WHITE)
        server.port = input(Fore.GREEN + '\nSet Port: '+ Fore.WHITE)
        server.pwd = input(Fore.GREEN + '\nSet Password: '+ Fore.WHITE)
        server.delay = int(input(Fore.GREEN + '\nSet Send delay (sec)' + Fore.WHITE))
        main()
    except:
        print(Fore.RED + 'Error!' + Fore.WHITE)

def set_email():
    try: 
        message.frommail = input(Fore.GREEN + '\nSet From: ' + Fore.WHITE)
        message.tomail = input(Fore.GREEN + '\nSet To: ' + Fore.WHITE)
        message.object = input(Fore.GREEN + '\nSet Object: ' + Fore.WHITE)
        message.text = input(Fore.GREEN + '\nSet Text: ' + Fore.WHITE)
    except:
        print(Fore.RED + '\nSomething went wrong\nPlease try again or leave bug-report' + Fore.WHITE)
    main()

def create_db():
    print(Fore.YELLOW + "\nCreating database file...\n" + Fore.WHITE)
    with open("mail.json", "w") as outfile:
            data = {}
            data['mails'] = []
            json.dump(data, outfile)

def write_json(data): 
    with open('mail.json','w') as f: 
        json.dump(data, f, indent=4) 

def addAddress():
    if path.exists("mail.json"):
        toUpdate = {}
        address = input('Input address one or more with comma: ')
        address = address.replace(', ', ',')
        addresslist = address.split(',')
        for i in addresslist:
            if i.find('@') != -1:
                toUpdate = {"email": i, "wasUsed": False}
                with open("mail.json") as file:
                    data = json.load(file)
                    newdata = data['mails']
                    if not (next((item for item in newdata if item["email"] == i), False)):
                        newdata.append(toUpdate)
                        write_json(data)
                    else: 
                        print(Fore.RED + i + " Already exist!" + Fore.WHITE)
            else:
                print(Fore.RED + "ERROR! Please check email: " + Fore.LIGHTRED_EX + i + Fore.WHITE)
    else:
        create_db()
        addAddress()


        
    main()


def main():
    print(Fore.BLUE + '''
    [0] Check e-mails                 [3] Check SMTP settings                 [6]Add address to DB
    [1] Send e-mail                   [4] Check e-mail settings
    [2] Set SMTP                      [5] Set e-mail settings
    
    [69] Quit                         [99] Clear ''' + Fore.WHITE)
    count = int(input(Fore.CYAN + '\nChoose function: ' + Fore.WHITE))
    if count == 0:
        check_emails()
    if count == 1:
        send_email()
    if count == 2:
        set_smtp()
    if count == 3:
        server.check()
    if count == 4:
        message.check()
    if count == 5:
        set_email()
    if count == 6:
        addAddress()
    if count == 69:
        quit()
    if count == 99:
        clear()

main()
