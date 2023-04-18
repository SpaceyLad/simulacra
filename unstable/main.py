#!/usr/bin/env python3

# Simulacra 1.4
# Implemented functions and cleaned up some nasty code.
# Fixed the language function. You can now convert Norwegian AND Swedish characters.
# Replaced the generation pattern to make all possible combinations.
# Scandinavian characters is now automatically found and replaced instead of asked for. This should improve the flow.
# Complexity 3 and 4 is replaced with functions.
# Custom words function added.
# Custom Number range function added.
# Added exit instead of loop when choose forename and lastname is easy mode.

# Written and developed by Stian Kvålshagen

# TODO: Replace complexity 3 and 4 with functions.
# TODO: Add number and number range to easy mode.

import sys
import argparse
from colorama import Fore, Style

# Settings
special = [".", "-", "_"]
commonNumbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "12", "123"]
c4MinNum = 0
c4MaxNum = 1000

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--complexity",
                    help="Adjust what level of complexity the usernames will be.\nNote that increasing complexity will increase size a lot!\nAdjust the settings in code if needed.",
                    type=int)
parser.add_argument("-d", "--domain", help="Print with mail domain. Example: outlook.com", action="store_true")
parser.add_argument("-e", "--easy", help="Easy mode! Just follow the text. (For non-technical people.)",
                    action="store_true")
parser.add_argument("-F", "--firstname", help="The first name.", type=str)
parser.add_argument("-L", "--lastname", help="The last name.", type=str)
parser.add_argument("-M", "--middlename", help="The middle name.", type=str)
parser.add_argument("-p", "--print", help="Print result", action=argparse.BooleanOptionalAction)
parser.add_argument("-qa", "--quickall", help="Quick mode with max result. Will not affect easy mode.",
                    action="store_true")
parser.add_argument("-qm", "--quickminimum", help="Quick mode with minimum result. Will not affect easy mode.",
                    action="store_true")

# Global variables. They work like settings to adjust what will be added in the final wordlist.
comp = 2
maxComp = 4
args = parser.parse_args()
forename = args.firstname
last_name = args.lastname
middle_name = args.middlename
quick_all = args.quickall
quick_minimum = args.quickminimum
if args.complexity:
    comp = args.complexity

fornames = []
middlenames = []
lastnames = []


def easy():
    global comp, forename, middle_name, last_name
    art = "  _________.__              .__\n /   _____/|__| _____  __ __|  | _____    ________________\n \_____  \ |  |/     \|  |  \  | \__  \ _/ ___\_  __ \__  \ \n /        \|  |  Y Y  \  |  /  |__/  __ \\  \___|  | \// __ \_\n/_______  /|__|__|_|  /____/|____(____  /\___  >__|  (____  /\n        \/          \/                \/     \/           \/\n"
    print(art)
    while 1:
        forename = input(Fore.CYAN + "What is the first name? [Required]\n" + Style.RESET_ALL)
        if forename != "":
            break
        print(Fore.RED + "You need a first name!" + Style.RESET_ALL)
    fornames.append(forename)
    middle_name = input(Fore.CYAN + "What is the middle name? If nothing, press [Enter]\n" + Style.RESET_ALL)
    if middle_name != "":
        args.middlename = True
        middlenames.append(middle_name)
    while 1:
        last_name = input(Fore.CYAN + "What is the last name? [Required]\n" + Style.RESET_ALL)
        if last_name != "":
            break
        print(Fore.RED + "You need a last name!" + Style.RESET_ALL)
    lastnames.append(last_name)
    compIn = input(Fore.CYAN + "Please choose complexity level: 1 -  " + str(maxComp) + "\n" + Style.RESET_ALL)
    comp = int(compIn)
    domainCheck = input(Fore.CYAN + "Do you want to use a domain?[y/n]\n" + Style.RESET_ALL)
    if domainCheck == "y":
        args.domain = True
    else:
        args.domain = False


def error_check():
    if comp > maxComp:
        print(Fore.RED + "Please use complexity between 1 and " + str(maxComp) + Style.RESET_ALL)
        sys.exit()
    if type(forename) != str:
        print(Fore.RED + "You need a first name!" + Style.RESET_ALL)
        sys.exit()
    if type(last_name) != str:
        print(Fore.RED + "You need a last name!" + Style.RESET_ALL)
        sys.exit()


