# Simulacra 1.2
Welcome to Simulacra ~
The purpose of this script is to create a wordlist with possible usernames or email addresses when you only know the persons full name.
This is useful when attacking a system where you need the username or mail, but only have access to the persons full name.
You can try to create a small wordlist and do a password dictionary attack, or maybe a large list and Fuzz a login page.
Can be used to attack AD and websites.

This is script is good at finding mail addresses, but especially against Norwegian mail addresses because of the Norwegian letter conversion mode and domain mode.

## What is does Simulacra mean?
A simulacrum is a representation or imitation of a person or thing.
## How to use
You must use the -F -L and -C arguments or enable easy mode with -e.
Play around with easy mode to explore all functions, and then adjust them as you please.
There is a simple explanations in the help menu.

### Examples
##### Easy mode
python3 simulacra.py -e
##### Small username list
python3 simulacra.py -F John -L Doe -c 1 -p
##### Medium username list [Middle name]
python3 simulacra.py -F John -M Sneaky -L Doe -c 3
##### Large username list [Middle name & Domain]
python3 simulacra.py -F Jøhn -M Snæky -L Doe -c 4 -no -d


The filters in use are on top, feel free to modify them!
## Changelog
### 1.2 - Major update
* Added option for converting Norwegian letters with double and single letters.
* Added new complexity with 0 - 9999 numbers behind every username.
* Removed complexity 3 because of poor optimalisation
* Remove duplicates.
* Tweaked the number gens not including the original value without number in complexity 3 and 4.
* Improved flow in easy mode
* Improved domain function. You can now add more than 1 domain.
* Default complexity is 2 (Recommended)
* Fixed a handful of logic flaws.
* Make it possible to add own symbols in complexity 2.
### 1.1 - Minor update
* Easy mode added
* Colours added
* Domain added
* Middle name option added
* Cleaner code
### 1.0 - Creation
* First name added
* Last name added
* Print function added
* Write to file added
* Added complexity 1 - 4.
## Planned features
* Make option that only follows industry standard usernames. (Like j.smith)
* Implement quick mode for small and large lists.

## Note
Keep in mind that usually you don't want to have to many usernames.
If you do, password brute-forcing can take a long time. So try to stay within complexity 2 as long as the user is not using mail with numbers in it.
The list can range from 8 usernames to 1,6 million with default filters.

Note that I am new to python and this project was started to improve my scripting skills.
I do appreciate feedback and tips. Feel free to throw me some ideas or bugs you encounter.

This is a hobby project and for security research.
The code is inspired by username-anarchy, written by Andrew Horton(urbanadventurer)
If you like the code and the idea, I highly recommend visiting and try out username-anarchy for further enumeration and learning :)
https://github.com/urbanadventurer/username-anarchy

Written and developed by Stian Kvålshagen :]
