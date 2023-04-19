#!/usr/bin/env python3

""" *------------------------------------------------------------------------------------------------------------*
 Simulacra 1.4
 Implemented functions and cleaned up some nasty code.
 Fixed the language function. You can now convert Norwegian AND Swedish characters.
 Replaced the generation pattern to make all possible combinations.
 Scandinavian characters is now automatically found and replaced instead of asked for. This should improve the flow.
 Complexity 3 and 4 is replaced with functions.
 Custom words function added.
 Custom Number range function added.
 Added exit instead of loop when choose forename and lastname is easy mode.
*------------------------------------------------------------------------------------------------------------* """
# TODO: Remove all the lower() when generating text.
# Written and developed by Stian Kvålshagen

import argparse
from colorama import Fore, Style

# Settings
special = [".", "-", "_"]
commonNumbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "12", "123"]
range_min = 0
range_max = 100

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--commonNr", help="Add common numbers to the back of generated usernames.")
parser.add_argument("-d", "--domain", help="Print with mail domain. Example: outlook.com", action="store_true")
parser.add_argument("-e", "--easy", help="Easy mode! Just follow the text. (For non-technical people.)",
                    action="store_true")
parser.add_argument("-F", "--firstname", help="The first name.", type=str)
parser.add_argument("-L", "--lastname", help="The last name.", type=str)
parser.add_argument("-l", "--light", help="Light mode. Generates less usernames.",
                    action=argparse.BooleanOptionalAction)
parser.add_argument("-M", "--middlename", help="The middle name.", type=str)
parser.add_argument("-p", "--print", help="Print result", action=argparse.BooleanOptionalAction)
parser.add_argument("-r", "--range", help=f"Add numbers {range_min} to {range_max} to the end of generated username.",
                    action=argparse.BooleanOptionalAction)
parser.add_argument("-qa", "--quickall", help="Quick mode with max result. Will not affect easy mode.",
                    action="store_true")
parser.add_argument("-qm", "--quickminimum", help="Quick mode with minimum result. Will not affect easy mode.",
                    action="store_true")

# Global variables. They work like settings to adjust what will be added in the final wordlist.
args = parser.parse_args()
f = args.firstname
l = args.lastname
m = args.middlename
quick_all = args.quickall
quick_minimum = args.quickminimum

forenames = []
middlenames = []
lastnames = []


def easy():
    print(
        f"  _________.__              .__\n /   _____/|__| _____  __ __|  | _____    ________________\n \_____  \ |  |/     \|  |  \  | \__  \ _/ ___\_  __ \__  \ \n /        \|  |  Y Y  \  |  /  |__/  __ \\  \___|  | \// __ \_\n/_______  /|__|__|_|  /____/|____(____  /\___  >__|  (____  /\n        \/          \/                \/     \/           \/\n")

    # Firstname
    while 1:
        f = input(f"{Fore.CYAN}What is the first name? [Required]\n{Style.RESET_ALL}")
        if f != "":
            break
        print(f"{Fore.RED}You need a first name!{Style.RESET_ALL}")
    forenames.append(f)

    # Middle name
    m = input(f"{Fore.CYAN}What is the middle name? If nothing, press [Enter]\n{Style.RESET_ALL}")
    if m != "":
        args.middlename = True
        middlenames.append(m)

    # Last name
    while 1:
        l = input(f"{Fore.CYAN}What is the last name? [Required]\n{Style.RESET_ALL}")
        if l != "":
            break
        print(f"{Fore.RED}You need a last name!{Style.RESET_ALL}")
    lastnames.append(l)

    # Light mode check.
    lightCheck = input(f"{Fore.CYAN}Light mode? [Less usernames][y/n]\n{Style.RESET_ALL}")
    if lightCheck == "y":
        args.light = True

    # Domain check.
    domainCheck = input(f"{Fore.CYAN}Do you want to use a domain?[y/n]\n{Style.RESET_ALL}")
    if domainCheck == "y":
        args.domain = True
    else:
        args.domain = False

    # Nr check.
    nrCheck = input(f"{Fore.CYAN}Do you want to add numbers to the end of the name?[y/n]\n{Style.RESET_ALL}")
    if nrCheck == "y":
        typeCheck = input(
            f"{Fore.CYAN}1. Common numbers. {' '.join(map(str, commonNumbers))}\n2. Everything between {range_min} and {range_max} \n3. No numbers. \n{Style.RESET_ALL}")
        match typeCheck:
            case "1":
                args.commonNr = True
            case "2":
                args.range = True


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
            symbols = input(f"{Fore.CYAN}Which symbols do you want to use? Separate with comma (,)\n{Style.RESET_ALL}")
            input_list = symbols.split(',')
            for special_input in input_list:
                special.append(special_input)