def special_characters(special_nr):
    global special

    match special_nr:
        case "1":
            special = [".", "-", "_"]
        case "2":
            special = ["."]
        case "3":
            special = ["-"]
        case "4":
            special = ["-"]
        case "5":
            symbols = input(Fore.CYAN + "Which symbols do you want to use? Separate with comma (,)\n" + Style.RESET_ALL)
            input_list = symbols.split(',')
            for special_input in input_list:
                special.append(special_input)


def complexity_2(usernames):
    for f in fornames:
        for l in lastnames:
            for x in special:
                usernames.append(l[0].lower() + x + f.lower())
                usernames.append(f[0].lower() + x + l.lower())

            for x in special:
                usernames.append(f.lower() + x + l[0].lower() + l[1].lower() + l[2].lower())

            for x in special:
                usernames.append(
                    f[0].lower() + f[1].lower() + f[2].lower() + x + l[0].lower() + l[
                        1].lower() + l[
                        2].lower())

            for x in special:
                usernames.append(f.lower() + x + l.lower())
                usernames.append(l.lower() + x + f.lower())


def complexity_3(usernames):
    holder = []

    for f in fornames:
        for l in lastnames:
            for x in commonNumbers:
                usernames.append(f.lower() + f[0].lower() + l[1].lower() + l[2].lower() + x)

            for x in commonNumbers:
                usernames.append(f.lower() + l.lower() + x)
                usernames.append(l.lower() + f.lower() + x)

    for x in usernames:
        for y in commonNumbers:
            holder.append(x + y)
    for x in holder:
        usernames.append(x)


def complexity_4(usernames):
    holder = []
    if comp == 4:
        for x in usernames:
            for y in range(c4MinNum, c4MaxNum):
                holder.append(x + str(y))
        for x in holder:
            usernames.append(x)


def middle_name_add(usernames):
    # 1 First letter from lastname & first name & vise versa including middle name)
    usernames.append(last_name[0].lower() + middle_name[0].lower() + forename.lower())
    usernames.append(forename[0].lower() + middle_name[0].lower() + last_name.lower())
    usernames.append(last_name[0].lower() + middle_name.lower() + forename.lower())
    usernames.append(forename[0].lower() + middle_name.lower() + last_name.lower())
    if comp >= 2:
        for x in special:
            usernames.append(last_name[0].lower() + middle_name[0].lower() + x + forename.lower())
            usernames.append(forename[0].lower() + middle_name[0].lower() + x + last_name.lower())
            usernames.append(last_name[0].lower() + middle_name.lower() + x + forename.lower())
            usernames.append(forename[0].lower() + middle_name.lower() + x + last_name.lower())
            usernames.append(last_name[0].lower() + x + middle_name[0].lower() + forename.lower())
            usernames.append(forename[0].lower() + x + middle_name[0].lower() + last_name.lower())
            usernames.append(last_name[0].lower() + x + middle_name.lower() + forename.lower())
            usernames.append(forename[0].lower() + x + middle_name.lower() + last_name.lower())
            usernames.append(last_name[0].lower() + x + middle_name[0].lower() + x + forename.lower())
            usernames.append(forename[0].lower() + x + middle_name[0].lower() + x + last_name.lower())
            usernames.append(last_name[0].lower() + x + middle_name.lower() + x + forename.lower())
            usernames.append(forename[0].lower() + x + middle_name.lower() + x + last_name.lower())

    # 2. middle name
    usernames.append(middle_name.lower())

    # 3. name & 1 letter middle name & 3 letters last name
    usernames.append(
        forename.lower() + middle_name[0].lower() + last_name[0].lower() + last_name[1].lower() + last_name[2].lower())
    if comp >= 2:
        for x in special:
            usernames.append(
                forename.lower() + middle_name[0].lower() + x + last_name[0].lower() + last_name[1].lower() + last_name[
                    2].lower())
            usernames.append(
                forename.lower() + middle_name.lower() + x + last_name[0].lower() + last_name[1].lower() + last_name[
                    2].lower())
            usernames.append(
                forename.lower() + x + middle_name[0].lower() + last_name[0].lower() + last_name[1].lower() + last_name[
                    2].lower())
            usernames.append(
                forename.lower() + x + middle_name.lower() + last_name[0].lower() + last_name[1].lower() + last_name[
                    2].lower())
            usernames.append(
                forename.lower() + x + middle_name[0].lower() + x + last_name[0].lower() + last_name[1].lower() +
                last_name[2].lower())
            usernames.append(
                forename.lower() + x + middle_name.lower() + x + last_name[0].lower() + last_name[1].lower() +
                last_name[2].lower())

    # 4. 3 letters first name & 3 letters middle name &  3 letters last name
    usernames.append(
        forename[0].lower() + forename[1].lower() + forename[2].lower() + middle_name[0].lower() + middle_name[
            1].lower() + middle_name[
            2].lower() + last_name[0].lower() + last_name[1].lower() + last_name[2].lower())
    if comp >= 2:
        for x in special:
            usernames.append(
                forename[0].lower() + forename[1].lower() + forename[2].lower() + middle_name[0].lower() + middle_name[
                    1].lower() + middle_name[
                    2].lower() + x + last_name[0].lower() + last_name[1].lower() + last_name[2].lower())
            usernames.append(
                forename[0].lower() + forename[1].lower() + forename[2].lower() + x + middle_name[0].lower() +
                middle_name[1].lower() +
                middle_name[2].lower() + last_name[0].lower() + last_name[1].lower() + last_name[2].lower())
            usernames.append(
                forename[0].lower() + forename[1].lower() + forename[2].lower() + x + middle_name[0].lower() +
                middle_name[1].lower() +
                middle_name[2].lower() + x + last_name[0].lower() + last_name[1].lower() + last_name[2].lower())

    # 5. full names mix
    usernames.append(forename.lower() + middle_name.lower() + last_name.lower())
    usernames.append(last_name.lower() + middle_name.lower() + forename.lower())
    if comp >= 2:
        for x in special:
            usernames.append(forename.lower() + middle_name.lower() + x + last_name.lower())
            usernames.append(last_name.lower() + middle_name.lower() + x + forename.lower())
            usernames.append(forename.lower() + x + middle_name.lower() + last_name.lower())
            usernames.append(last_name.lower() + x + middle_name.lower() + forename.lower())
            usernames.append(forename.lower() + x + middle_name.lower() + x + last_name.lower())
            usernames.append(last_name.lower() + x + middle_name.lower() + x + forename.lower())


