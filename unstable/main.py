#!/usr/bin/env python3
import argparse
from colorama import Fore, Style

""" *------------------------------------------------------------------------------------------------------------*
    Author:Stian Kvålshagen
    Date: 13.05.2023
*------------------------------------------------------------------------------------------------------------* """

""" *------------------------------------------------------------------------------------------------------------*
 Simulacra 1.4
 Implemented functions and cleaned up some nasty code.
 Fixed the language function. You can now convert Norwegian AND Swedish characters.
 Replaced the generation pattern to make all possible combinations.
 Scandinavian characters is now automatically found and replaced instead of asked for. This should improve the flow.
 Complexity 3 and 4 is replaced with functions called common_nr and range.
 Custom Number range function added.
 Added exit instead of loop when choose forename and lastname is easy mode.
*------------------------------------------------------------------------------------------------------------* """

# Settings
special = [".", "-", "_"]
commonNumbers = ["1", "2", "3", "12", "123"]
range_min = 0
range_max = 100


def easy():
    print(
        f"  _________.__              .__\n /   _____/|__| _____  __ __|  | _____    ________________\n \_____  \ |  |/     \|  |  \  | \__  \ _/ ___\_  __ \__  \ \n /        \|  |  Y Y  \  |  /  |__/  __ \\  \___|  | \// __ \_\n/_______  /|__|__|_|  /____/|____(____  /\___  >__|  (____  /\n        \/          \/                \/     \/           \/\n")

    def input_with_check(prompt, error_msg):
        while True:
            value = input(prompt)
            if value:
                return value
            print(error_msg)

    forenames.append(input_with_check(f"{Fore.CYAN}What is the first name? [Required]\n{Style.RESET_ALL}",
                                      f"{Fore.RED}You need a first name!{Style.RESET_ALL}"))
    middle_name = input(f"{Fore.CYAN}What is the middle name? If nothing, press [Enter]\n{Style.RESET_ALL}")
    if middle_name:
        args.middlename = middle_name
        middlenames.append(middle_name)
    lastnames.append(input_with_check(f"{Fore.CYAN}What is the last name? [Required]\n{Style.RESET_ALL}",
                                      f"{Fore.RED}You need a last name!{Style.RESET_ALL}"))

    args.light = input(f"{Fore.CYAN}Light mode? [Less usernames][y/n]\n{Style.RESET_ALL}") == "y"
    args.domain = input(f"{Fore.CYAN}Do you want to use a domain?[y/n]\n{Style.RESET_ALL}") == "y"
    if input(f"{Fore.CYAN}Do you want to add numbers to the end of the name?[y/n]\n{Style.RESET_ALL}") == "y":
        typeCheck = input(
            f"{Fore.CYAN}1. Common numbers. {' '.join(map(str, commonNumbers))}\n2. Everything between {range_min} and {range_max} \n3. No numbers. \n{Style.RESET_ALL}")
        args.commonNr = typeCheck == "1"
        args.range = typeCheck == "2"


def special_characters(special_nr, usernames):
    global special

    def non_light_mode(usernames):
        for f in forenames:
            for l in lastnames:
                for x in special:
                    f = f.lower()
                    l = l.lower()
                    if args.industry:
                        usernames.append(f"{f}.{l}")
                        usernames.append(f"{l}_{f}")
                    else:
                        # Write what this part does here!
                        usernames.append(f"{l[0]}{x}{f}")
                        usernames.append(f"{f[0]}{x}{l}")

                        # Write what this part does here!
                        usernames.append(f"{f}{x}{l[0]}{l[1]}{l[2]}")

                        # Write what this part does here!
                        usernames.append(f"{f[0]}{f[1]}{f[2]}{x}{l[0]}{l[1]}{l[2]}")

                        # Write what this part does here!
                        usernames.append(f"{f}{x}{l}")
                        usernames.append(f"{l}{x}{f}")

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
    non_light_mode(usernames)


