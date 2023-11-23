# Simulacra 1.4

![DALL·E 2023-11-23 13 38 18 - A horror-themed and artistic cover art for 'Simulacra'  The scene is set in a dimly lit, eerie office environment  In the center, a person appears ner](https://github.com/SpaceyLad/simulacra/assets/87969837/e0a6aa22-450b-4f4c-95fe-3cbbbb6215a8)

Welcome to Simulacra ~
The purpose of this script is to create a wordlist with possible usernames or email addresses when you only know the person’s full name.
This is useful when attacking a system where you need the username or mail, but only have access to the persons full name.
You can try to create a small wordlist and do a password dictionary attack, or maybe a large list and Fuzz a login page.
Can be used to attack AD, websites and much more.

This is script is good at finding email addresses, but especially against Scandinavic mail addresses because of the letter conversion mode and domain mode.

### What is does Simulacra mean?
A simulacra is a representation or imitation of a person, object, or phenomenon. It often refers to a copy or simulation that might not have a direct connection to the original, creating a sense of detachment from reality.

## How to use
You must use the -F (First name)-L (Last name) or enable easy mode with -e.
Play around with easy mode to explore all functions, and then adjust them as you please.
There is a simple explanation in the help menu.
The script supports conversion of names that includes both Norwegian/Danish and Swedish/Finnish characters.
The filters in use are on top, feel free to modify them!

### Examples
##### Help
python3 simulacra.py -h
##### Easy mode
python3 simulacra.py -e
##### Industry standard
python3 simulacra.py -F John -L Doe -i
##### Small username list
python3 simulacra.py -F John -L Doe
##### Medium username list with common numbers behind
python3 simulacra.py -F John -M Sneaky -L Doe -c
##### Large username list with range and domain
python3 simulacra.py -F Jøhn -M Snæky -L Doe -r -d


## Planned features
* Add support for more Nation specific characters.

## Note
Keep in mind that usually you don't want to have to many usernames.
When I say Norwegian, it means æ,ø,å which is also Danish characters.
When I say Swedish, it means ä,ö,å which is also Finnish characters.
If you do, password brute-forcing can take a long time. So try to stay within complexity 2 as long as the user is not using mail with numbers in it.
The list can range from 8 usernames to 1,6 million with default filters.

I do appreciate feedback and tips. Feel free to throw me some ideas or bugs you encounter.

This is a hobby project and for security research.
The code is inspired by username-anarchy, written by Andrew Horton(urbanadventurer)
If you like the code and the idea, I highly recommend visiting and try out username-anarchy for further enumeration and learning :)
https://github.com/urbanadventurer/username-anarchy

Written and developed by Stian Kvålshagen :]