# Convert Norwegian/Danish or Swedish letters into single and double letters.
def scandinavian(fornames, lastnames):
    global quick_all, quick_minimum
    if not quick_minimum and not quick_all:
        if quick_all:
            uI = "1"
        if quick_minimum:
            uI = "3"
        if not quick_minimum and not quick_all:
            if "ø" in forename or "æ" in forename or "å" in forename or "ø" in last_name or "æ" in last_name or "å" in last_name or "ø" in middle_name or "æ" in middle_name or "å" in middle_name:
                uI = input(
                    Fore.CYAN + "Select the following option to convert Norwegian/Danish letters:\n[1] Convert All\n[2] Convert double only (Ex: ø = oo)\n[3] Convert single only (Ex: ø = o)\n[4] None\n" + Style.RESET_ALL)
            nor_combo_1 = ["æ", "ø", "å"]
            nor_combo_2 = ["a", "o", "a", "e"]
            nor_combo_3 = ["ae", "oo", "aa"]
            convert_scandinavian(nor_combo_1, nor_combo_2, nor_combo_3, uI, fornames, lastnames)
        if quick_all:
            uI = "1"
        if quick_minimum:
            uI = "3"
        if not quick_minimum and not quick_all:
            if "ä" in forename or "ö" in forename or "ä" in last_name or "ö" in last_name or "ä" in middle_name or "ö" in middle_name:
                uI = input(
                    Fore.CYAN + "Select the following option to convert Swedish/Finnish letters:\n[1] Convert All\n[2] Convert double only (Ex: ö = oo)\n[3] Convert single only (Ex: ö = o)\n[4] None\n" + Style.RESET_ALL)
            swe_combo_1 = ["ä", "ö", "å"]
            swe_combo_2 = ["a", "o", "a"]
            swe_combo_3 = ["aa", "oo", "aa"]
            convert_scandinavian(swe_combo_1, swe_combo_2, swe_combo_3, uI, fornames, lastnames)


def convert_scandinavian(combo_1, combo_2, combo_3, user_input, fornames, lastnames):
    u_cache = []
    p_cache = []
    for o in range(3):
        for x in fornames:
            for y in range(len(combo_1)):
                if combo_1[y] in x.lower():
                    if user_input == "1" or user_input == "2":
                        scanVar = x.lower()
                        scanVar = scanVar.replace(combo_1[y], combo_3[y])
                        u_cache.append(scanVar)
                    if user_input == "1" or user_input == "3":
                        scanVar = x.lower()
                        scanVar = scanVar.replace(combo_1[y], combo_2[y])
                        u_cache.append(scanVar)
        for x in u_cache:
            fornames.append(x)

        for o in range(3):
            for x in lastnames:
                for y in range(len(combo_1)):
                    if combo_1[y] in x.lower():
                        if user_input == "1" or user_input == "2":
                            scanVar = x.lower()
                            scanVar = scanVar.replace(combo_1[y], combo_3[y])
                            u_cache.append(scanVar)
                        if user_input == "1" or user_input == "3":
                            scanVar = x.lower()
                            scanVar = scanVar.replace(combo_1[y], combo_2[y])
                            u_cache.append(scanVar)
            for x in u_cache:
                lastnames.append(x)