def middle_name_add(usernames):
    def add_middle_name(usernames, m):
        usernames.append(f"{m}")

    def add_initial_variations(usernames, f, m, l, special_chars=None):
        initial_variations = [
            f"{l[0]}{m}{f}",
            f"{f[0]}{m}{l}",
            f"{l[0]}{m[0]}{f}",
            f"{f[0]}{m[0]}{l}",
            f"{l[0]}{m[0]}{f[0]}",
            f"{f[0]}{m[0]}{l[0]}",
            f"{l[0]}{m}{f[0]}",
            f"{f[0]}{m}{l[0]}"
        ]

        if special_chars:
            for x in special_chars:
                initial_variations += [
                    f"{l[0]}{m[0]}{x}{f}",
                    f"{f[0]}{m[0]}{x}{l}",
                    f"{l[0]}{m}{x}{f}",
                    f"{f[0]}{m}{x}{l}",
                    f"{l[0]}{x}{m[0]}{f}",
                    f"{f[0]}{x}{m[0]}{l}",
                    f"{l[0]}{x}{m}{f}",
                    f"{f[0]}{x}{m}{l}",
                    f"{l[0]}{x}{m[0]}{x}{f}",
                    f"{f[0]}{x}{m[0]}{x}{l}",
                    f"{l[0]}{x}{m}{x}{f}",
                    f"{f[0]}{x}{m}{x}{l}"
                ]

        usernames.extend(initial_variations)

    def add_name_variations(usernames, f, m, l, special_chars):
        name_variations = [
            f"{f}{m[0]}{l[0]}{l[1]}{l[2]}",
            f"{f[0]}{f[1]}{f[2]}{m[0]}{m[1]}{m[2]}{l[0]}{l[1]}{l[2]}",
            f"{f}{m}{l}",
            f"{l}{m}{f}"
        ]

        if special_chars:
            for x in special_chars:
                name_variations += [
                    f"{f}{m[0]}{x}{l[0]}{l[1]}{l[2]}",
                    f"{f}{m}{x}{l[0]}{l[1]}{l[2]}",
                    f"{f}{x}{m[0]}{l[0]}{l[1]}{l[2]}",
                    f"{f}{x}{m}{l[0]}{l[1]}{l[2]}",
                    f"{f}{x}{m[0]}{x}{l[0]}{l[1]}{l[2]}",
                    f"{f}{x}{m}{x}{l[0]}{l[1]}{l[2]}",
                    f"{f[0]}{f[1]}{f[2]}{m[0]}{m[1]}{m[2]}{x}{l[0]}{l[1]}{l[2]}",
                    f"{f[0]}{f[1]}{f[2]}{x}{m[0]}{m[1]}{m[2]}{l[0]}{l[1]}{l[2]}",
                    f"{f[0]}{f[1]}{f[2]}{x}{m[0]}{m[1]}{m[2]}{x}{l[0]}{l[1]}{l[2]}",
                    f"{f}{m}{x}{l}",
                    f"{l}{m}{x}{f}",
                    f"{f}{x}{m}{l}",
                    f"{l}{x}{m}{f}",
                    f"{f}{x}{m}{x}{l}",
                    f"{l}{x}{m}{x}{f}"
                ]
            usernames.extend(name_variations)

    light_mode = args.light if args else False
    for f in forenames:
        for l in lastnames:
            for m in middlenames:
                f = f.lower()
                m = m.lower()
                l = l.lower()
                add_middle_name(usernames, m)
                add_initial_variations(usernames, f, m, l, special if not light_mode else None)
                add_name_variations(usernames, f, m, l, special if not light_mode else None)


