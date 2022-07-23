# Simulacra 1.2
Welcome to Simulacra ~
The purpose of this script is to create a wordlist with possible usernames or email addresses when you only know the persons full name.
This is useful when attacking a system where you need the username or mail, but only have access to the persons full name.
You can try to create a small wordlist and do a password dictionary attack, or maybe a large list and Fuzz a login page.
Can be used to attack AD and websites.

This is script is good at finding mail addresses, but especially against Norwegian mail addresses because of the Norwegian letter conversion mode and domain mode.

### What is does Simulacra mean?
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
