# -*- coding: utf-8 -*-
#! /usr/bin/env python

#create a txt file with a list of passwords inside, will need to use nested for loops to append every possible combination of 2 extra letters onto the password
#open a file write each combination line by line

wordlist = open("list.txt", 'w')
pw = "s1lKy"
char = "\/.,><;:!£$%^&*()-_=+][{}#~@1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
line = ''

for i in char:
    for j in char:
        line += pw
        line += i
        line += j
        line += '\n'
        wordlist.write(line)
        line = ''
