# Code version: 0.04
# Build from: 20.04.2021 00:01
# Created By Mittod

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
        self.text = text

    def check(self):
        print(Fore.GREEN + '\nFrom: ' + Fore.WHITE + self.frommail, Fore.GREEN + '\nTo: ' + Fore.WHITE + self.tomail,
              Fore.GREEN + '\nObject: ' + Fore.WHITE + self.objectmessage, Fore.GREEN + '\nText: ' + Fore.WHITE + self.text)
        main()


class SMTP_server:
    def __init__(self, name, port, login, pwd, delay):
        self.name = name
        self.port = port
        self.login = login
        self.pwd = pwd
        self.delay = delay

    def check(self):
        print(Fore.LIGHTYELLOW_EX + '\nSMPT Server: ' + Fore.WHITE + self.name, Fore.LIGHTYELLOW_EX + '\nSMTP Server port: ' + Fore.WHITE + str(self.port),
              Fore.LIGHTYELLOW_EX + '\nSMTP Server login: ' + Fore.WHITE + self.login, Fore.LIGHTYELLOW_EX + '\nSMTP Server password: ' + Fore.WHITE + self.pwd + Fore.WHITE)
        return


server = SMTP_server("", 666, "", "", "")
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
 {1}                                                - SCRIPT CREATED BY MITTOD'''.format(Fore.BLUE, Fore.WHITE)

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

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
    

def do_banner():
    banner = random.choice([banner_1, banner_2])
    print(banner)
    time.sleep(1)
    clear()

def getrandomcolor():
    return random.choice([Fore.LIGHTGREEN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTWHITE_EX, Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX])

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
                print(Fore.GREEN, '[', mailnumber, ']',
                      i['email'],  Fore.WHITE)
            else:
                print(Fore.RED, '[', mailnumber, ']',  i['email'],  Fore.WHITE)
            if (mailnumber >= 3) and (len(data['mails']) - mailnumber != 0):
                print(Fore.LIGHTGREEN_EX, 'And', len(
                    data['mails']) - mailnumber, 'more...' + Fore.WHITE)
                break
        f.close()
    else:
        create_db()
        check_emails()
    emailsMenu()


def validate_emails():
    valide = []
    f = open('mail.json')
    data = json.load(f)
    i = 0
    for i in data['mails']:
        if i['wasUsed'] == False:
            valide.append(i)
    return valide


def configCreate():
    if path.exists("config.json"):

        with open("config.json") as f:
            config = json.load(f)
            config['config'].append({"SMTP Adress": 'test', "SMTP Login": 'server.login',
                                    "SMTP Password": 'server.pwd', "SMTP Port": 'server.port'})
    else:
        with open("config.json", "w") as file:
            data = {}
            data['config'] = []
            json.dump(data, file)
        configCreate()


def send(i):
    try:
        smtpObj = smtplib.SMTP_SSL(server.name, server.port)
        smtpObj.ehlo()
        smtpObj.login(server.login, server.pwd)
        smtpObj.sendmail(message.frommail, i['email'], 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (
            message.frommail, i['email'], message.objectmessage, message.text))
        smtpObj.quit()
        print(Fore.GREEN +
              '''[ {0} ] {1} complete!'''.format(0, i['email']) + Fore.WHITE)
    except:
        print(
            Fore.RED + '''[ {0} ] {1} failed!'''.format(1, i['email']) + Fore.WHITE)


def searchdb(t):
    f = open('mail.json')
    data = json.load(f)
    for i in data['mails']:
        if t == i["email"]:
            return True


def send_email():
    flag = int(input('''\n{0}[ 0 ] Send one email\n[ 1 ] Send all possible\n[ 2 ] Send all email in db\n\n{1}Choose function: {2}'''.format(
        Fore.MAGENTA, Fore.CYAN, Fore.WHITE)))
    valide = validate_emails()
    if flag == 0:
        target = input('''{0}Please enter email adress: {1}'''.format(
            Fore.YELLOW, Fore.WHITE))
        if searchdb(target):
            pass
        else:
            print(Fore.RED + "Something went wrong. I don't see that email adress in db." + Fore.RESET)
            ask = input("Do you want add it at db? (yes/no): ")
            if ask.lower() == "yes":
                print('''Adding to db ...'''.format(Fore.GREEN))
                addAddress(target)
            elif ask.lower() == "no":
                pass
        target = {'email': target, 'wasUsed': False}
        send(target)
    elif flag == 1:
        for i in valide:
            send(i)
            time.sleep(server.delay)
    main()




def set_smtp():
    try:
        server.name = input(Fore.GREEN + '\nSet Server name: ' + Fore.WHITE)
        server.port = input(Fore.GREEN + '\nSet Port: ' + Fore.WHITE)
        server.login = input(Fore.GREEN + '\nSet Login: ' + Fore.WHITE)
        server.pwd = input(Fore.GREEN + '\nSet Password: ' + Fore.WHITE)
        #server.delay = int(input(Fore.GREEN + '\nSet Send delay (sec)' + Fore.WHITE))
        main()
    except:
        print(Fore.RED + 'Error!' + Fore.WHITE)
    configCreate()


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
    with open('mail.json', 'w') as f:
        json.dump(data, f, indent=4)


def addAddress(target):
    if path.exists("mail.json"):
        toUpdate = {}
        if target == None:
            address = input('Input address one or more with comma: ')
        else:
            address = target
        address = address.replace(', ', ',')
        addresslist = address.split(',')
        for i in addresslist:
            if i.find('@') != -1:
                toUpdate = {"email": i, "wasUsed": False}
                with open("mail.json") as file:
                    data = json.load(file)
                    newdata = data['mails']
                    if (next((item for item in newdata if item["email"] == i), False)):
                        print(Fore.RED + i + " Already exist!" + Fore.WHITE)
                        continue
                    newdata.append(toUpdate)
                    write_json(data)
            else:
                print(Fore.RED + "ERROR! Please check email: " +
                      Fore.LIGHTRED_EX + i + Fore.WHITE)
    else:
        create_db()
        addAddress(target)
    # main()


def converter():
    pathfile = input("Enter path to txt file: ")
    if path.exists(pathfile):
        with open(pathfile, 'r') as file:
            f = file.read()
            f = f.split('\n')
            for x in f:
                target = x.split(':')[0]
                addAddress(target)
    else:
        clear()
        time.sleep(0.1)
        print(Fore.RED+"Wrong path to file" + Fore.RESET)
        converter()
    main()


def emailsMenu():
    
    print(getrandomcolor() + '''███████╗      ███╗   ███╗ █████╗ ██╗██╗     ███████╗    ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
