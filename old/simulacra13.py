#!/usr/bin/env python3

# Simulacra 1.3
# Written and developed by Stian Kvålshagen

# Todo
# Implement industry standard mode. (Complexity 0)

# New in 1.3!
# Added Swedish character convertion.
# Added ASCII art in easy mode.
# Added "quick large" and "quick small" mode. (Works with all sections!)
# Optimized convertion of scandinavic characters with advanced loops.

# This will be the last update for a while.

import sys
import argparse
import colorama
from colorama import Fore,Style

# Filters
special = [".","-","_"]
commonNumbers = ["1","2","3","4","5","6","7","8","9","12","123"]
c4MinNum = 0
c4MaxNum = 1000

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument("-c","--complexity",help="Adjust what level of complexity the usernames will be.\nNote that increasing complexity will increase size a lot!\nAdjust the settings in code if needed.",type=int)
parser.add_argument("-d","--domain",help="Print with mail domain. Example: outlook.com",action="store_true")
parser.add_argument("-e","--easy",help="Easy mode! Just follow the text. (For non-technical people.)",action="store_true")
parser.add_argument("-F","--firstname",help="The first name.",type=str)
parser.add_argument("-L","--lastname",help="The last name.",type=str)
parser.add_argument("-M","--middlename",help="The middle name.",type=str)
parser.add_argument("-no","--norwegian",help="Enable conversion of Norwegian/Danish letters [æ = 'ae,'a','e'] [ø = 'oo',o] [å = 'aa','a'].",action="store_true")
parser.add_argument("-p","--print",help="Print result",action=argparse.BooleanOptionalAction)
parser.add_argument("-qa","--quickall",help="Quick mode with max result. Will not affect easy mode.",action="store_true")
parser.add_argument("-qm","--quickminimum",help="Quick mode with minimum result. Will not affect easy mode.",action="store_true")
parser.add_argument("-sw","--swedish",help="Enable conversion of Swedish/Finish letters [ä = 'aa,'a'] [ö = 'oo',o] [å = 'aa','a'].",action="store_true")

comp = 2
maxComp = 4
args = parser.parse_args()
fName = args.firstname
lName = args.lastname
mName = args.middlename
qa = args.quickall
qm = args.quickminimum
if args.complexity:
 comp = args.complexity

# Easy mode
art = "  _________.__              .__\n /   _____/|__| _____  __ __|  | _____    ________________\n \_____  \ |  |/     \|  |  \  | \__  \ _/ ___\_  __ \__  \ \n /        \|  |  Y Y  \  |  /  |__/  __ \\  \___|  | \// __ \_\n/_______  /|__|__|_|  /____/|____(____  /\___  >__|  (____  /\n        \/          \/                \/     \/           \/\n"
if args.easy:
 print(art)
 fName = input(Fore.CYAN + "What is the first name? (Required)\n" + Style.RESET_ALL)
 if fName == "":
  print(Fore.RED + "You need a first name!" + Style.RESET_ALL)
  sys.exit()
 mName = input(Fore.CYAN + "What is the middle name? If nothing, press [Enter]\n" + Style.RESET_ALL)
 if mName != "":
  args.middlename = True
 lName = input(Fore.CYAN + "What is the last name? (Required)\n" + Style.RESET_ALL)
 if lName == "":
  print(Fore.RED + "You need a last name!" + Style.RESET_ALL)
  sys.exit()
 domainCheck = input(Fore.CYAN + "Do you want to use a domain?[y/n]\n" + Style.RESET_ALL)
 if domainCheck == "y":
  args.domain = True
 compIn = input(Fore.CYAN + "Please choose complexity level: 1 -  " + str(maxComp) + "\n" + Style.RESET_ALL)
 comp = int(compIn)
 norwegianCheck = input(Fore.CYAN + "Do you want to convert Norwegian/Danish letters? (æ,ø,å) [y/n]\n" + Style.RESET_ALL)
 if norwegianCheck == "y":
  args.norwegian = True
 swedishCheck = input(Fore.CYAN + "Do you want to convert Swedish/Finnish (ä,ö,å) letters? [y/n]\n" + Style.RESET_ALL)
 if swedishCheck == "y":
  args.swedish = True

# Error messages
if comp > maxComp:
 print(Fore.RED + "Please use complexity between 1 and " + str(maxComp) + Style.RESET_ALL)
 sys.exit()
if type(fName) != str:
 print(Fore.RED + "You need a first name!" + Style.RESET_ALL)
 sys.exit()
if type(lName) != str:
 print(Fore.RED + "You need a last name!" + Style.RESET_ALL)
 sys.exit()
if not args.middlename:
 print(Fore.GREEN + "Generating wordlist for: " + fName + " " + lName + Style.RESET_ALL)
if args.middlename:
 print(Fore.GREEN + "Generating wordlist for: " + fName + " " + mName + " " + lName + Style.RESET_ALL)
usernames = []

if comp >= 2:
 if not qm and not qa:
  compNr = input(Fore.CYAN + "Select special characters:\n[1] All default symbols ('.','-','_')\n[2] .\n[3] -\n[4] _ \n[5] Add your own symbols.\n" + Style.RESET_ALL)
 if qa:
  compNr = "1"
 if qm:
  compNr = "2"
 if compNr == "1":
  special = [".","-","_"]
 if compNr == "2":
  special = ["."]
 if compNr == "3":
  special = ["-"]
 if compNr == "4":
  special = ["-"]
 if compNr == "5":
  special = []
  symbols = input(Fore.CYAN + "Which symbols do you want to use? Separate with comma (,)\n" + Style.RESET_ALL)
  sList = symbols.split(',')
  for x in sList:
   special.append(x)

