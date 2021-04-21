#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Michael Huang
Phillips Academy, Andover
Senior-3
@author: Michael Huang
"""



locatedPrimes=set([])
def numPrime(n):
    global locatedPrimes
    if n<2:
        return
    if n%2==0:
        locatedPrimes.add(2)
        numPrime(n//2)
        return
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            locatedPrimes.add(i)
            numPrime(n//i)
            return
    locatedPrimes.add(n)
    return

strs=[]
N_str=[]
Ns=[]
Ps=[]
print("\nEnter values below (in this format: \"N P\"):")
for i in range(0,5):
    strs.append(input().split(" "))

    N_str.append(strs[i][0])
    Ns.append(int(N_str[i]))
    for j in range (1,10):
        try:
            Ps.append(len(N_str[i])-int(strs[i][j]))
            break
        except:
            continue

for j in range(0,5):
    P=Ps[j]
    N_arr=[]
    N=Ns[j]
    for i in N_str[j]:
        N_arr.append(int(i))
    try:
        valP=N_arr[P]
    except:
        if P<0:
            P=0
        else:
            P=len(N_arr)-1
        valP=N_arr[P]
    string = ""
    numPrime(N)
    for i,item in enumerate(N_arr):
        if(i>P):
            string+=str(abs(item-valP))
        elif(i<P):
            string+=str(item+valP)
        else:
            string+=str(len(locatedPrimes))
    print("\n\n"+str(j+1)+" : "+string+"\n")
    locatedPrimes=set([])