def non_light_mode(usernames):
    for f in forenames:
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


def add_commonNr(usernames):
    holder = []

    for f in forenames:
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


def range_add(usernames):
    holder = []
    for x in usernames:
        for y in range(range_min, range_max):
            holder.append(x + str(y))
    for x in holder:
        usernames.append(x)


def middle_name_add(usernames):
    for f in forenames:
        for l in lastnames:
            for m in middlenames:
                # 1 First letter from lastname & first name & vise versa including middle name)
                usernames.append(l[0].lower() + m[0].lower() + f.lower())
                usernames.append(f[0].lower() + m[0].lower() + l.lower())
                usernames.append(l[0].lower() + m.lower() + f.lower())
                usernames.append(f[0].lower() + m.lower() + l.lower())
                if args.light:
                    for x in special:
                        usernames.append(l[0].lower() + m[0].lower() + x + f.lower())
                        usernames.append(f[0].lower() + m[0].lower() + x + l.lower())
                        usernames.append(l[0].lower() + m.lower() + x + f.lower())
                        usernames.append(f[0].lower() + m.lower() + x + l.lower())
                        usernames.append(l[0].lower() + x + m[0].lower() + f.lower())
                        usernames.append(f[0].lower() + x + m[0].lower() + l.lower())
                        usernames.append(l[0].lower() + x + m.lower() + f.lower())
                        usernames.append(f[0].lower() + x + m.lower() + l.lower())
                        usernames.append(l[0].lower() + x + m[0].lower() + x + f.lower())
                        usernames.append(f[0].lower() + x + m[0].lower() + x + l.lower())
                        usernames.append(l[0].lower() + x + m.lower() + x + f.lower())
                        usernames.append(f[0].lower() + x + m.lower() + x + l.lower())

                # 2. middle name
                usernames.append(m.lower())

                # 3. name & 1 letter middle name & 3 letters last name
                usernames.append(f.lower() + m[0].lower() + l[0].lower() + l[1].lower() + l[2].lower())
                if args.light:
                    for x in special:
                        usernames.append(f.lower() + m[0].lower() + x + l[0].lower() + l[1].lower() + l[2].lower())
                        usernames.append(f.lower() + m.lower() + x + l[0].lower() + l[1].lower() + l[2].lower())
                        usernames.append(f.lower() + x + m[0].lower() + l[0].lower() + l[1].lower() + l[2].lower())
                        usernames.append(f.lower() + x + m.lower() + l[0].lower() + l[1].lower() + l[2].lower())
                        usernames.append(f.lower() + x + m[0].lower() + x + l[0].lower() + l[1].lower() + l[2].lower())
                        usernames.append(f.lower() + x + m.lower() + x + l[0].lower() + l[1].lower() + l[2].lower())

                # 4. 3 letters first name & 3 letters middle name &  3 letters last name
                usernames.append(
                    f[0].lower() + f[1].lower() + f[2].lower() + m[0].lower() + m[1].lower() + m[2].lower() + l[
                        0].lower() + l[1].lower() + l[2].lower())
                if args.light:
                    for x in special:
                        usernames.append(
                            f[0].lower() + f[1].lower() + f[2].lower() + m[0].lower() + m[1].lower() + m[
                                2].lower() + x + l[0].lower() + l[1].lower() + l[2].lower())
                        usernames.append(
                            f[0].lower() + f[1].lower() + f[2].lower() + x + m[0].lower() + m[1].lower() + m[
                                2].lower() + l[0].lower() + l[1].lower() + l[2].lower())
                        usernames.append(
                            f[0].lower() + f[1].lower() + f[2].lower() + x + m[0].lower() + m[1].lower() + m[
                                2].lower() + x + l[0].lower() + l[1].lower() + l[2].lower())

                # 5. full names mix
                usernames.append(f.lower() + m.lower() + l.lower())
                usernames.append(l.lower() + m.lower() + f.lower())
                if args.light:
                    for x in special:
                        usernames.append(f.lower() + m.lower() + x + l.lower())
                        usernames.append(l.lower() + m.lower() + x + f.lower())
                        usernames.append(f.lower() + x + m.lower() + l.lower())
                        usernames.append(l.lower() + x + m.lower() + f.lower())
                        usernames.append(f.lower() + x + m.lower() + x + l.lower())
                        usernames.append(l.lower() + x + m.lower() + x + f.lower())