██╔════╝      ████╗ ████║██╔══██╗██║██║     ██╔════╝    ████╗ ████║██╔════╝████╗  ██║██║   ██║
█████╗  █████╗██╔████╔██║███████║██║██║     ███████╗    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
██╔══╝  ╚════╝██║╚██╔╝██║██╔══██║██║██║     ╚════██║    ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
███████╗      ██║ ╚═╝ ██║██║  ██║██║███████╗███████║    ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
╚══════╝      ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                              ''' + Fore.RESET)
    print(Fore.GREEN +
          '''\n[0] Check e-mails in db\n[1] Send e-mails\n[2] Set e-mail settings\n\n[69] Quit\n[99] Clear \n[88] Back to main menu''' + Fore.RESET)
    try:
        function = int(input(Fore.CYAN + "\nChoose function: " + Fore.RESET))
    except:
        print(Fore.RED + "It's not a nunber!" + Fore.RESET)
    if function == 0:
        check_emails()
    elif function == 1:
        send_email()
    elif function == 2:
        set_email()
    elif function == 69:
        quit()
    elif function == 99:
        clear()
        emailsMenu()
    elif function == 88:
        clear()
        main()
    else:
        clear()
        print(Fore.RED + "Sorry, i don't know that function")
        emailsMenu()


def smtpMenu():
    
    print(getrandomcolor() + '''███████╗███╗   ███╗████████╗██████╗     ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
