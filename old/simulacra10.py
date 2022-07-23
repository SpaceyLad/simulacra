#!/usr/bin/env python3

#Written and developed by Stian Kvålshagen

import sys
import argparse

#Import data needed
parser = argparse.ArgumentParser()
parser.add_argument("-c","--complex",help="Adjust what level of complexity the usernames will be.\nNote that increasing complexity will increase size a lot!\nAdjust the settings in code if needed.",required=True,type=int)
parser.add_argument("-f","--firstname",help="The persons firstname",required=True,type=str)
parser.add_argument("-l","--lastname",help="The persons lastname",required=True,type=str)
parser.add_argument("-p","--printer",help="Print result",required=False,action=argparse.BooleanOptionalAction)
args = parser.parse_args()

fName = args.firstname
lName = args.lastname
comp = args.complex
printCheck = args.printer

print("Generating wordlist for: " + fName + " " + lName)

usernames = []

#Add special characters here if needed! This will be applied in complexity level 2.
special = [".","-","_"]

#You can add more numbers here to expand complexity 3.
commonNumbers = ["1","2","3","4","5","6","7","8","9","12","123"]

#1st(First letter from lastname + name & vise versa)
usernames.append(lName[0].lower() + fName.lower())
usernames.append(fName[0].lower() + lName.lower())
if comp >= 2:
 tmp = []
 for x in special:
  usernames.append(lName[0].lower() + x + fName.lower())
  usernames.append(fName[0].lower() + x + lName.lower())
if comp == 3:
 for x in commonNumbers:
  usernames.append(lName[0].lower() + fName.lower() + x)
  usernames.append(fName[0].lower() + lName.lower() + x)

#2nd(pure names)
usernames.append(fName.lower())
usernames.append(lName.lower())
if comp == 3:
 for x in commonNumbers:
  usernames.append(fName.lower() + x)
  usernames.append(lName.lower() + x)

#3rd(name and 3 letters last name)
usernames.append(fName.lower() + lName[0].lower() + lName[1].lower() + lName[2].lower())
if comp >= 2:
 for x in special:
  usernames.append(fName.lower() + x + lName[0].lower() + lName[1].lower() + lName[2].lower())
if comp == 3:
 for x in commonNumbers:
  usernames.append(fName.lower() + lName[0].lower() + lName[1].lower() + lName[2].lower() + x)

#4th(3 letters name and 3 letters lastname)
usernames.append(fName[0].lower() + fName[1].lower() + fName[2].lower() + lName[0].lower() + lName[1].lower() + lName[2].lower())
if comp >= 2:
 for x in special:
  usernames.append(fName[0].lower() + fName[1].lower() + fName[2].lower() + x + lName[0].lower() + lName[1].lower() + lName[2].lower())
if comp == 3:
 for x in commonNumbers:
  usernames.append(fName[0].lower() + fName[1].lower() + fName[2].lower() + lName[0].lower() + lName[1].lower() + lName[2].lower() + x)

#5th(3 letters lastname and 3 letters name)
usernames.append(lName[0].lower() + lName[1].lower() + lName[2].lower() + fName[0].lower() + fName[1].lower() + fName[2].lower())
if comp >= 2:
 for x in special:
  usernames.append(lName[0].lower() + lName[1].lower() + lName[2].lower() + x + fName[0].lower() + fName[1].lower() + fName[2].lower())
if comp == 3:
 for x in commonNumbers:
  usernames.append(lName[0].lower() + lName[1].lower() + lName[2].lower() + fName[0].lower() + fName[1].lower() + fName[2].lower() + x)

#6th(name and lastname)
usernames.append(fName.lower() + lName.lower())
usernames.append(lName.lower() + fName.lower())
if comp >= 2:
 for x in special:
  usernames.append(fName.lower() + x + lName.lower())
  usernames.append(lName.lower() + x + fName.lower())
if comp == 3:
 for x in commonNumbers:
  usernames.append(fName.lower() + lName.lower() + x)
  usernames.append(lName.lower() + fName.lower() + x)

#Complexity 4
holder = []
if comp >= 4:
 for x in usernames:  
  for y in commonNumbers:
   holder.append(x + y)
 usernames = holder

#Print
if printCheck is True:
 for x in usernames:
  print (x)

c = 0

ready = False
while not ready:
 try:
  file = open(fName.lower() + "_" + str(c) + ".txt","x")
  print(fName.lower() + "_" + str(c) + ".txt created.")
  ready = True
 except:
  print(fName.lower() + "_" + str(c) + ".txt allready exists..")
  c = c + 1

for x in usernames:
 file.write(x + "\n")