# Convert Norwegian/Danish or Swedish letters into single and double letters.
def scandinavian():
    global quick_all, quick_minimum
    if not quick_minimum and not quick_all:
        if quick_all:
            uI = "1"
        if quick_minimum:
            uI = "3"
        if not quick_minimum and not quick_all:
            if args.middlename:
                if "ø" in forenames[0] or "æ" in forenames[0] or "å" in forenames[0] or "ø" in lastnames[0] or "æ" in \
                        lastnames[0] or "å" in lastnames[0] or "ø" in middlenames[0] or "æ" in middlenames[0] or "å" in \
                        middlenames[0]:
                    uI = input(
                        f"{Fore.CYAN}Select the following option to convert Norwegian/Danish letters:\n[1] Convert All\n[2] Convert double only (Ex: ø = oo)\n[3] Convert single only (Ex: ø = o)\n[4] None\n{Style.RESET_ALL}")
            else:
                if "ø" in forenames[0] or "æ" in forenames[0] or "å" in forenames[0] or "ø" in lastnames[0] or "æ" in \
                        lastnames[0] or "å" in lastnames[0]:
                    uI = input(
                        f"{Fore.CYAN}Select the following option to convert Norwegian/Danish letters:\n[1] Convert All\n[2] Convert double only (Ex: ø = oo)\n[3] Convert single only (Ex: ø = o)\n[4] None\n{Style.RESET_ALL}")
            nor_combo_1 = ["æ", "ø", "å"]
            nor_combo_2 = ["a", "o", "a", "e"]
            nor_combo_3 = ["ae", "oo", "aa"]
            convert_scandinavian(nor_combo_1, nor_combo_2, nor_combo_3, uI)
        if quick_all:
            uI = "1"
        if quick_minimum:
            uI = "3"
        if not quick_minimum and not quick_all:
            if args.middlename:
                if "ä" in forenames[0] or "ö" in forenames[0] or "ä" in lastnames[0] or "ö" in lastnames[0] or "ä" in \
                        middlenames[0] or "ö" in middlenames[0]:
                    uI = input(
                        f"{Fore.CYAN}Select the following option to convert Swedish/Finnish letters:\n[1] Convert All\n[2] Convert double only (Ex: ö = oo)\n[3] Convert single only (Ex: ö = o)\n[4] None\n{Style.RESET_ALL}")
            else:
                if "ä" in forenames[0] or "ö" in forenames[0] or "ä" in lastnames[0] or "ö" in lastnames[0]:
                    uI = input(
                        f"{Fore.CYAN}Select the following option to convert Swedish/Finnish letters:\n[1] Convert All\n[2] Convert double only (Ex: ö = oo)\n[3] Convert single only (Ex: ö = o)\n[4] None\n{Style.RESET_ALL}")
                swe_combo_1 = ["ä", "ö", "å"]
                swe_combo_2 = ["a", "o", "a"]
                swe_combo_3 = ["aa", "oo", "aa"]
                convert_scandinavian(swe_combo_1, swe_combo_2, swe_combo_3, uI)


def convert_scandinavian(combo_1, combo_2, combo_3, user_input):
    if args.middlename:
        checks = [forenames, lastnames, middlenames]
    else:
        checks = [forenames, lastnames]
    for current in checks:
        cache = []
        for x in current:
            for y in range(len(combo_1)):
                if combo_1[y] in x.lower():
                    if user_input == "1" or user_input == "2":
                        scanVar = x.lower()
                        scanVar = scanVar.replace(combo_1[y], combo_3[y])
                        cache.append(scanVar)
                    if user_input == "1" or user_input == "3":
                        scanVar = x.lower()
                        scanVar = scanVar.replace(combo_1[y], combo_2[y])
                        cache.append(scanVar)
        for x in cache:
            current.append(x)


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
            file = open(f"{forenames[0]}_{c}.txt", "x")
            print(f"{forenames[0]}_{c}.txt created.")
            ready = True
        except:
            print(f"{forenames[0]}_{c}.txt already exists..")
            c = c + 1
    for x in usernames:
        file.write(x + "\n")


