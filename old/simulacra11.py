#!/usr/bin/env python3

# Written and developed by Stian Kvålshagen

import sys
import argparse
import colorama
from colorama import Fore,Style

# Filters
special = [".","-","_"]
commonNumbers = ["1","2","3","4","5","6","7","8","9","12","123"]

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument("-c","--complex",help="Adjust what level of complexity the usernames will be.\nNote that increasing complexity will increase size a lot!\nAdjust the settings in code if needed.",type=int)
parser.add_argument("-d","--domain",help="Print with mail domain. Example: outlook.com",type=str)
parser.add_argument("-e","--easy",help="Easy mode! Just follow the text. (For non techinal people.)",action="store_true")
parser.add_argument("-F","--firstname",help="The first name",type=str)
parser.add_argument("-L","--lastname",help="The last name",type=str)
parser.add_argument("-M","--middlename",help="The middle name",type=str)
parser.add_argument("-p","--printer",help="Print result",action=argparse.BooleanOptionalAction)
args = parser.parse_args()
fName = args.firstname
lName = args.lastname
mName = args.middlename
comp = args.complex
printCheck = args.printer
domain = args.domain

# Easy mode
if args.easy:
 fName = input(Fore.CYAN + "What is the first name?\n" + Style.RESET_ALL)
 mN = input(Fore.CYAN + "Does the person have a middle name that you want to use? [y/n]\n" + Style.RESET_ALL)
 if mN == "y":
  mName = input(Fore.CYAN + "What is the middle name?\n" + Style.RESET_ALL)
  args.middlename = True
 lName = input(Fore.CYAN + "What is the last name?\n" + Style.RESET_ALL)
 domainCheck = input(Fore.CYAN + "Do you want to use a domain? [y/n]\n" + Style.RESET_ALL)
 if domainCheck == "y":
  domain = input(Fore.CYAN + "What is the full domain? Ex: gmail.com\n" + Style.RESET_ALL)
  args.domain = True
 compIn = input(Fore.CYAN + "Please choose complexity level: 1 - 4\n" + Style.RESET_ALL)
 comp = int(compIn)

if not args.middlename:
 print(Fore.GREEN + "Generating wordlist for: " + fName + " " + lName + Style.RESET_ALL)
if args.middlename:
 print(Fore.GREEN + "Generating wordlist for: " + fName + " " + mName + " " + lName + Style.RESET_ALL)
usernames = []

# 1. First letter from lastname + name & vise versa
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

# 2. pure names
usernames.append(fName.lower())
usernames.append(lName.lower())
if comp == 3:
 for x in commonNumbers:
  usernames.append(fName.lower() + x)
  usernames.append(lName.lower() + x)

# 3. name & 3 letters last name
usernames.append(fName.lower() + lName[0].lower() + lName[1].lower() + lName[2].lower())
if comp >= 2:
 for x in special:
  usernames.append(fName.lower() + x + lName[0].lower() + lName[1].lower() + lName[2].lower())
if comp == 3:
 for x in commonNumbers:
  usernames.append(fName.lower() + lName[0].lower() + lName[1].lower() + lName[2].lower() + x)

# 4. 3 letters first name & 3 letters lastname
usernames.append(fName[0].lower() + fName[1].lower() + fName[2].lower() + lName[0].lower() + lName[1].lower() + lName[2].lower())
if comp >= 2:
 for x in special:
  usernames.append(fName[0].lower() + fName[1].lower() + fName[2].lower() + x + lName[0].lower() + lName[1].lower() + lName[2].lower())
if comp == 3:
 for x in commonNumbers:
  usernames.append(fName[0].lower() + fName[1].lower() + fName[2].lower() + lName[0].lower() + lName[1].lower() + lName[2].lower() + x)

# 5. name and lastname
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

# Middle name
if args.middlename:
# 1 First letter from lastname & first name & vise versa including middle name)
 usernames.append(lName[0].lower() + mName[0].lower() + fName.lower())
 usernames.append(fName[0].lower() + mName[0].lower() + lName.lower())
 usernames.append(lName[0].lower() + mName.lower() + fName.lower())
 usernames.append(fName[0].lower() + mName.lower() + lName.lower())
 if comp >= 2:
  for x in special:
   usernames.append(lName[0].lower() + mName[0].lower() + x + fName.lower())
   usernames.append(fName[0].lower() + mName[0].lower() + x + lName.lower())
   usernames.append(lName[0].lower() + mName.lower() + x + fName.lower())
   usernames.append(fName[0].lower() + mName.lower() + x + lName.lower())
   usernames.append(lName[0].lower() + x + mName[0].lower() + fName.lower())
   usernames.append(fName[0].lower() + x + mName[0].lower() + lName.lower())
   usernames.append(lName[0].lower() + x + mName.lower() + fName.lower())
   usernames.append(fName[0].lower() + x + mName.lower() + lName.lower())
 if comp == 3:
  for x in commonNumbers:
   usernames.append(lName[0].lower() + mName[0].lower() + fName.lower() + x)
   usernames.append(fName[0].lower() + mName[0].lower() + lName.lower() + x)
   usernames.append(lName.lower() + mName[0].lower() + fName.lower() + x)
   usernames.append(fName.lower() + mName[0].lower() + lName.lower() + x)
