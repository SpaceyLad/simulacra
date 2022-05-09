# Simulacra

This is a hobby project and for security research.
The code is inspired by username-anarchy, written by Andrew Horton(urbanadventurer)
If you like the code and the idea, I highly recommend visiting and try out username-anarchy for further enumeration and learning :)
https://github.com/urbanadventurer/username-anarchy

# How to use

You have to use the -f -l and -c arguments!

There is a simple explanation in the help menu which you can use with -h.
Here are some examples:

A simple wordlist and printing the result on screen. 
This will create a file calledjohn_0.txt that has 9 usernames in them.

python3 simulacra.py -f John -l Doe -c 1 -p

A very complex wordlist without print
This one will create a list with 330 different usernames.

The script is also easy to modify. I added comments so you should find where to go if you want to edit anything.

# Changelog

Version 1.0
Script created.
Added complexity 1 - 4.

# Planned features

* Make the program able to make passwordlists based on the full name.
* Optimize code.
* Make middle name an option.

# Note

Keep in mind that usually you don't want to have to many usernames.
If you do, password brute-forcing can take a long time.
It is only smart if you know how to test the usernames against the target efficiently.

Note that I am new to python and this project was started to improve my scripting skills.
I do appreciate feedback and tips. Feel free to throw me some ideas!

Written and developed by Stian Kvålshagen :]