# Convert Norwegian/Danish or Swedish letters into single and double letters.
def scandinavian():
    global quick_all, quick_minimum

    def scandinavian_letter_check(lang_letters, name_parts):
        return any(l in name_part for name_part in name_parts for l in lang_letters)

    def prompt_conversion_options(language):
        return input(
            f"{Fore.CYAN}Select the following option to convert {language} letters:\n"
            f"[1] Convert All\n"
            f"[2] Convert double only (Ex: ø = oo)\n"
            f"[3] Convert single only (Ex: ø = o)\n"
            f"[4] None\n"
            f"{Style.RESET_ALL}"
        )

    def convert_letters(combo_1, combo_2, combo_3, user_input):
        # Set up the list of name categories to check
        name_categories = [forenames, lastnames]
        if args.middlename:
            name_categories.append(middlenames)

        # Iterate through each name category and apply the conversion rules
        for name_category in name_categories:
            converted_names = []

            for name in name_category:
                name_lower = name.lower()

                for i, combo in enumerate(combo_1):
                    if combo in name_lower.lower():
                        # Apply conversion based on user input
                        if user_input in ["1", "2"]:
                            converted_names.append(name_lower.replace(combo, combo_3[i]))
                        if user_input in ["1", "3"]:
                            converted_names.append(name_lower.replace(combo, combo_2[i]))

            # Add the converted names to the current name category
            name_category.extend(converted_names)

    if not quick_minimum and not quick_all:
        name_parts = forenames + lastnames + (middlenames if args.middlename else [])

        norwegian_letters = ["æ", "ø", "å"]
        if scandinavian_letter_check(norwegian_letters, name_parts):
            user_input = prompt_conversion_options("Norwegian/Danish")
            nor_combo_1, nor_combo_2, nor_combo_3 = norwegian_letters, ["a", "o", "a"], ["ae", "oo", "aa"]
            convert_letters(nor_combo_1, nor_combo_2, nor_combo_3, user_input)

        swedish_letters = ["ä", "ö", "å"]
        if scandinavian_letter_check(swedish_letters, name_parts):
            user_input = prompt_conversion_options("Swedish/Finnish")
            swe_combo_1, swe_combo_2, swe_combo_3 = swedish_letters, ["a", "o", "a"], ["aa", "oo", "aa"]
            convert_letters(swe_combo_1, swe_combo_2, swe_combo_3, user_input)


def write_result(usernames):
    count = 0
    while 1:
        try:
            with open(f"{forenames[0]}_{count}.txt", "x") as file:
                print(f"{forenames[0]}_{count}.txt created.")
                for x in usernames:
                    file.write(x + "\n")
                break
        except FileExistsError:
            print(f"{forenames[0]}_{count}.txt already exists..")
            count += 1


def questions():
    skip = False
    domains_input = ""

    if args.domain:
        if not quick_minimum and not quick_all:
            domains_input = input(
                f"{Fore.CYAN}Type the domains you want inserted separated with coma (Ex: gmail.com,outlook.com)\n{Style.RESET_ALL}")
        elif quick_all:
            domains_input = "gmail.com,outlook.com,yahoo.com"
        elif quick_minimum:
            domains_input = "gmail.com"

        if not domains_input:
            print("No domain detected. Skipping this part.")
            skip = True

    special_nr = None
    if not quick_minimum and not quick_all:
        special_nr = input(
            f"{Fore.CYAN}Select special characters:\n[1] All default symbols ('.','-','_')\n[2] .\n[3] -\n[4] _ \n[5] Add your own symbols.\n{Style.RESET_ALL}")
    elif quick_all:
        special_nr = "1"
    elif quick_minimum:
        special_nr = "2"

    return special_nr, domains_input, skip


