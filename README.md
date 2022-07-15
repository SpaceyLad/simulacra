# Simulacra 1.1
Welcome to my little side project!
The purpose of this script is to create a wordlist with possible usernames when you only know the persons full name.
This is useful when attacking a system where you need the username, but only have access to the persons full name.
You can try to create a small wordlist and do a password brute-force attack, or maybe a large list and Fuzz a login page.

This is a hobby project and for security research.
The code is inspired by username-anarchy, written by Andrew Horton(urbanadventurer)
If you like the code and the idea, I highly recommend visiting and try out username-anarchy for further enumeration and learning :)
https://github.com/urbanadventurer/username-anarchy

## How to use
You must use the -F -L and -C arguments or enable easy mode with -e.
There is a simple explanation in the help menu.

### Examples
##### Easy mode
python3 simulacra.py -e
##### Small username list
python3 simulacra.py -F John -L Doe -c 1 -p  
##### Medium username list [Middle name]
python3 simulacra.py -F John -M Sneaky -L Doe -c 3 
##### Large username list [Middle name & Domain]
python3 simulacra.py -F Jane -M Marry -L Doe-c 4 -d gmail.com


The filters in use are on top, feel free to modify them!
## Changelog
### Version 1.1
* Easy mode added
* Colours added
* Domain added
* Middle name option added
* Cleaner code

### Version 1.0
* First name added
* Last name added
* Print function added
* Write to file added
* Added complexity 1 - 4.

## Planned features
* Make the program able to make password lists based on the full name.
* Make option that only follows industry standard usernames. (Like j.smith)

## Note
Keep in mind that usually you don't want to have to many usernames.
If you do, password brute-forcing can take a long time.
It is only smart if you know how to test the usernames against the target efficiently.

Note that I am new to python and this project was started to improve my scripting skills.
I do appreciate feedback and tips. Feel free to throw me some ideas!

Written and developed by Stian Kvålshagen :]
