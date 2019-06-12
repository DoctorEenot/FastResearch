import socket
from PIL import Image, ImageGrab
import pyautogui
import time

def SimpleScan(host,FileName):
    '''
    Scan based on ports of curent host
    Example: you have host with huge count of open ports
    and that`s simple scan for that state
    '''
    print('starting checking host: '+host)
    try:
        file = open(FileName,'r')
    except:
        raise Exception('File '+FileName+' doesn`t exist, bitch')
        return
    data = file.readline()
    NotWeb = []
    while data:
        sock = socket.socket()
        sock.settimeout(0.4)
        data = list(data)
        data.remove('\n')
        port = ''
        for i in range(len(data)):
            port = port+data[i]
        print(port)
        payload = 'GET / HTTP/1.1\r\nHost: '+host+':'+port+'\r\nUser-Agent: Say10\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nCookie: _ga=GAKillYourself; _gid=GAForTheNameOfSay10\r\nUpgrade-Insecure-Requests: 1\r\nCache-Control: max-age=10000000\r\n\r\n'
        payload = bytes(payload,'utf-8')
        port_ = int(port)
        try:
            sock.connect((host,port_))
            sock.send(payload)
            req = sock.recv(1024)
        except:
            req = 'MNWasdkju1983uskjn'
            NotWeb.append(port)
        if req != 'MNWasdkju1983uskjn':
            out = open(port+'.txt','w')
            out.write(str(req))
            out.close()
        sock.close()
        data = file.readline()
    ans = input('Continue checking (y/n)')
    if ans == 'N' or ans == 'n':
        return
    print('Checking web ended,starting checking another ports: '+str(len(NotWeb)))
    for i in range(len(NotWeb)):
        port = NotWeb[i]
        print(port)
        try:
            sock.connect((host,port))
            req = sock.recv(1024)
        except:
            req = 'MNWasdkju1983uskjn'
        
        if req != 'MNWasdkju1983uskjn':
            out = open(str(port)+'(NW)'+'.txt','w')
            out.write(str(req))
            out.close()
        sock.close()


def WebScan(FileName,Browser):
    '''
    Scan based on web browser, just to see content of the site
    FileName : Name of file with hosts
    Browser : (x,y,x1,y1) where x,y,x1,y1 window, which you want to be screenshoted
    It works good with firefox on default settings
    '''
    try:
        file = open(FileName,'r')
    except:
        raise Exception('File '+FileName+' doesn`t exist, bitch')
        return
    host = file.readline()
    i = 0
    while host:
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('l')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('l')
        pyautogui.press('backspace')
        pyautogui.typewrite(host)
        pyautogui.press('enter')
        time.sleep(5)
        screen = ImageGrab.grab(Browser)
        screen.save(str(i)+'.jpg')
        i = i + 1
        host = file.readline()
    file.close()
