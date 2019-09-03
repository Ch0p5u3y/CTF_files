#! /usr/bin/env python

val = 0
for x in range(70055, 78055): #loop through the specified values, incremented until we found our desired value
    val = ((x << 2) + x)*2 #recreate the calculation from the binary
    if val == 705170: #compare to the binary's hardcoded value and print whether it is correct or not
        print "[$$$] - Desired result %d ---> %d found!" % (x, val)
        break
    else:
        print "[X] - %d ---> %d incorrect number!" % (x, val)
        pass
print "\nExiting script!"
