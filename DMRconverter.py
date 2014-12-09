#!/usr/bin/env python
#
# Copyright (c) 2014, N0MJS and the K0USY Group.
#
# This work is licensed under the Creative Commons Attribution-ShareAlike
# 3.0 Unported License.To view a copy of this license, visit
# http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to
# Creative Commons, 444 Castro Street, Suite 900, Mountain View,
# California, 94041, USA.


import re
import sys
import socket

def id_to_ip (_id):
    _ip = list(re.findall('..', hex(_id)[2:].rjust(6,'0')))
    for i, octet in enumerate(_ip):
        _ip[i] = str(int(octet, 16))
    _ip = _ip[0] + '.' + _ip[1] + '.' + _ip[2]
    return _ip
    
def ip_to_id (_ip):
    _id = list(int(octet) for octet in _ip.split('.'))
    _id.pop(0)
    _id = int(''.join(["%02X" % long(octet) for octet in _id]), 16)
    return _id

def convert(_item):

    try:
        if (int(_item) < 16777216): 
            ip = id_to_ip(int(_item))
            radio_ip = '12.' + ip
            pc_ip = '13.' + ip
            print "Radio ID:                ", _item
            print "Radio IP adddress:       ", radio_ip
            print "PC IP address:           ", pc_ip
            print ""
        else:
            print "Not a valid radio ID or IP address:  ", _item
            print ""
    except ValueError:
        try:
            socket.inet_aton(_item)
            id = ip_to_id(_item)
            print "IP addresss:             ", _item
            print "Radio ID is:             ", id 
            print ""
        except socket.error:
            print "Not a valid radio ID or IP address:  ", _item
            print ""

print ""

if len(sys.argv) > 1:
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print "usage: DMRconverter.py [radio id | ip address | (nothing)]..."
        print ""
        print "     (nothing) results in an interactive seesion"
        print "     CAI network ID is assumed to be 12"
        print ""
    else:
        for item in sys.argv[1:]:
            convert(item)
else:
    print "  enter a radio ID or IP address to convert, or a"
    print "  the enter/return key to quit"
    print ""
    while True:
        item = raw_input("Radio ID or IP Address to Convert? ").split(' ')
        print ""
        if not item:
            sys.exit()
        for id in item:
            convert(id)
    






    