def domains(usernames, skip, domains_input):
    usernameMail = []
    if not skip:
        domainList = domains_input.split(',')
        for y in domainList:
            for x in usernames:
                usernameMail.append(x + "@" + y)
        usernames = usernameMail
        return usernames


def write_result(usernames):
    c = 0
    ready = False
    while not ready:
        try:
            file = open(forename.lower() + "_" + str(c) + ".txt", "x")
            print(forename.lower() + "_" + str(c) + ".txt created.")
            ready = True
        except:
            print(forename.lower() + "_" + str(c) + ".txt allready exists..")
            c = c + 1
    for x in usernames:
        file.write(x + "\n")


def questions():
    skip = False

    if args.domain:
        if not quick_minimum and not quick_all:
            domains_input = input(
                Fore.CYAN + "Type the domains you want inserted separated with coma (Ex: gmail.com,outlook.com)\n" + Style.RESET_ALL)
        if quick_all:
            domains_input = "gmail.com,outlook.com,yahoo.com"
        if quick_minimum:
            domains_input = "gmail.com"
        if domains_input == "":
            print("No domain detected. Skipping this part.")
            skip = True
    else:
        domains_input = ""

    if not quick_minimum and not quick_all:
        special_nr = input(
            Fore.CYAN + "Select special characters:\n[1] All default symbols ('.','-','_')\n[2] .\n[3] -\n[4] _ \n[5] Add your own symbols.\n" + Style.RESET_ALL)
    if quick_all:
        special_nr = "1"
    if quick_minimum:
        special_nr = "2"
    return special_nr, domains_input, skip


def generate_wordlist():
    usernames = []

    if not args.middlename:
        print(Fore.GREEN + "Generating wordlist for: " + forename + " " + last_name + Style.RESET_ALL)
    if args.middlename:
        print(
            Fore.GREEN + "Generating wordlist for: " + forename + " " + middle_name + " " + last_name + Style.RESET_ALL)
    if "ø" in forename or "æ" in forename or "å" in forename or "ä" in forename or "ö" in forename or "ø" in last_name or "æ" in last_name or "å" in last_name or "ä" in last_name or "ö" in middle_name or "ø" in middle_name or "æ" in middle_name or "å" in middle_name or "ä" in middle_name or "ö" in middle_name:
        scandinavian(fornames, lastnames)

    for f in fornames:
        for l in lastnames:
            # 1. First letter from lastname + name & vise versa
            usernames.append(l[0].lower() + f.lower())
            usernames.append(f[0].lower() + l.lower())

            # 2. pure names
            usernames.append(f.lower())
            usernames.append(l.lower())

            # 3. name & 3 letters last name
            usernames.append(f.lower() + l[0].lower() + l[1].lower() + l[2].lower())

            # 4. 3 letters first name & 3 letters lastname
            usernames.append(
                f[0].lower() + f[1].lower() + f[2].lower() + l[0].lower() + l[1].lower() +
                l[2].lower())

            # 5. name and lastname
            usernames.append(f.lower() + l.lower())
            usernames.append(l.lower() + f.lower())

    special_nr, domains_input, skip = questions()

    if args.middlename:
        middle_name_add(usernames)
    if comp >= 2:
        complexity_2(usernames)
    if comp >= 3:
        complexity_3(usernames)
    if comp >= 4:
        complexity_4(usernames)
    if comp >= 2:
        special_characters(special_nr)
    if args.domain:
        usernames = domains(usernames, skip, domains_input)

    # Remove duplicates from list
    usernames = list(dict.fromkeys(usernames))

    # Print if wanted.
    if args.print:
        print(Fore.GREEN + "Result:" + Style.RESET_ALL)
        for x in usernames:
            print(x)

    # Ask use if they want the wordlist.
    amount = len(usernames)
    writeCheck = input(Fore.CYAN + "Your list will have " + str(
        amount) + " words in it. Are you sure you want to make the wordlist?[y/n]" + Style.RESET_ALL)
    if writeCheck == "y":
        write_result(usernames)
    else:
        quit(0)


if args.easy:
    easy()
error_check()
generate_wordlist()
