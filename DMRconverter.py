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

print "DMR Radio ID to IP Address and Radio ID to IP Address Converter"
print "  enter a radio ID or IP address to convert, or a"
print "  the enter/return key to quit"

while True:
    input = raw_input("Radio ID or IP Address to Convert? ")
    if not input:
        sys.exit()

    if '.' in input:
        id = ip_to_id(input)
        print ""
        print "Radio ID is:", id 
        print ""
    elif (int(input) < 16777216):
        ip = id_to_ip(int(input))
        radio_ip = '12.' + ip
        pc_ip = '13.' + ip
        print ""
        print "Radio IP adddress:       ", radio_ip
        print "Attached PC IP address:  ", pc_ip
        print ""
    else:
        print ""
        print "Something went wrong..."
        print ""
    
