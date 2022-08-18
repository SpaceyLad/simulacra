# Simulacra 1.3
Welcome to Simulacra ~
The purpose of this script is to create a wordlist with possible usernames or email addresses when you only know the person’s full name.
This is useful when attacking a system where you need the username or mail, but only have access to the persons full name.
You can try to create a small wordlist and do a password dictionary attack, or maybe a large list and Fuzz a login page.
Can be used to attack AD, websites and more.

This project is marked as "done". But I will note down ideas and come back to it in the future when I have more knowledge.

This is script is good at finding mail addresses, but especially against Scandinavic mail addresses because of the letter conversion mode and domain mode.

### What is does Simulacra mean?
A simulacrum is a representation or imitation of a person or thing.
## How to use
You must use the -F (First name)-L (Last name) and -c (Complexity) arguments or enable easy mode with -e.
Play around with easy mode to explore all functions, and then adjust them as you please.
There is a simple explanation in the help menu.
The script supports conversion of names that includes both Norwegian and Swedish characters.
The filters in use are on top, feel free to modify them!

### Examples
##### Easy mode
python3 simulacra.py -e
##### Small username list
python3 simulacra.py -F John -L Doe -c 1 -p
##### Medium username list [Middle name]
python3 simulacra.py -F John -M Sneaky -L Doe -c 3
##### Large username list [Middle name, Norwegian chars & Domain]
python3 simulacra.py -F Jøhn -M Snæky -L Doe -c 4 -no -d
##### Very Large username list [Middle name, Swedish chars, Domain & quick add all]
python3 simulacra.py -F Jöhn -M Snäky -L Doe -c 4 -sw -d -qa


## Planned features
* Make option that only follows industry standard usernames. (Like j.smith)
* Add support for more Nation specific characters.
## Note
Keep in mind that usually you don't want to have to many usernames.
When I say Norwegian, it means æ,ø,å which is also Danish characters.
When I say Swedish, it means ä,ö,å which is also Finnish characters.
If you do, password brute-forcing can take a long time. So try to stay within complexity 2 as long as the user is not using mail with numbers in it.
The list can range from 8 usernames to 1,6 million with default filters.

Note that I am new to python and this project was started to improve my scripting skills.
I do appreciate feedback and tips. Feel free to throw me some ideas or bugs you encounter.

This is a hobby project and for security research.
The code is inspired by username-anarchy, written by Andrew Horton(urbanadventurer)
If you like the code and the idea, I highly recommend visiting and try out username-anarchy for further enumeration and learning :)
https://github.com/urbanadventurer/username-anarchy

Written and developed by Stian Kvålshagen :]
