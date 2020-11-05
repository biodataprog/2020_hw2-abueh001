#!/usr/bin/env python3

start = 0
end   = 99
divisor=7
print("Printing out numbers from",start,"to",end, " not divisible by",divisor)

while (start != end+1):
    if (start%divisor != 0): 
        print(start)
    start += 1