def generate_wordlist():
    def range_add(usernames):
        for u in usernames[:]:
            for r in range(range_min, range_max):
                usernames.extend(f"{u}{r}" for r in range(range_min, range_max))

    def add_common_nr(usernames):
        # Use "[:]:" to go through the loop once, not going through the extended usernames.
        for u in usernames[:]:
            usernames.extend(f"{u}{cn}" for cn in commonNumbers)

    def domains(usernames, skip, domains_input):
        if not skip:
            domains_split = domains_input.split(',')
            usernames = [username + "@" + domain for domain in domains_split for username in usernames]
        return usernames

    usernames = []

    # Fill the lists if it is not running easy mode.
    forenames.append(args.firstname)
    lastnames.append(args.lastname)
    if args.middlename is not None:
        middlenames.append(args.middlename)
    else:
        middlenames.append("")

    print(
        f"{Fore.GREEN}Generating wordlist for {forenames[0]}{' ' + middlenames[0] if middlenames[0] else ''} {lastnames[0]}{Style.RESET_ALL}:")

    # Check for special characters in names
    special_chars = {"ø", "æ", "å", "ä", "ö"}
    if any(char in name for char in special_chars for name in [forenames[0], middlenames[0], lastnames[0]]):
        scandinavian()

    for f in forenames:
        f = f.lower()
        for l in lastnames:
            l = l.lower()
            # The basic conversions! Will always be used.
            # First letter from lastname + name & vise versa

            usernames.append(f"{f}")
            usernames.append(f"{f[0]}{l}")
            usernames.append(f"{f}{l}")
            usernames.append(f"{f}{l[0]}")
            if not args.industry:
                usernames.append(f"{l[0]}{f}")

                # pure names
                usernames.append(f"{l}")

                # 1 - 3 letters first name & 1 to 3 letters lastname
                usernames.append(f"{f[0]}{l[0]}")
                usernames.append(f"{f[0]}{f[1]}{l[0]}{l[1]}")
                usernames.append(f"{f[0]}{f[1]}{f[2]}{l[0]}{l[1]}{l[2]}")

                # 3 letters first name & 1 to 4 letters lastname
                usernames.append(f"{f[0]}{f[1]}{f[2]}{l[0]}")
                usernames.append(f"{f[0]}{f[1]}{f[2]}{l[0]}{l[1]}")
                usernames.append(f"{f[0]}{f[1]}{f[2]}{l[0]}{l[1]}{l[2]}")
                try:
                    usernames.append(f"{f[0]}{f[1]}{f[2]}{l[0]}{l[1]}{l[2]}{l[3]}")
                except:
                    continue

                # Name and lastname
                usernames.append(f"{l}{f}")
                usernames.append(f"{l}{f[0]}")

    special_nr, domains_input, skip = questions()

    if args.middlename and not args.industry:
        middle_name_add(usernames)
    if not args.light:
        special_characters(special_nr, usernames)
    if args.commonNr:
        add_common_nr(usernames)
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

    writeCheck = input(
        f"{Fore.CYAN}Your list will have {len(usernames)} words in it. Are you sure you want to make the wordlist?[y/n]{Style.RESET_ALL}")
    if writeCheck == "y":
        write_result(usernames)
    else:
        quit(0)


if __name__ == '__main__':

    # Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--commonNr", help="Add common numbers to the back of generated usernames.",
                        action="store_true")
    parser.add_argument("-d", "--domain", help="Print with mail domain. Example: outlook.com", action="store_true")
    parser.add_argument("-e", "--easy", help="Easy mode! Just follow the text. (For non-technical people.)",
                        action="store_true")
    parser.add_argument("-F", "--firstname", help="The first name.", type=str)
    parser.add_argument("-i", "--industry", help="Print with industry standard. (Very small list)", action="store_true")
    parser.add_argument("-L", "--lastname", help="The last name.", type=str)
    parser.add_argument("-l", "--light", help="Light mode. Generates less usernames.",
                        action=argparse.BooleanOptionalAction)
    parser.add_argument("-M", "--middlename", help="The middle name.", type=str)
    parser.add_argument("-p", "--print", help="Print result", action=argparse.BooleanOptionalAction)
    parser.add_argument("-r", "--range",
                        help=f"Add numbers {range_min} to {range_max} to the end of generated username.",
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

    if args.easy:
        easy()
    generate_wordlist()