def questions():
    skip = False

    if args.domain:
        if not quick_minimum and not quick_all:
            domains_input = input(
                f"{Fore.CYAN}Type the domains you want inserted separated with coma (Ex: gmail.com,outlook.com)\n{Style.RESET_ALL}")
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
            f"{Fore.CYAN}Select special characters:\n[1] All default symbols ('.','-','_')\n[2] .\n[3] -\n[4] _ \n[5] Add your own symbols.\n{Style.RESET_ALL}")
    if quick_all:
        special_nr = "1"
    if quick_minimum:
        special_nr = "2"
    return special_nr, domains_input, skip


def generate_wordlist():
    usernames = []

    # Fill the lists if it is not running easy mode.
    if args.firstname != "":
        forenames.append(args.firstname)
    if args.middlename != "":
        middlenames.append(args.middlename)
    if args.lastname != "":
        lastnames.append(args.lastname)

    if not args.middlename:
        print(f"{Fore.GREEN}Generating wordlist for: {forenames[0]} {lastnames[0]} {Style.RESET_ALL}")
    if args.middlename:
        print(f"{Fore.GREEN}Generating wordlist for {forenames[0]} {middlenames[0]} {lastnames[0]} {Style.RESET_ALL}: ")

    if "ø" in forenames[0] or "æ" in forenames[0] or "å" in forenames[0] or "ä" in forenames[0] or "ö" in forenames[
        0] or "ø" in lastnames[0] or "æ" in lastnames[0] or "å" in lastnames[0] or "ä" in lastnames[0] or "ö" in \
            lastnames[0] or "ø" in middlenames[0] or "æ" in middlenames[0] or "å" in middlenames[0] or "ä" in \
            middlenames[0] or "ö" in middlenames[0]:
        scandinavian()

    for f in forenames:
        f = f.lower()
        for l in lastnames:
            l = l.lower()
            # The basic conversions! Will always be used.
            # 1. First letter from lastname + name & vise versa
            usernames.append(f"{l[0]}{f}")
            usernames.append(f"{f[0]}{l}")

            # 2. pure names
            usernames.append(f"{f}")
            usernames.append(f"{l}")

            # 3. name & 3 letters last name
            usernames.append(f"{f}{l[0]}{l[1]}{l[2]}")

            # 4. 3 letters first name & 3 letters lastname
            usernames.append(f"{f[0]}{f[1]}{f[2]}{l[0]}{l[1]}{l[2]}")

            # 4. 3 letters first name & 4 letters lastname
            usernames.append(
                f[0].lower() + f[1].lower() + f[2].lower() + l[0].lower() + l[1].lower() +
                l[2].lower() + l[3].lower())

            # 5. name and lastname
            usernames.append(f.lower() + l.lower())
            usernames.append(l.lower() + f.lower())

    special_nr, domains_input, skip = questions()

    if args.middlename:
        middle_name_add(usernames)
    if not args.light:
        non_light_mode(usernames)
        special_characters(special_nr)
    if args.commonNr:
        add_commonNr(usernames)
    if args.range:
        range_add(usernames)
    if args.domain:
        usernames = domains(usernames, skip, domains_input)

    # Remove duplicates from list
    usernames = list(dict.fromkeys(usernames))

    # Print if wanted.
    if args.print:
        print(f"{Fore.GREEN}Result:{Style.RESET_ALL}")
        for x in usernames:
            print(x)

    # Ask use if they want the wordlist.
    for x in forenames:
        print(x)
    amount = len(usernames)
    writeCheck = input(
        f"{Fore.CYAN}Your list will have {amount} words in it. Are you sure you want to make the wordlist?[y/n]{Style.RESET_ALL}")
    if writeCheck == "y":
        write_result(usernames)
    else:
        quit(0)


if args.easy:
    easy()
generate_wordlist()