# 2. middle name
 usernames.append(mName.lower())
 if comp == 3:
  for x in commonNumbers:
   usernames.append(mName.lower() + x)
# 3. name & 1 letter middle name & 3 letters last name
 usernames.append(fName.lower() + mName[0].lower() + lName[0].lower() + lName[1].lower() + lName[2].lower())
 if comp >= 2:
  for x in special:
   usernames.append(fName.lower() + mName[0].lower() + x + lName[0].lower() + lName[1].lower() + lName[2].lower())
   usernames.append(fName.lower() + mName.lower() + x + lName[0].lower() + lName[1].lower() + lName[2].lower())
   usernames.append(fName.lower() + x + mName[0].lower() +  lName[0].lower() + lName[1].lower() + lName[2].lower())
   usernames.append(fName.lower() + x + mName.lower() + lName[0].lower() + lName[1].lower() + lName[2].lower())
   usernames.append(fName.lower() + x + mName[0].lower() + x + lName[0].lower() + lName[1].lower() + lName[2].lower())
   usernames.append(fName.lower() + x + mName.lower() + x + lName[0].lower() + lName[1].lower() + lName[2].lower())
  if comp == 3:
   for x in commonNumbers:
    usernames.append(fName.lower() + mName[0].lower() + lName[0].lower() + lName[1].lower() + lName[2].lower() + x)
    usernames.append(fName.lower() + mName.lower() + lName[0].lower() + lName[1].lower() + lName[2].lower() + x)
# 4. 3 letters first name & 3 letters middle name &  3 letters last name
 usernames.append(fName[0].lower() + fName[1].lower() + fName[2].lower() + mName[0].lower() + mName[1].lower() + mName[2].lower() + lName[0].lower() + lName[1].lower() + lName[2].lower())
 if comp >= 2:
  for x in special:
   usernames.append(fName[0].lower() + fName[1].lower() + fName[2].lower() + mName[0].lower() + mName[1].lower() + mName[2].lower() + x +  lName[0].lower() + lName[1].lower() + lName[2].lower())
   usernames.append(fName[0].lower() + fName[1].lower() + fName[2].lower() + x + mName[0].lower() + mName[1].lower() + mName[2].lower() + lName[0].lower() + lName[1].lower() + lName[2].lower())
   usernames.append(fName[0].lower() + fName[1].lower() + fName[2].lower() + x + mName[0].lower() + mName[1].lower() + mName[2].lower() + x + lName[0].lower() + lName[1].lower() + lName[2].lower())
   if comp == 3:
    for x in commonNumbers:
     usernames.append(fName[0].lower() + fName[1].lower() + fName[2].lower() + mName[0] + mName[1] + mName[2] + lName[0].lower() + lName[1].lower() + lName[2].lower() + x)
# 5. full names mix
 usernames.append(fName.lower()  + mName.lower() + lName.lower())
 usernames.append(lName.lower() + mName.lower() + fName.lower())
 if comp >= 2:
  for x in special:
   usernames.append(fName.lower() + mName.lower() + x + lName.lower())
   usernames.append(lName.lower() + mName.lower() + x + fName.lower())
   usernames.append(fName.lower() + x + mName.lower() + lName.lower())
   usernames.append(lName.lower() + x + mName.lower() + fName.lower())
  if comp == 3:
   for x in commonNumbers:
    usernames.append(fName.lower() + mName.lower() + lName.lower() + x)
    usernames.append(lName.lower() + mName.lower() + fName.lower() + x)

# Complexity 4
holder = []
if comp == 4:
 for x in usernames:
  for y in commonNumbers:
   holder.append(x + y)
 usernames = holder

# Mail domain
if args.domain:
 usernameMail = []
 for x in usernames:
  usernameMail.append(x + "@" + domain)
 usernames = usernameMail

# Print
if printCheck is True:
 for x in usernames:
  print (x)

# Create file
amount = len(usernames)
writeCheck = input(Fore.RED + "Your list will have " + str(amount) + " words in it. Are you sure you want to make the wordlist?[y/n]" + Style.RESET_ALL)

if writeCheck == "y":
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
else:
 quit()
