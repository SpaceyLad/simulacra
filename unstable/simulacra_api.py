""" *------------------------------------------------------------------------------------------------------------*
    Author: Stian Kvålshagen
    Date: 19.01.2024
    Type: API
*------------------------------------------------------------------------------------------------------------* """


def special_characters(special_nr, usernames, forenames, lastnames, industry):
    global special

    def non_light_mode(usernames):
        for f in forenames:
            for l in lastnames:
                for x in special:
                    f = f.lower()
                    l = l.lower()
                    if industry:
                        usernames.append(f"{f}.{l}")
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
            symbols = input(f"Which symbols do you want to use? Separate with comma (,)\n")
            input_list = symbols.split(',')
            for special_input in input_list:
                special.append(special_input)
    non_light_mode(usernames)
    return special


def middle_name_add(usernames, forenames, lastnames, middlenames, special):
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

    for f in forenames:
        for l in lastnames:
            for m in middlenames:
                f = f.lower()
                m = m.lower()
                l = l.lower()
                add_middle_name(usernames, m)
                add_initial_variations(usernames, f, m, l, special)
                add_name_variations(usernames, f, m, l, special)


# Convert Norwegian/Danish or Swedish letters into single and double letters.
def scandinavian(name_parts):

    def scandinavian_letter_check(lang_letters, name_parts):
        return any(l in name_part for name_part in name_parts for l in lang_letters)

    def convert_letters(combo_1, combo_2, combo_3):
        # Set up the list of name categories to check
        name_categories = [name_parts]

        # Iterate through each name category and apply the conversion rules
        for name_category in name_categories:
            converted_names = []

            for name in name_category:
                name_lower = name.lower()

                for i, combo in enumerate(combo_1):
                    if combo in name_lower:
                        # Replace with single letter version and add to list
                        converted_single = name_lower.replace(combo, combo_2[i])
                        if converted_single not in converted_names:
                            converted_names.append(converted_single)

                        # Replace with double letter version and add to list
                        converted_double = name_lower.replace(combo, combo_3[i])
                        if converted_double not in converted_names:
                            converted_names.append(converted_double)

            # Add the converted names to the current name category
            name_category.extend(converted_names)

    norwegian_letters = ["æ", "ø", "å"]
    if scandinavian_letter_check(norwegian_letters, name_parts):
        nor_combo_1, nor_combo_2, nor_combo_3 = norwegian_letters, ["a", "o", "a"], ["ae", "oo", "aa"]
        convert_letters(nor_combo_1, nor_combo_2, nor_combo_3)

    swedish_letters = ["ä", "ö", "å"]
    if scandinavian_letter_check(swedish_letters, name_parts):
        swe_combo_1, swe_combo_2, swe_combo_3 = swedish_letters, ["a", "o", "a"], ["aa", "oo", "aa"]
        convert_letters(swe_combo_1, swe_combo_2, swe_combo_3)


def generate_wordlist(f, m, l, domains_input, industry, range_nr, range_bool, range_min, range_max, common_box,
                      range_box, specific_box):
    forenames = []
    lastnames = []
    middlenames = []

    def range_add(usernames, range_min, range_max):
        range_max = range_max + 1
        for u in usernames[:]:
            usernames.extend(f"{u}{r}" for r in range(range_min, range_max))

    def add_common_nr(usernames, commonNumbers):
        # Use "[:]:" to go through the loop once, not going through the extended usernames.
        for u in usernames[:]:
            usernames.extend(f"{u}{cn}" for cn in commonNumbers)

    def domains(usernames, domains_input):
        domains_split = domains_input.split(',')
        usernames = [username + "@" + domain for domain in domains_split for username in usernames]
        return usernames

    usernames = []

    # Fill the lists if it is not running easy mode.

    forenames.append(f)
    lastnames.append(l)
    if m is not None:
        middlenames.append(m)
    else:
        middlenames.append("")

    print(
        f"Generating wordlist for {forenames[0]}{' ' + middlenames[0] if middlenames[0] else ''} {lastnames[0]}:")

    for f in forenames:
        f = f.lower()
        for l in lastnames:
            l = l.lower()
            # The basic conversions! Will always be used.
            # First letter from lastname + name & vise versa

            usernames.append(f"{f}")
            usernames.append(f"{f[0]}{l}")
            usernames.append(f"{f}{l}")
            usernames.append(f"{f}.{l}")
            if m:
                usernames.append(f"{f}.{m}.{l}")
            usernames.append(f"{f}{l[0]}")
            if not industry:
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

    # Check for special characters in names
    special_chars = {"ø", "æ", "å", "ä", "ö"}
    if middlenames is not None:
        if any(char in name for char in special_chars for name in [forenames[0], middlenames[0], lastnames[0]]):
            name_parts = forenames + lastnames + (middlenames if m else [])
            scandinavian(name_parts)
    else:
        if any(char in name for char in special_chars for name in [forenames[0], lastnames[0]]):
            middlenames = []
            name_parts = forenames + lastnames + (middlenames if m else [])
            scandinavian(name_parts)

    # TODO: Make prompt for speical chars!
    special_nr = "1"
    special = special_characters(special_nr, usernames, forenames, lastnames, industry)

    scandinavian(usernames)

    if m and not industry:
        middle_name_add(usernames, forenames, lastnames, middlenames, special)

    if specific_box or common_box:
        add_common_nr(usernames, range_nr)

    if range_box:
        range_add(usernames, range_min, range_max)
    if domains_input:
        usernames = domains(usernames, domains_input)

    # Remove duplicates from list
    usernames = list(dict.fromkeys(usernames))

    return usernames