██╔════╝████╗ ████║╚══██╔══╝██╔══██╗    ████╗ ████║██╔════╝████╗  ██║██║   ██║
███████╗██╔████╔██║   ██║   ██████╔╝    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
╚════██║██║╚██╔╝██║   ██║   ██╔═══╝     ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
███████║██║ ╚═╝ ██║   ██║   ██║         ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
╚══════╝╚═╝     ╚═╝   ╚═╝   ╚═╝         ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                              '''+ Fore.RESET)
    server.check()
    print(Fore.GREEN + '''\n[0] Check SMTP settings\n[1] Set SMTP settings\n\n[69] Quit\n[99] Clear \n[88] Back to main menu''')
    try:
        function = int(input(Fore.CYAN + "\nChoose function: " + Fore.RESET))
    except:
        print(Fore.RED + "It's not a number!" + Fore.RESET)
    if function == 0:
        server.check()
    elif function == 1:
        set_smtp()
    elif function == 69:
        quit()
    elif function == 99:
        clear()
        smtpMenu()
    elif function == 88:
        clear()
        main()
    else:
        system('clear')
        print(Fore.RED + "Sorry, i dont't know that function" + Fore.RESET)
        smtpMenu()

def dbMenu():
    
    print(getrandomcolor() + '''██████╗ ██████╗     ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
██╔══██╗██╔══██╗    ████╗ ████║██╔════╝████╗  ██║██║   ██║
██║  ██║██████╔╝    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
██║  ██║██╔══██╗    ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
██████╔╝██████╔╝    ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
╚═════╝ ╚═════╝     ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
                                                          ''' + Fore.RESET)
    print(Fore.YELLOW + '''\n[0] Add adress into DB\n[1] Add adresses from file\n\n[69] Quit\n[99] Clear \n[88] Back to main menu''')
    try:
        function = int(input(Fore.CYAN + "\nChoose function: " + Fore.RESET))
    except:
        print(Fore.RED + "It's not a number!" + Fore.RESET)
    if function == 0:
        addAddress(None)
    elif function == 1:
        converter()
    elif function == 69:
        quit()
    elif function == 99:
        clear()
        dbMenu()
    elif function == 88:
        clear()
        main()
    else:
        clear()
        print(Fore.RED + "Sorry, i don't know that function" + Fore.RESET)
        dbMenu()


def help():
    clear()
    print(getrandomcolor() + '''██╗  ██╗███████╗██╗     ██████╗ 
██║  ██║██╔════╝██║     ██╔══██╗
███████║█████╗  ██║     ██████╔╝
██╔══██║██╔══╝  ██║     ██╔═══╝ 
██║  ██║███████╗███████╗██║     
╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     
                                ''' + Fore.RESET)
    print(Fore.LIGHTMAGENTA_EX + "Note: " + Fore.LIGHTYELLOW_EX +"Сначала добавьте адреса электронных почт в базу данных в меню Базы Данных.\nЗатем установите подключение к SMTP серверу в меню SMTP.\nВ меню E-mail задайте данные для рассылки\nProfit!" + Fore.RESET)

    input(getrandomcolor() + "\n\nPress Enter to continue..." + Fore.RESET)
    clear()
    main()



def settingsMenu():
    print()

def main():
    print(getrandomcolor() + '''███╗   ███╗ █████╗ ██╗███╗   ██╗    ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
████╗ ████║██╔══██╗██║████╗  ██║    ████╗ ████║██╔════╝████╗  ██║██║   ██║
██╔████╔██║███████║██║██╔██╗ ██║    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
██║╚██╔╝██║██╔══██║██║██║╚██╗██║    ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
██║ ╚═╝ ██║██║  ██║██║██║ ╚████║    ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                          ''' + Fore.RESET)
    screen1 = print(Fore.LIGHTBLUE_EX + '''\n[0] e-mails menu\n[1] SMTP menu\n[2] DB\n[3] Settings\n\n[69] Quit\n[99] Clear''' + Fore.RESET)
    try:
        target = int(input(Fore.CYAN + "\nChoose function: " + Fore.RESET))
    except:
        print(Fore.RED+"It's not a number!" + Fore.RESET)
        time.sleep(0.5)
        clear()
        main()
    if target == 0:
        # E-MAILS MENU
        system('clear')
        emailsMenu()
    elif target == 1:
        # SMTP MENU
        system('clear')
        smtpMenu()
    elif target == 2:
        # DB MENU
        system('clear')
        dbMenu()
    elif target == 69:
        quit()
    elif target == 99:
        clear()
        main()
    elif target == 101:
        help()
    else:
        clear()
        print(Fore.RED + "Function is undefinded, please try again" + Fore.RESET)
        main()

main()