# Username combinations
# 1. First letter from lastname + name & vise versa
usernames.append(lName[0].lower() + fName.lower())
usernames.append(fName[0].lower() + lName.lower())
if comp >= 2:
 tmp = []
 for x in special:
  usernames.append(lName[0].lower() + x + fName.lower())
  usernames.append(fName[0].lower() + x + lName.lower())

# 2. pure names
usernames.append(fName.lower())
usernames.append(lName.lower())

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
   usernames.append(lName[0].lower() + x + mName[0].lower() + x + fName.lower())
   usernames.append(fName[0].lower() + x + mName[0].lower() + x + lName.lower())
   usernames.append(lName[0].lower() + x + mName.lower() + x + fName.lower())
   usernames.append(fName[0].lower() + x + mName.lower() + x + lName.lower())
# 2. middle name
 usernames.append(mName.lower())
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
# 4. 3 letters first name & 3 letters middle name &  3 letters last name
 usernames.append(fName[0].lower() + fName[1].lower() + fName[2].lower() + mName[0].lower() + mName[1].lower() + mName[2].lower() + lName[0].lower() + lName[1].lower() + lName[2].lower())
 if comp >= 2:
  for x in special:
   usernames.append(fName[0].lower() + fName[1].lower() + fName[2].lower() + mName[0].lower() + mName[1].lower() + mName[2].lower() + x +  lName[0].lower() + lName[1].lower() + lName[2].lower())
   usernames.append(fName[0].lower() + fName[1].lower() + fName[2].lower() + x + mName[0].lower() + mName[1].lower() + mName[2].lower() + lName[0].lower() + lName[1].lower() + lName[2].lower())
   usernames.append(fName[0].lower() + fName[1].lower() + fName[2].lower() + x + mName[0].lower() + mName[1].lower() + mName[2].lower() + x + lName[0].lower() + lName[1].lower() + lName[2].lower())
# 5. full names mix
 usernames.append(fName.lower()  + mName.lower() + lName.lower())
 usernames.append(lName.lower() + mName.lower() + fName.lower())
 if comp >= 2:
  for x in special:
   usernames.append(fName.lower() + mName.lower() + x + lName.lower())
   usernames.append(lName.lower() + mName.lower() + x + fName.lower())
   usernames.append(fName.lower() + x + mName.lower() + lName.lower())
   usernames.append(lName.lower() + x + mName.lower() + fName.lower())
   usernames.append(fName.lower() + x + mName.lower() + x + lName.lower())
   usernames.append(lName.lower() + x + mName.lower() + x + fName.lower())

# Complexity 3
holder = []
if comp == 3:
 for x in usernames:
  for y in commonNumbers:
   holder.append(x + y)
 for x in holder:
  usernames.append(x)

# Complexity 4
holder = []
if comp == 4:
 for x in usernames:
  for y in range(c4MinNum,c4MaxNum):
   holder.append(x + str(y))
 for x in holder:
  usernames.append(x)

# Convert Norwegian/Danish or Swedish letters into single and double letters.
if args.norwegian or args.swedish:
 if args.norwegian:
  l = ["æ","ø","å"]
  s = ["a","o","a","e"]
  d = ["ae","oo","aa"]
 if args.swedish:
  l = ["ä","ö","å"]
  s = ["a","o","a"]
  d = ["aa","oo","aa"]
 if not qm and not qa:
  if args.norwegian:
   uI = input(Fore.CYAN + "Select the following option to convert Norwegian/Danish letters:\n[1] Convert All\n[2] Convert double only (Ex: ø = oo)\n[3] Convert single only (Ex: ø = o)\n[4] None\n" + Style.RESET_ALL)
  if args.swedish:
   uI = input(Fore.CYAN + "Select the following option to convert Swedish/Finnish letters:\n[1] Convert All\n[2] Convert double only (Ex: ö = oo)\n[3] Convert single only (Ex: ö = o)\n[4] None\n" + Style.RESET_ALL)
 if qa:
  uI = "1"
 if qm:
  uI = "3"
 holder = []
 for o in range(3):
  for x in usernames:
   for y in range(len(l)):
    if l[y] in x.lower():
     if uI == "1" or uI == "2":
      scanVar = x.lower()
      scanVar = scanVar.replace(l[y],d[y])
      holder.append(scanVar)
     if uI == "1" or uI == "3":
      scanVar = x.lower()
      scanVar = scanVar.replace(l[y],s[y])
      holder.append(scanVar)
     if args.norwegian and not args.swedish:
      scanVar = scanVar.replace(l[0],s[3])
      holder.append(scanVar)
  for x in holder:
   usernames.append(x)

# Mail domains
if args.domain:
 skip = False
 if not qm and not qa:
  domains = input(Fore.CYAN + "Type the domains you want inserted sparated with coma (Ex: gmail.com,outlook.com)\n" + Style.RESET_ALL)
 if qa:
  domains = "gmail.com,outlook.com,yahoo.com"
 if qm:
  domains = "gmail.com"
 if domains == "":
  print("No domain detected. Skipping this part.")
  skip = True
 if not skip:
  domainList = domains.split(',')
  usernameMail = []
  for y in domainList:
   for x in usernames:
    usernameMail.append(x + "@" + y)
  usernames = usernameMail

# Remove duplicates from list
usernames = list(dict.fromkeys(usernames))

# Print
if args.print:
 print(Fore.GREEN + "Result:" + Style.RESET_ALL)
 for x in usernames:
  print (x)

# Create file
amount = len(usernames)
writeCheck = input(Fore.CYAN + "Your list will have " + str(amount) + " words in it. Are you sure you want to make the wordlist?[y/n]" + Style.RESET_ALL)
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
