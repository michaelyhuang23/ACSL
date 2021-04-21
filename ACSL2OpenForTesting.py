#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 14:52:07 2020
Michael Huang
Phillips Academy, Andover
Senior-3

@author: michaelhyh
"""
import sys
import random
import time
sys.setrecursionlimit(10000000)

characterPos2={}
identifiedCS2={}

def longestSubstring(string1, string2):
        longestLen=0
        startIndex1=0
        endIndex1=0
        startIndex2=0
        endIndex2=0
        headOfLongest=""
        for i,character in enumerate(string1):
            try:
                for index in characterPos2[character]:
                    if index in identifiedCS2.keys() and i in identifiedCS2[index]:
                        continue
                    j=1
                    try:
                        identifiedCS2[index].append(i)
                    except:
                        identifiedCS2[index]=[i]
                    while(index+j<len(string2) and i+j<len(string1) and string2[index+j]==string1[i+j]):
                        try:
                            identifiedCS2[index+j].append(i+j)
                        except:
                            identifiedCS2[index+j]=[i+j] 
                        j+=1
                    
                    if j>longestLen or (j==longestLen and (string1[i:i+j]<headOfLongest)):
                        headOfLongest=string1[i:i+j]
                        longestLen=j
                        startIndex2=index
                        endIndex2=index+j-1
                        startIndex1=i
                        endIndex1=i+j-1
                    elif string1[i:i+j]==headOfLongest:
                        if i<startIndex1:
                            startIndex1=i
                            endIndex1=i+j-1
                        if index<startIndex2:
                            startIndex2=index
                            endIndex2=index+j-1
            except:
                continue
        return [startIndex1,endIndex1,startIndex2,endIndex2,longestLen]
def limitedLongestSubstring(times,startIndex1,endIndex1,startIndex2,endIndex2):
        if startIndex1>endIndex1 or startIndex2>endIndex2:
            return 0
        newstartIndex1=startIndex1
        newendIndex1=endIndex1
        newstartIndex2=startIndex2
        newendIndex2=endIndex2
        longestLen=0
        headOfLongest=""
        for i2 in range(startIndex2,endIndex2+1):
            if i2 not in identifiedCS2:
                continue
            for index1 in identifiedCS2[i2]:
                if index1>endIndex1 or index1<startIndex1:
                    continue
                j=0
                while (i2+j in identifiedCS2 and index1+j in identifiedCS2[i2+j]):
                    if i2+j<startIndex2 or i2+j>endIndex2 or index1+j<startIndex1 or index1+j>endIndex1:
                        break
                    j+=1
                if j>longestLen or (j==longestLen and (strings1[times][index1:index1+j]<headOfLongest)):
                    longestLen=j
                    headOfLongest=strings1[times][index1:index1+j]
                    newstartIndex1=index1
                    newendIndex1=index1+j-1
                    newstartIndex2=i2
                    newendIndex2=i2+j-1
                elif strings1[times][index1:index1+j]==headOfLongest:
                    if index1<newstartIndex1:
                        newstartIndex1=index1
                        newendIndex1=index1+j-1
                    if i2<newstartIndex2:
                        newstartIndex2=i2
                        newendIndex2=i2+j-1
        return longestLen+limitedLongestSubstring(times,startIndex1,newstartIndex1-1,startIndex2,newstartIndex2-1)+limitedLongestSubstring(times,newendIndex1+1,endIndex1,newendIndex2+1,endIndex2)


input1=["","","","",""]
input2=["","","","",""]
strings1=["","","","",""]
strings2=["","","","",""]
for i in range(0,5):
    for j in range(0,2000):
        input1[i]+=str(chr(random.randrange(ord("A"),ord("Z")+1))).upper()
        input2[i]+=str(chr(random.randrange(ord("A"),ord("Z")+1))).upper()
    print(input1[i] + " and "+input2[i])
startT=time.time()
print("start")
ans=[]
for times in range(0,5):
    for i,character in enumerate(input1[times]):
        if not character.isalpha():
            continue
        strings1[times]+=character
    for i,character in enumerate(input2[times]):
        if not character.isalpha():
            continue
        strings2[times]+=character
        try:
            characterPos2[character].append(len(strings2[times])-1)
        except:
            characterPos2[character]=[len(strings2[times])-1]  
    info=longestSubstring(strings1[times], strings2[times])
    print("times "+str(times)+" phase 1 finished")
    for key in identifiedCS2.keys():
        identifiedCS2[key]=frozenset(identifiedCS2[key])
    
    ans.append(info[4]+limitedLongestSubstring(times,0,info[0]-1, 0, info[2]-1)+limitedLongestSubstring(times,info[1]+1,len(strings1[times])-1, info[3]+1, len(strings2[times])-1))
    characterPos2={}
    identifiedCS2={}
print("\n")
for i in range(0,5):
    try:
        print("number "+str(i+1)+" has ADF: "+str(ans[i]))
    except:
        print("number "+str(i+1)+" has ADF: 1")
print("runtime for strings each of a size of 2000 characters: "+str(time.time()-startT))