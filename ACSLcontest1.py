#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Michael Huang
Phillips Academy, Andover
Senior-3
@author: Michael Huang
"""
import time
import random
def genPrime(start, end):
    """
    this function generate primes that are bigger than start and 1 more prime bigger than end
    """
    global length
    global primes
    for i in range(start+2,2147483647,2):
        isPrime=True
        s=i**0.5
        for j in primes:
            if(i%j==0):
                isPrime=False
                break
            if(j>s):
                break
        if isPrime:
            primes.append(i)
            length+=1
            if i>end:
                return
def guessPrime(prime,i):
    global length
    global primes
    guess=i+(prime-primes[i])//2
    if(guess>=length):
        guess=length-1
    if(guess<0):
        guess=0
    return guess
def findPrime(prime):
    global index
    global length
    global primes
    guess=guessPrime(prime,index)
    if primes[guess]==prime:
        return guess
    if primes[guess]<prime:
        left=guess
        right=guessPrime(prime,guess)
    else:
        right=guess
        left=guessPrime(prime,guess)
    if primes[right]==prime:
        return right
    if primes[left]==prime:
        return left
    middle=(right+left)//2
    while primes[middle]!=prime:
        while middle!=right and middle!=left and primes[middle]!=prime:
            if primes[middle]<prime:
                left=middle
            elif primes[middle]>prime:
                right=middle
            else:
                return middle
            middle=(left+right)//2
        left=0
        right=length-1
    return middle
def nextPrime(lastPrime):
    global index
    global length
    global primes
    if(primes[-2]>=lastPrime):
        if primes[index]==lastPrime:
            index+=1
            try:
                return primes[index]
            except:
                return primes[-1]
        else:
            index=findPrime(lastPrime)+1
            try:
                return primes[index]
            except:
                return primes[-1]
    else:
        genPrime(primes[-1],lastPrime)
        index=length-1
        try:
            return primes[index]
        except:
            return primes[-1]
def fermatTest(n):
    for i in range (0,20):
        r=random.randint(2,n-2)
        if pow(r,n-1,n)!=1:
            return False
    return True
def numPrime(n):
    if(n<2):
        return
    global locatedPrimes
    prime=2
    count=0
    tested=False
    while prime<n**0.5+1:
        if((not tested) and count>10000 and count>n**0.3):
            if(fermatTest(n)):
                return 1
            else:
                tested=True
        if(n%prime==0):
            locatedPrimes.add(prime)
            numPrime(n//prime)
            return
        prime=nextPrime(prime)
        count+=1
    locatedPrimes.add(n)
    return

primes=[2,3]
locatedPrimes=set([])
index=0
length=2
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
startT=time.time()
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
    locatedPrimes.clear()
print(time.time()-startT)



