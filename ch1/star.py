#!/usr/bin/env python
for i in range(0,3):
    for j in range(2, i, -1):
        if(j>i):
             print(" ",end=" ")
    for k in range(0, i+1):
        if(k<=i):
            print("*",end=" ")
    for l in range(0, i+1):
        if(l<i):
            print("*",end=" ")
    print("\n")

for i in range(2, -1, -1):
    for j in range(2, i-1, -1):
        if(j>i-1):
            print(" ",end=" ")
    for k in range(0, i):
        if(k<i):
            print("*",end=" ")
    for l in range(0, k+1):
        if(l<k):
            print("*")
    print("\n")
