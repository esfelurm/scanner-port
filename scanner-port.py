import sys, platform
import socket
import time
import threading
import requests
from queue import Queue
gn = '\033[00;32m'
rd = '\033[00;31m'
yw = '\033[00;33m'
Lgn = '\033[01;32m'
be = '\033[00;34m'
we = '\033[01;37m'

banner = f"""{yw}
------------------------------------------------------------

{gn}@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@&BPY??????J5G#@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@BY~:.:^!.   !!^..:!Y#@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@&5^ .75B&@#. . 7@@&B5!. ~P@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@P: ~P&@@@@&^ !#: 7@@@@@&5: ^G@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@? .5@@@@@@&~ ^&@G  J@@@@@@@Y  J@@@@@@@@@@@@@@
{we}@@@@@@@@@@@@@@7 :B@@@@@@@! :#@@@5  Y@@@@@@@G  J@@@@@@@@@@@@@
@@@@@@@@@@@@@5  G@@@@@@@? .B@@@@@J  P@@@@@@@5  B@@@@@@@@@@@@
@@@@@@@@@@@@@! :PPPPPPP?  ~PPPPPPP: .5PPPPPP5. ?@@@@@@@@@@@@
@@@@@@@@@@@@@~ .::::::   :^:::::::^.  .::::::  ?@@@@@@@@@@@@
@@@@@@@@@@@@@? :&@@@@P  !@@@@@@@@@@B. :#@@@@B  Y@@@@@@@@@@@@
@@@@@@@@@@@@@B. ?@@@B. ^&@@@@@@@@@@@P  ~&@@@! :&@@@@@@@@@@@@
@@@@@@@@@@@@@@P  J@#: .#@@@@@@@@@@@@@J  !@@7 .B@@@@@@@@@@@@@
{rd}@@@@@@@@@@@@@@@G: ~^ .G@@@@@@@@@@@@@@@7  !^ ~#@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@&J.  ^&@@@@@@@@@@@@@@@B.  :5@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@&5!..^?5G##&&##BPY7^.:!P@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@#P?~:...::...:^!JG&@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@&#BBBBB#&@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
{yw}------------------------------------------------------------
"""
for c in banner:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.005)

print ("")
print ("")
print ("")

IP = requests.get('https://get.geojs.io/v1/ip.json')
myip = IP.json()['ip']
print(f"{rd}[*]{yw} You ip : {gn}"+myip)

print(f'{rd}[*]{yw} version  :{gn}', platform.version())
socket.setdefaulttimeout(0.25)
lock = threading.Lock()
print (f"{be}____________________________________")
time.sleep(4)
print (f"""
{rd}[-]{yw} Creator channel Telegram: {Lgn}@esfelurm
{rd}[!]{yw}To use, please enter https and http! 
Example : {gn} Telegram.com
{rd}[!] Communication is TCP! 
""")
print ("")
time.sleep(2)
ip_address = input(f"{rd} ┌─["+f"{Lgn}@esfelurm"+f"{be}/"+f"{we}port-scanner"+f"""{rd}]
 └──╼ """+f"{gn}Enter the site address : >>>{yw} ")
print ("")
time.sleep(1)
host = socket.gethostbyname(ip_address)
print (f'{rd}[+]{yw} IP Address : {gn}', host)
print (f"{be}____________________________________")
def scanner(port):
   tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      Connect = tcpsocket.connect((host, port))
          
      with lock:
         time.sleep(2)
         print(f'{rd}[!]{yw} Port :{Lgn}', port, f'{yw} is open! ')

         print(f"{be}____________________________________")
      Connect.close()
   except:
      pass

def execute():
   while True:
      worker = queue.get()
      scanner(worker)
      queue.task_done()
      
queue = Queue()
start_time = time.time()
   
for x in range(100):
   thread = threading.Thread(target = execute)
   thread.daemon = True
   thread.start()
   
for worker in range(1, 500):
   queue.put(worker)
   
queue.join()

print (f"{rd}[*]{gn} channel Telegram : {Lgn} https://t.me/esfelurm")
